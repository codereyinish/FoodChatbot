# IMPORT PACKAGES
from fastapi import FastAPI , Request #Request to validate type hint of JSON request
from pydantic import BaseModel
from typing import Any, Dict, List #for type hints

from collections import Counter
import generichelper

import dbOperations


app = FastAPI()


#Helper functions for each intent

in_progress_order = {}


def handle_order_add(parameters:Dict[str, Any], session_id:str, query_text:str) -> Dict[str, Any]:
    item =  parameters.get("food_items", [])
    quantities = parameters.get("quantity",[])

    #Normalize both variables
    item, quantities = generichelper.NormalizeVariable(item, quantities)
    print(query_text)
    if len(item)!= len(quantities):
        fulfillmentText = "Sorry I didn't understand. Can you please specify the food items and quantity properly please'"
    #later try to add multiple items together , 1 lassi and 2 momo
    else:
       new_food_dictionary = dict(zip(item, quantities))
    if session_id in in_progress_order: #USE EXISTING SESSION
        #Check if user is trying to make an update or add more
        update_keywords = ["change", "instead", "make", "replace", "no", "not", "update", "only"]
        if any(word in query_text for word in update_keywords):
            #REPLACEMENT
            in_progress_order[session_id].update(new_food_dictionary)
        else:
            #INCREMENT
            in_progress_order[session_id] = dict(Counter(in_progress_order.get(session_id, {})) + Counter(new_food_dictionary))  # use Counter when we want to comnbine multiple key's values together
    else: #NEW SESSION_ID WILL BE CREATED BY PYTHON DICT
        in_progress_order[session_id]= new_food_dictionary
    return generichelper.ReturnFulfillmentMessage(in_progress_order[session_id])



def handle_order_remove(parameters: Dict[str, Any], session_id:str, query_text:str, all_params_present:bool)-> Dict[
    str,
Any]:
    print("YO")
    print(in_progress_order)
    item = parameters.get("items", [])
    quantities = parameters.get("quantity", [])

    # Normalize both variables
    item, quantities = generichelper.NormalizeVariable(item, quantities)
    keywords_for_all = ["all", "everything", "entire", "whole"]


    #Remove items from a particular session_id
    def removeItems():
        removable_item_dict = dict(zip(item, quantities))
        # print(removable_item_dict)
        if session_id in in_progress_order:
         in_progress_order[session_id] = dict(Counter(in_progress_order[session_id]) - Counter(removable_item_dict))
         return generichelper.ReturnFulfillmentMessage(in_progress_order[session_id])

    #CONDITION 1
    if not item:
        return{
            "fulfillmentText" : "Which item do you want to remove? "
        }
    #CONDITION 2
    if not quantities:
    # either we got "random char" or "all keyword" , we cant discard all keyword
        if any(word in query_text for word in keywords_for_all):
            #get existing quantity for  item from the session_dict
            existing_items = in_progress_order.get(session_id, {})
            quantities = [existing_items.get(i, 0) for i in item]
            print (quantities)
            return removeItems()

        return {
            "fulfillmentText": f"How many { ','.join(item)} you want to remove? "
        }


#Formality CHeck if multiple items entered together, every item should have corresponding quantities
    if len(item)!= len(quantities):
        return {
            "fulfillmentText": "Sorry I didn't understand. Can you please specify the food items and quantity "
                               "properly please'"
        }
    #CONDITION 3
    return removeItems()



def handle_order_reset(session_id:str):
    #Clear all items from given current session
    # print(in_progress_order[session_id])
    in_progress_order[session_id].clear()
    # print("after")
    # print(in_progress_order[session_id])

def handle_order_track(parameters: Dict[str, Any], session_id:str)-> Dict[str, Any]:
    pass

def handle_order_complete(parameters: Dict[str, Any], session_id:str)-> Dict[str, Any]:
    if session_id not in in_progress_order:
        return {
            "fulfillmentText": "I'm having a trouble finding your order. Sorry! Can you place a new oMier please?"
        }
    order = in_progress_order[session_id]
    order_id = save_to_db(order)
    if order_id == -1:
        return{
            "fulfillmentText": "Sorry, I couldn't process your order due to a backend error. " \
            "Please place a new order again"
        }
    #Insertion is successful so does trigger for total_price
    order_total_price = dbOperations.get_total_order_price(order_id)
    return{
        "fulfillmentText":  f"Awesome. We have placed your order. "\
                            f"Here is your order id # {order_id}. " \
                            f"'Your order total is {order_total_price} which you can pay at the time of delivery!"
        }


def save_to_db(order: dict):
    #get next order_id from database
    next_order_id = dbOperations.get_next_order_id()
    if next_order_id == -1:
        return -1
    for food_item, quantity in order.items():
       result =  dbOperations.insert_order_item( next_order_id, food_item, quantity)
       if result == -1:
           return -1
       return next_order_id



#Main WEBHOOK HANDLER

@app.post("/")
async def handle_request(request: Request):
    req_json = await request.json()

#EXTRACTION

    intent = req_json.get("queryResult", {}).get("intent", {}).get("displayName")
    parameters = req_json.get("queryResult", {}).get("parameters", {})
    query_text = req_json.get("queryResult", {}).get("queryText", "")
    all_params_present = req_json.get("queryResult", {}).get("allRequiredParamsPresent", False)

    session_path = req_json.get("session", "")
    session_id = session_path.split("/sessions/")[-1]

    intent_handle_dict = {
    "Order.Add-context:ongoing-order" : handle_order_add,
    "Order.remove-context:ongoing-order": handle_order_remove,
    "Order.reset-context:ongoing-order": handle_order_reset,
    "Order.track-context:ongoing-order" : handle_order_track,
    "Order.complete-context:ongoing_order": handle_order_complete
    }
    if intent == "Order.Add-context:ongoing-order":
        return intent_handle_dict[intent](parameters, session_id, query_text)
    elif intent == "Order.remove-context:ongoing-order":
        return intent_handle_dict[intent](parameters, session_id, query_text, all_params_present)
    elif intent == "Order.reset-context:ongoing-order":
        return intent_handle_dict[intent](session_id)
    else:
        return intent_handle_dict[intent](parameters, session_id)















# if intent_name == "order.track-context:ongoing-order":
#     # response = {"fulfillmentText": "Your order is tracked"}
#     try:
#         order_id = int(parameters.get('order_id', 0))
#     except ValueError:
#         return{"fulfillment text": "Invalid Order Id"}
#     order_status = dbhelper.get_order_status(order_id)
#     if order_status:
#         return{"fulfillmentText": f"Your order status is: {order_status}"}
#     else: #if None is returned
#         return {"fulfillmentText": "Order not found."}
# pass
# #Route functions based on intent
