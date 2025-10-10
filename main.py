# IMPORT PACKAGES
from fastapi import FastAPI , Request #Request to validate type hint of JSON request
from pydantic import BaseModel
from typing import Any, Dict, List #for type hints

from collections import Counter
import generichelper

import dbhelper
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
    item = parameters.get("items", [])
    quantities = parameters.get("quantity", [])

    # Normalize both variables
    item, quantities = generichelper.NormalizeVariable(item, quantities)
    print (f"{quantities} hello")
    print(f"{item}Bye")
    keywords_for_all = ["all", "everything", "entire", "whole"]

    if not item:
        return{
            "fulfillmentText" : "Which item do you want to remove? "
        }
    if not quantities:
    # either we got "random char" or "all keyword" , we cant discard all keyword
        if any(word in query_text for word in keywords_for_all):
            #get existing quantity for  item from the session_dict
            existing_items = in_progress_order.get(session_id, {})
            quantities = [existing_items.get(i, 0) for i in item]
            print (quantities)
            return {
                "fulfillmentText": "Thanks"
            }
        return {
            "fulfillmentText": f"How many { ','.join(item)} you want to remove? "
        }


#Formality CHeck if multiple items entered together, every item should have corresponding quantities
    if len(item)!= len(quantities):
        return {
            "fulfillmentText": "Sorry I didn't understand. Can you please specify the food items and quantity "
                               "properly please'"
        }

    removable_item_dict = dict(zip(item,quantities))
        # print(removable_item_dict)
    #Remove items from a particular session_id
    if session_id in in_progress_order:
         in_progress_order[session_id] = dict(Counter(in_progress_order[session_id]) - Counter(removable_item_dict))
         return generichelper.ReturnFulfillmentMessage(in_progress_order[session_id])
    return {
            "fulfillmentText" : f"Sorry Session Expired or Not Found"
        }



def handle_order_track(parameters: Dict[str, Any], session_id:str)-> Dict[str, Any]:
    pass

def handle_order_complete(parameters: Dict[str, Any], session_id:str)-> Dict[str, Any]:
    pass



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
    "Order.track-context:ongoing-order" : handle_order_track,
    "Order.complete-context:ongoing_order": handle_order_complete
    }
    if intent == "Order.Add-context:ongoing-order":
        return intent_handle_dict[intent](parameters, session_id, query_text)
    elif intent == "Order.remove-context:ongoing-order":
        return intent_handle_dict[intent](parameters, session_id, query_text, all_params_present)
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
