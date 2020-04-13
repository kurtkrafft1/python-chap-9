class Company:

    def __init__(self, name, industry, address):
        self.name = name 
        self.industry = industry
        self.address = address
        self.employees = list()
    
    def add_employee(self, employee):
        self.employees.append(employee)
    