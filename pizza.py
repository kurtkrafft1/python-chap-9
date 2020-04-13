class Pizza:
    def __init__(self):
        self.crust = input("What kind of crust would you like?")
        self.sauce = input("What kind of sauce would you like?")
        self.size = input("What size would you like? ")
        self.topping1 = input("Please choose a topping: ")
        self.topping2 = input("Please choose a topping: ")
        self.toppings = [self.topping1, self.topping2]


    def add_topping(self):
        newTopping = input("What topping would you like?")
        self.toppings.append(newTopping)
        q = input("Would you like to add another topping?")
        if q.lower() == "yes":
            self.add_topping()
        else:
            self.what_did_I_order_again()
           
    
    def what_did_I_order_again(self):
        string = ",".join(self.toppings)
        print(f'looks like you ordered a {self.size} size pizza , {self.crust} crust with {string} and {self.sauce} style sauce')
    
