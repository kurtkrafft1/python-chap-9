import datetime

class Building:
    
    def __init__(self, address, stories, name):
        self.address = address
        self.stories = stories
        self.name = name
    
    def construct(self, date= datetime.datetime.now()):
        self.date_constructed = date
        print(f"The {self.name} was built {self.date_constructed}")
        
    def purchase(self, new_owner):
        self.owner = new_owner
        print(f"The {self.name} was bought by {self.owner}")
