import logging

# Configure basic logging to log INFO level and higher
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)

# Inventory & Item Details Setup
inventory = ["apple", "banana", "orange", "grape", "mango"]  # 'mango' added to demonstrate error logging
item_details = {
    "apple": {"price": 1.2, "quantity": 10},
    "banana": {"price": 0.8, "quantity": 15},
    "orange": {"price": 1.5, "quantity": 8},
    "grape": {"price": 2.0, "quantity": 12}
}

logging.info("Starting inventory iteration...")

for item in inventory:
    logging.info(f"Processing item: {item}")
    
    # Check if the item exists in details dictionary
    if item in item_details:
        for key, value in item_details[item].items():
            print(f"  {key}: {value}")
    else:
        # Log an error if an item from inventory is missing in details
        logging.error(f"Item '{item}' not found in item_details mapping!")

# Data Structures Example
logging.info("Demonstrating Python data structures...")

names = ["Naresh", "Rahul", "Naresh"]         # List
coordinates = (28.6, 77.2)                   # Tuple
student = {"name": "Naresh", "age": 22}      # Dict
unique_names = set(names)                    # Set derived from list

logging.info(f"Loaded student data for {student['name']} (Age: {student['age']})")
logging.info(f"Unique names count: {len(unique_names)}")