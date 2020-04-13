from pizza import Pizza
from urban import Building
from employee import Employee
from companies import Company
from city import City


#WONT WORK__ALTERED OG MODEL TO GIVE USER ABILITY TO BUILD OWN ###########################
# meat_lovers = Pizza("Deep dish", "Red", "16 in", "anchovies", "pineapple")
# meat_lovers.add_topping("Pepperoni", "Olives")
# meat_lovers.what_did_I_order_again()

############## THIS WILL WORK #############
# create your own pizza
# create = Pizza()
# create.what_did_I_order_again()

# create.add_topping()


###################### URBAN AND BUILDINGS #########################
batman_building = Building("100 Broadway ave", 90, "Batman Building")
batman_building.designer = "Kurt Krafft"
batman_building.purchase('Kurt Realities')
batman_building.construct()

walgreens = Building('123 Main Street' , 1, "Walgreens on Main")
walgreens.designer = "God"
walgreens.purchase('Dwayne Industries')
walgreens.construct()

building_3 = Building("2629 Pennington Lane", 30, "Random House owned by the waitch")
building_3.designer = "Kurt"
building_3.purchase('Kurt Realities')
building_3.construct()

White_House = Building("2020 Pennsylvania ave", 3, "White House")
White_House.designer = "George Washington Smith"
White_House.purchase('Kurt Realities')
White_House.construct(date="July 4th 1776")

home = Building("910 Shelby Ave", 2, "Home")
home.designer = "Sir Patrick Stewart"
home.purchase("Renu Management")
home.construct()

# city = [batman_building, walgreens, building_3, White_House, home]
# print("___________________")
# for building in city:
#     print(f"The {building.name} is owned by {building.owner} and was built {building.date_constructed} and designed by {building.designer}. You can find it at {building.address}.")
#     print("___________________")

nashville = City("Nashville", "Kurt Krafft", 1993)
nashville.add_building(batman_building)
nashville.add_building(walgreens)
nashville.add_building(building_3)
nashville.add_building(White_House)
nashville.add_building(home)

def declare_city(city):
    print(f"Here are all the buildings in {city.name}")
    for building in city.buildings:
        print(f"the {building.name} is in {city.name} and located at {building.address}")

declare_city(nashville)


############################ Comapnies and Employees ####################

# bill = Employee("Bill Burr", "Mob-Boss", "12/12/2012")
# sally = Employee("Sally Sotha", "Hitman", "04/01/2020")
# ivan = Employee("Ivan the Terrible", "Common Gangster", "01/01/1863")

# jim = Employee("Jim Halpert", "Salesman", "03/12/2001")
# michael = Employee("Michael Scott", "Regional Manager", "10/23/1995")

# russian_mafia = Company('Mafia', 'Mean-Muggin and Thuggin', '6969 Chzecvholska Ave')
# dunder_mifflin = Company("Dunder Mifflin", 'Paper Supply', '32 Scranton Way')

# russian_mafia.add_employee(bill)
# russian_mafia.add_employee(sally)
# russian_mafia.add_employee(ivan)


# dunder_mifflin.add_employee(jim)
# dunder_mifflin.add_employee(michael)

# companies = [russian_mafia, dunder_mifflin]

# for comp in companies:
#     print(f"---{comp.name}---")
#     print(f"a {comp.industry} company located at {comp.address}")
#     for people in comp.employees:
#         print(f"{people.name} is a {people.title} here and has been here since {people.date_started}")
    
#     print("_______")

