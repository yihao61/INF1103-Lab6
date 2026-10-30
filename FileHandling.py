import json
import os

def save_inventory(inv_list, filepath):
    print("\nSaving inventory.....")

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(inv_list, file, indent=4)

    print("Inventory Saved.....\n")
    return

def load_inventory(filepath):
    inv_list = []

    if not os.path.exists(filepath):

        print(f"{filepath} does not exists, creating a blank file...")
        with open(filepath, "w", encoding="utf-8") as file:
            pass
        return inv_list
    
    with open(filepath, "r", encoding="utf-8") as file:
        print(f"{filepath} found.")
        inv_list = json.load(file)

    print("Inventory loaded successfully!")
    return inv_list
