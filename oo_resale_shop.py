from computer import Computer
from typing import Dict


class ResaleShop():

    # Attributes
    inventory : Dict[int, Computer] = {}
    itemID: int
   
    #Constructor
    def __init__(self):
        self.inventory:dict = {}
        self.itemID = 0

    #PC is the name of my variable, of type Computer, so I can pass in the instance of the computer
    def buy(self, PC:Computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = PC

    #okay, current issue is arguments? Do I pass in the computer? I think I have to.
    #but then I don't use PC at all?
    def sell(self, PC:Computer):
        if self.itemID in self.inventory:
            del self.inventory[self.itemID]
            print("Item", self.itemID, "sold!")
        else: 
            print("Item", self.itemID, "not found. Please select another item to sell.")

    #prints out the inventory if it exists
    #Confused because now it's printing out : None at the end? Why?
    def output(self):
        if self.inventory:
        # For each item
            for self.itemID in self.inventory:
            # Print its details, using vomit() method from computer class
                print(f'Item ID: {self.itemID} : {self.inventory[self.itemID].vomit()}')
        else:
            print("No inventory to display.")

def main():
    my_computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    myShop = ResaleShop()
    myShop.buy(my_computer)
    myShop.output()

    print()
    print()
    print()

    myShop.sell(my_computer)
    myShop.output()

main()