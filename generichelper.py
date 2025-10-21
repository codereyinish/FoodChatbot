from typing import Any, Dict, List #for type hints
def get_str_from_food_dict(food_dict:Dict[str,Any]):
    return ",".join([f"{int(value)} {key}" for key, value in food_dict.items()])

# if __name__ == "__main__":
#     print(get_str_from_food_dict({"momo": 2, "thali": 1}))

# Nomralize both variables..#dialogflow returns single variable as int or float, not list..add momo --> quantity =
    # 1.0 , not [1]
def NormalizeVariable(item, quantities):
    if isinstance(item, str):
        item = [] if item.strip()== "" else [item]
    if isinstance(quantities, (int, float)):
        quantities = [quantities]
    elif isinstance(quantities, str):
        quantities = [] if quantities.strip() == "" else [quantities]
    return item,quantities  #return tuple

def ReturnFulfillmentMessage(order_dict):
    order_str = get_str_from_food_dict(order_dict)
    fulfillmentText = f"So far you have: {order_str}. Do you need anything else?"
    print("🧾 Current in_progress_order:", order_dict)  # for debugging
    return {
        "fulfillmentText": fulfillmentText
    }


#Remove items from a particular session_id
def removeItems(item, quantities, session_id, in_progress_order):
    removable_item_dict = dict(zip(item, quantities))
    if session_id not in in_progress_order:
        return {
            "fulfillmentText": "I having a trouble finding your order. Please place your order again"
        }
    # Else start deleting
    order_dict = in_progress_order[session_id]
    removedItems = []
    absentItems = []
    for item, qty_to_remove in removable_item_dict.items():
        if item in order_dict:
            if order_dict[item] > qty_to_remove:
                order_dict[item] -= qty_to_remove
            else:  # remove completely the item and its value
                del order_dict[item]
            removedItems.append(item)
        else:
            absentItems.append(item)

    # BUILD THE MESSAGE telling about Deleted and Absent Items together in a Message
    message_parts = []
    if removedItems:
        message_parts.append(f"Removed: {', '.join(removedItems)}")
    if absentItems:
        message_parts.append(f"Not in your order: {' ,'.join(absentItems)}")
    if len(order_dict)!=0:
        message_parts.append(f" Your cart now looks like this:  {showItems(order_dict)}")
    else:
        message_parts.append(f"Your cart is now empty")
    return {
        "fulfillmentText": " . ".join(message_parts)
    }

def showItems(order_dict):
    joined_str = ", ".join(f"{int(q)} {i}"  for i, q in order_dict.items())
    return joined_str



def validate_session_id_and_retrieve_order(session_id, in_progress_order):
    if session_id not in in_progress_order:
        return {
            "fulfillmentText": "I'm having a trouble finding your order. Sorry! Can you place a new oMier please?"
        }
    order_dict = in_progress_order[session_id]
    return order_dict


def   check_item_in_the_order_list(order_dict, item):
    #item is a list , not a dictionary so retrieve value from the list
    if isinstance(item, list) and len(item)>0:#there must be a item
        item = item[0]
    return item in order_dict #if present , returns true , if not false



