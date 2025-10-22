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

    #Normalize both variables to remove "" for invalid item and quantity
    item, quantities = generichelper.NormalizeVariable(item, quantities)
    if len(item)==0:
        return{
            "fulfillmentText": "Which item you want to add?"
        }


    if len(item)!= len(quantities):
        return{
        "fulfillmentText" : "Sorry I didn't understand. Can you please specify the food items and quantity properly "}

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
    item = parameters.get("items", [])
    quantities = parameters.get("quantity", [])

    # Normalize both variables
    item, quantities = generichelper.NormalizeVariable(item, quantities)
    keywords_for_all = ["all", "everything", "entire", "whole"]


    #CONDITION 1
    if len(item) ==0:
        return{
            "fulfillmentText" : "Which item do you want to remove? "
        }
    order_dict = generichelper.validate_session_id_and_retrieve_order(session_id, in_progress_order)
    result = generichelper.check_item_in_the_order_list(order_dict, item)
    if not result:
        return {
            "fulfillmentText": f"{generichelper.convert_list_to_string(item)} isn’t in your cart. Please check the "
                               f"name or "
                               f"add it "
                               f"first."
        }

    #CONDITION 2
    if not quantities:
    # either we got "random char" or "all keyword" , we cant discard all keyword
        if any(word in query_text for word in keywords_for_all):
            #get existing quantity for  item from the session_dict
            existing_items = in_progress_order.get(session_id, {})
            quantities = [existing_items.get(i, 0) for i in item]
            return generichelper.removeItems(item, quantities, session_id, in_progress_order)
        #if any random character entered like ("a" , "ermm" instead of valid integer for quantity)
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
    return generichelper.removeItems(item, quantities, session_id, in_progress_order)



def handle_order_reset(session_id:str):
    #Clear all items from given current session
    in_progress_order[session_id].clear()
    return{
        "fulfillmentText": "Your cart is cleared."
    }


def save_to_db(order: dict):
    #get next order_id from database
    next_order_id = dbOperations.get_next_order_id()
    if next_order_id == -1:
        return -1
    for food_item, quantity in order.items():
       result =  dbOperations.insert_order_item( next_order_id, food_item, quantity)
       print(f"{food_item} inserted")
       if result == -1:
           return -1

    return next_order_id



def handle_order_display(session_id):
    order_dict = generichelper.validate_session_id_and_retrieve_order(session_id, in_progress_order)
    if len(order_dict)!=-0:
        return {
            "fulfillmentText": f"Your cart currently looks like this:  {generichelper.showItems(order_dict)} "
        }
    return{
        "fulfillmentText": "Your cart is empty at the moment. 🪄 Add something tasty to get started!"
    }
        
        




def handle_order_complete(parameters: Dict[str, Any], session_id:str)-> Dict[str, Any]:
    order_dict = generichelper.validate_session_id_and_retrieve_order(session_id, in_progress_order)
    order_id = save_to_db(order_dict)
    if order_id == -1:
        return{
            "fulfillmentText": "Sorry, I couldn't process your order due to a backend error. " \
            "Please place a new order again"
        }
    #Insertion is successful so does trigger for total_price
    order_total_price = dbOperations.get_total_order_price(order_id)
    del in_progress_order[session_id] #Remove the order from the buffer storage since it has been already stroed in
    # the database
    return{
        "fulfillmentText":  f"Awesome. We have placed your order. "\
                            f"Here is your order id #{order_id}. " \
                            f"'Your order total is ${order_total_price} which you can pay at the time of delivery!"
        }





def handle_order_track( parameters: Dict[str, Any]):
    track_id = parameters.get("order_id")
    status = dbOperations.validateTrackID(track_id)
    if status == -1:
        return{
                "fulfillmentText": "Hmm, it looks like there's no order linked to that tracking ID. Please enter the correct one."
        }
    return{
        "fulfillmentText": f"Your order is {status}"
    }




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
    "order.track-context:ongoing-order" : handle_order_track,
    "Order.complete-context:ongoing_order": handle_order_complete,
    "Order.display-context:ongoing-order": handle_order_display
    }
    if intent == "Order.Add-context:ongoing-order":
        return intent_handle_dict[intent](parameters, session_id, query_text)
    elif intent == "Order.remove-context:ongoing-order":
        return intent_handle_dict[intent](parameters, session_id, query_text, all_params_present)
    elif intent == "Order.reset-context:ongoing-order":
        return intent_handle_dict[intent](session_id)
    elif intent == "order.track-context:ongoing-order":
        return intent_handle_dict[intent](parameters)
    elif intent ==  "Order.display-context:ongoing-order":
        return intent_handle_dict[intent](session_id)
    else:
        return intent_handle_dict[intent](parameters, session_id)
















