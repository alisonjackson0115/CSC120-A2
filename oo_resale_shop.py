class ResaleShop:

    from typing import Dict, Optional
    # What attributes will it need?
    inventory : list = []
    computer : Dict
    item_id : int

    # storing the inventory for the store
    # buying a computer (add to inventory)
    # selling a computer (remove from inventory)



    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory : list, computer : Dict, item_id: int):
        self.inventory = inventory
        self.computer = computer
        self.item_id = item_id

    # What methods will you need?
        
    def buy(computer: Dict, inventory: list):
        inventory.append(computer)
        return inventory.index(computer)
    
    
    def sell(item_id: int, inventory: list):
        if inventory[item_id] is not None:
            inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
    

    def print_inventory(inventory: list):
    # If the inventory is not empty
        if inventory:
            # For each item
            for item in inventory:
                # Print its details
                print(f'Item ID: {inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")

    def main():
        pass
    main()
