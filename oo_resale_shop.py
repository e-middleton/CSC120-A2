#note to self, collaborated with Daniel Middleton to debug my itemID issue

from computer import Computer
from typing import Dict, Optional

#creates a class ResaleShop that is able to buy, sell, refurbish computers from it's inventory
class ResaleShop():
    # Attributes
    inventory : list[Computer] = []
   
    #Constructor
    def __init__(self):
        self.inventory:list = []

    #PC is the name of my variable, of type Computer, so I can pass in the specific instance
    def buy(self, PC:Computer):
        self.inventory.append(PC) #.append to add it into the list inventory


    def sell(self, PC:Computer):
        for i in range(len(self.inventory)): #checking if the computer exists in the inventory
            if self.inventory[i] == PC:
                self.inventory.remove(PC) #removes the computer from the list
                print("Computer sold!")
            else: 
                print("Computer not found. Please select another item to sell.")

    #had to import Optional so this works
    def refurbish(self, PC:Computer, new_os: Optional[str] = None):
        if self.inventory: #if our inventory exists
            for i in range(len(self.inventory)): #iterate through the indices
                if self.inventory[i] == PC: 
                #if computer in self.inventory:
                    PC = self.inventory[i] # locate the computer, ???WHAT does this do?
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
                    print("Item not found. Please select another item to refurbish.")
        
            else:
                print("No inventory to refurbish")

    #Updates the price of a computer in the inventory, if you pass in the computer and the new price
    def update_price(self, PC: Computer, new_price: int):
        if PC in self.inventory: #checking if the computer exists in the inventory
            PC.price = new_price
        else:
            print("Item not found. Cannot update price.")


    #prints out the inventory if it exists
    def output(self):
        if len(self.inventory) != False:
        # For each item
            for i in range(len(self.inventory)): #for an item in the list
            # Print its details, calling each individual attribute from Computer
                print(f'Item ID: {i} : Description: {self.inventory[i].description}\n'
                      f'Processor Type: {self.inventory[i].processor_type}\n'
                      f'Hard Drive Capacity: {self.inventory[i].hard_drive_capacity}\n'
                      f'Memory: {self.inventory[i].memory}\n'
                      f'Operating System: {self.inventory[i].operating_system}\n'
                      f'Year made: {self.inventory[i].year_made}\n'
                      f'Price: {self.inventory[i].price}\n'
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
    #print()

    #myShop.sell(testComputer)
    myShop.update_price(testComputer, 69)

    myShop.sell(testComputer)
    myShop.output()


   
    
if __name__ == "__main__":
    main()