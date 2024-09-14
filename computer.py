class Computer:
    #set up attributes for computer
    #attributes aren't initialized because there's no need for memory space yet
    #that happens in constructor
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    #itemID: int
    #add id in other places

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    #setting up my constructor to make new computers
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int, 
                    #itemID: int
                    ):
        
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system =  operating_system
        self.year_made = year_made
        self.price = price
    
    #how do I do this based on the itemID? like, how do I call this method based on the attribute itemID
    def update_price(self, new_price: int):
        self.price = new_price
        #I took out the clause where it checks if the itemID exists before it changes the price,
        # probs need to add that bad boy back in somehow

        #hopefully I can get this to work with resale shop to print the inventory
    def vomit(self):
        print("Description:", self.description)
        print("Processor type:", self.processor_type)
        print("Hard drive capacity:", self.hard_drive_capacity)
        print("Memory:", self.memory)
        print("Operating System:", self.operating_system)
        print("Year made:", self.year_made)
        print("Price:", self.price)


def main():

    my_computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    #print("Description", my_computer.description)

    #test
    #my_computer.update_price(69)
    #print()
    #print()
    #print(my_computer.price)



main()

    # What methods will you need?
    #should probably have a method to print the deets on a comp
