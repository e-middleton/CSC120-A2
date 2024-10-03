#creates a class Computer which holds all the stats about a computer in a shop
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


    #Constructor to create instances of class Computer
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int, 
                    ):
        
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system =  operating_system
        self.year_made = year_made
        self.price = price

