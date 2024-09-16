#note to self, collaborated with Daniel Middleton to debug my itemID issue

from computer import Computer
from typing import Dict, Optional

#creates a class ResaleShop that is able to buy, sell, refurbish computers from it's inventory
class ResaleShop():
    # Attributes
    inventory : Dict[int, Computer] = {}
    itemID: int
   
    #Constructor
    def __init__(self):
        self.inventory:dict = {}
        self.itemID = 0

    #PC is the name of my variable, of type Computer, so I can pass in the specific instance
    def buy(self, PC:Computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = PC

    #but then I don't use PC at all?
    #okay, trying this to try fix the error message?
    def sell(self, PC:Computer):
        if self.inventory[self.itemID] == PC:
        #if self.itemID in self.inventory:
            del self.inventory[self.itemID]
            print("Item", self.itemID, "sold!")
        else: 
            print("Item", self.itemID, "not found. Please select another item to sell.")

    #had to import Optional so this works
    #okay, some people were talking about updating os as a dif method? Like by itself
    #I have that bundled into refurbish, should I have it sep in computer class?
    def refurbish(self, PC:Computer, new_os: Optional[str] = None):
        if self.inventory:
            if self.inventory[self.itemID] == PC:
            #if self.itemID in self.inventory:
                PC = self.inventory[self.itemID] # locate the computer
                if int(PC.year_made) < 2000:
                    PC.price = 0 # too old to sell, donation only
                elif int(PC.year_made) < 2012:
                    PC.price = 250 # heavily-discounted price on machines 10+ years old
                elif int(PC.year_made) < 2018:
                    PC.price = 550 # discounted price on machines 4-to-10 year old machines
                else:
                    PC.price = 1000 # recent stuff

                if new_os is not None:
                    PC.operating_system = new_os # update details after installing new OS
            else:
                print("Item", self.itemID, "not found. Please select another item to refurbish.")
        
        else:
            print("No inventory to refurbish")

    #Updates the price of a computer in the inventory, if you pass in the computer and the new price
    def update_price(self, PC: Computer, new_price: int):
        if self.inventory[self.itemID] == PC:
            self.inventory[self.itemID].price = new_price
        else:
            print("Item", self.itemID, "not found. Cannot update price.")


    #prints out the inventory if it exists
    def output(self):
        if self.inventory != False:
        # For each item
            for self.itemID in self.inventory:
            # Print its details, calling each individual attribute from Computer
            #I couldn't figure out a cleaner way :(
                print(f'Item ID: {self.itemID} : Description: {self.inventory[self.itemID].description}\n'
                      f'Processor Type: {self.inventory[self.itemID].processor_type}\n'
                      f'Hard Drive Capacity: {self.inventory[self.itemID].hard_drive_capacity}\n'
                      f'Memory: {self.inventory[self.itemID].memory}\n'
                      f'Operating System: {self.inventory[self.itemID].operating_system}\n'
                      f'Year made: {self.inventory[self.itemID].year_made}\n'
                      f'Price: {self.inventory[self.itemID].price}\n'
                      )
        else:
            print("No inventory to display.")

def main():
    my_computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    testComputer:Computer = Computer(
        "Dell (early 1600s)",
        "3.5 GHc 6-Core Intel Xeon E5",
        5402, 32,
        "Windows", 1602, 5
    )

    #creates the first instance/initializes of my class ResaleShop so I can 
    myShop = ResaleShop()
    #myShop.buy(my_computer)
    myShop.buy(testComputer)
    #myShop.output()

   
    #myShop.output()
    #print()

    #myShop.sell(testComputer)
    #good, error message for sell works
    
    myShop.output()
    #good, error message for referbish works
   
    
if __name__ == "__main__":
    main()