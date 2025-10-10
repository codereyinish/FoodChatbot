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