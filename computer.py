class Computer:

    from typing import Dict, Optional

    # What attributes will it need?
    item_id : int
    new_price : int
    new_os : Optional[str]
    description: str
    operating_system: str
    year_made: int
    price: int

    # storing information about a specific computer
    # updating a computer's price
    # updating a computer's OS
    # refurbishing a computer


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, item_id : int, price : int, new_price : int, operating_system: str, year_made: int, new_os : Optional[str] = None):
        self.item_id = item_id
        self.price = price
        self.new_price = new_price
        self.new_os = new_os
        self.year_made = year_made
        self.operating_system = operating_system

    # What methods will you need?
        
    def update_price(item_id: int, price: int, new_price: int):
        if item_id > 0:
            new_price == price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def refurbish(item_id: int, year_made: int, price: int, operating_system: str, new_os: Optional[str] = None):
        if item_id > 0:
            if year_made < 2000:
                price == 0 # too old to sell, donation only
            elif year_made < 2012:
                price == 250 # heavily-discounted price on machines 10+ years old
            elif year_made < 2018:
                price == 550 # discounted price on machines 4-to-10 year old machines
            else:
                price == 1000 # recent stuff

            if new_os is not None:
                operating_system == new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

        

    def main():
        pass
    main()
    refurbish(12345, 2004, 1200, "MacOS", "Sierra")

        