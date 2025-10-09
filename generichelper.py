def get_str_from_food_dict(food_dict:Dict):
    return ",".join([f"{int(value)} {key}" for key, value in food_dict.items()])

# if __name__ == "__main__":
#     print(get_str_from_food_dict({"momo": 2, "thali": 1}))