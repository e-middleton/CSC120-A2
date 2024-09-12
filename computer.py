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
                    price: int):
        
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system =  operating_system
        self.year_made = year_made
        self.price = price
        
        
    # You'll remove this when you fill out your constructor

def main():

    my_computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    print("Description", my_computer.description)




main()

    # What methods will you need?
    #should probably have a method to print the deets on a comp
