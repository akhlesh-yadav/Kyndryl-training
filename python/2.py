#Create a small inventory list and a dictionary of item details; iterate and print results.
inventory = ["apple", "banana", "orange", "grape"]
item_details = {
    "apple": {"price": 1.2, "quantity": 10},
    "banana": {"price": 0.8, "quantity": 15},
    "orange": {"price": 1.5, "quantity": 8},
    "grape": {"price": 2.0, "quantity": 12}
}

for item in inventory:
    print(f"Item: {item}")
    for key, value in item_details[item].items():
        print(f"  {key}: {value}")


#Can use list/tuple/dict/set for common tasks.
names = ["Naresh", "Rahul", "Naresh"]       # List
coordinates = (28.6, 77.2)                 # Tuple
student = {"name": "Naresh", "age": 22}    # Dict
unique_names = {"Naresh", "Rahul"}         # Set
