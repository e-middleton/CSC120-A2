from computer import Computer
from typing import Dict


class ResaleShop():

    # What attributes will it need?
    inventory : Dict[int, Computer] = {}
    itemID: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory:dict = {}
        self.itemID = 0

    def buy(self, PC:Computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = PC

##when I want to add computer info into parameters, I have to say like, def name(self, myComputer: Computer)
    # What methods will you need?

    #am trying to print the inventory, it doesn't quite work though
    def output(self):
       if self.inventory:
        # For each item
        for self.itemID in self.inventory:
            # Print its details
            print(f'Item ID: {self.itemID} : {self.inventory[self.itemID]}')
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

main()