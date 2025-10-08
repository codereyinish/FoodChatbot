# IMPORT PACKAGES
from fastapi import FastAPI , Request #Request to validate type hint of JSON request
from pydantic import BaseModel
from typing import Any, Dict, List #for type hints

from collections import Counter
import dbhelper
app = FastAPI()

#Helper functions for each intent


in_progress_order = {
    "session_id_1": {"pizza" :2},
    "session_id_2": {"MangoLassi" : 3}
}
def handle_order_add(parameters:Dict[str, Any], session_id:str) -> Dict[str, Any]:
    item =  parameters.get("food_items", [])
    quantities = parameters.get("quantity",[])
    if len(item)!= len(quantities):
        fulfillmentText = "Sorry I didn't understand. Can you please specify the food items and quantity properly please'"
    #later try to add multiple items together , 1 lassi and 2 momo
    else:
       new_food_dictionary = dict(zip(item, quantities))
    if session_id in in_progress_order:
        in_progress_order[session_id] = dict(Counter(in_progress_order.get(session_id, {})) + Counter(new_food_dictionary))
    else:
        in_progress_order[session_id]= new_food_dictionary
    fulfillmentText = f" Successfully Added {item} {quantities}"
    print("🧾 Current in_progress_order:", in_progress_order)
    return{
        "fulfillmentText": fulfillmentText
    }


def handle_order_remove(parameters: Dict[str, Any], session_id:str)-> Dict[str, Any]:
    item = parameters.get("item", {})
    quantities = parameters.get("quantity, 1")
    return{
        "fulfillmentText":f"Removed {quantities} {item} from your order. (session: {session_id})"
    }

def handle_order_track(parameters: Dict[str, Any], session_id:str)-> Dict[str, Any]:
    pass

def handle_order_complete():
    pass


#Main WEBHOOK HANDLER

@app.post("/")
async def handle_request(request: Request):
    req_json = await request.json()

#EXTRACTION

    intent = req_json.get("queryResult", {}).get("intent", {}).get("displayName")
    parameters = req_json.get("queryResult", {}).get("parameters", {})

    session_path = req_json.get("session", "")
    session_id = session_path.split("/sessions/")[-1]

    intent_handle_dict = {
    "Order.Add-context:ongoing-order" : handle_order_add,
    "Order.remove-context:ongoing-order": handle_order_remove,
    "Order.track-context:ongoing-order" : handle_order_track,
    "Order.complete-context:ongoing_order": handle_order_complete
    }

    return intent_handle_dict[intent](parameters, session_id)



    #
    # else:
    #     if intent_name == "order.track-context:ongoing-order":
    #         # response = {"fulfillmentText": "Your order is tracked"}
    #         try:
    #             order_id = int(parameters.get('order_id', 0))
    #         except ValueError:
    #             return{"fulfillment text": "Invalid Order Id"}
    #         order_status = dbhelper.get_order_status(order_id)
    #         if order_status:
    #             return{"fulfillmentText": f"Your order status is: {order_status}"}
    #         else: #if None is returned
    #             return {"fulfillmentText": "Order not found."}
    #     #Route functions based on intent
    #     response = {"FulfillmentText": "Sorry I don't know how to handle that intent"}
    #     return response

#In Progress Order
inprogress_order = {
    "session_id_1" : {"pizzas:2", "samosa:1"},
    "session_id_2" : {"choole":1}
}








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
