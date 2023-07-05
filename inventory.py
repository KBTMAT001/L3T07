

#========The beginning of the class==========
from tabulate import tabulate

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
    
        return f"{self.product},{self.cost},{self.quantity},{self.code},{self.country}"
        
#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

    try:                                    # Creating a try except block in case an inventory file isn't loaded
        fo = open("inventory.txt","r")
        for line in fo:
            lineOut = str(line).split(sep=",")
            if lineOut[0] =="Country":
                pass
            elif len(lineOut) <5:
                print("Insufficient details added for shoe!")
            else:
                shoe_list.append(Shoe(lineOut[0],lineOut[1],lineOut[2],lineOut[3],lineOut[4]))
        fo.close()
        return shoe_list
    
    except FileNotFoundError:
        print("The file does not exist")

def capture_shoes(shoe_list,inCountry,inProduct,inCode,inQuantity,inCost):
    
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    inCountry = "\n"+inCountry                                             # Needed to included a line space for when its rewritten to the text file
    shoe_list.append(Shoe(inCountry,inCode,inProduct,inCost,inQuantity))

    print(shoe_list[-1].product,"has been added")                           #Use negative indexing to print the shoe added
    

def view_all():
    
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

    shoe_table =[]
    for shoe in shoe_list:          
        shoe_table.append(shoe.__str__().split(","))

    print(tabulate(shoe_table,headers=["Product name","Cost","Quantity","Code","Country"]))


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    minList = []
    minList.append(shoe_list[0])                          # initialising as a list as may be more than one shoe at the lowest value
    
    for item in shoe_list: 
        try:
            if int(item.quantity) < int(minList[0].quantity):
                minList = []                                        # Reinitialising the variable to remove all shoes in the list
                minList.append(item)
            elif int(item.quantity) == int(minList[0].quantity):
                minList = []
                minList.append(item)
        except ValueError:
    
            print("The input was not a valid integer.")


    for orderItem in minList:                                       # Getting input from user and updating the minimum list
        print(f"\n{orderItem.product} has: {(orderItem.quantity).rstrip()} remaining.")
        noUpdate = int(input("How many would you like to order: "))
        orderItem.quantity = int(orderItem.quantity) + noUpdate
    
    for orderItem in minList:                       # Updating the full inventory list
        for shoe in shoe_list:
            if orderItem.code == shoe.code:
                shoe.quantity = str(orderItem.quantity)+"\n"
    

def search_shoe(findCode):
    
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    for item in shoe_list:
        print(f"{item.code},{findCode}")
        if findCode == item.code:
            table = []
            table.append(item.__str__().split(","))
            return tabulate(table,headers=["Product name","Cost","Quantity","Code","Country"])
        
    return "Not found"

def value_per_item():

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    
    value_list = []

    for item in shoe_list:
        value_list.append([item.product,item.code,str(int(item.quantity)*int(item.cost))])
    
    print(tabulate(value_list,headers=["Product name","Code","Shoe Value (ZAR)"]))

def highest_qty():

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    maxList = []
    maxList.append(shoe_list[0])                          # initialising as a list as may be more than one shoe at the lowest value
    
    for item in shoe_list: 
        try:
            if int(item.quantity) > int(maxList[0].quantity):
                maxList = []                                        # Reinitialising the variable to remove all shoes in the list
                maxList.append(item)
            elif int(item.quantity) == int(maxList[0].quantity):
                maxList = []
                maxList.append(item)
        except ValueError:
    
            print("The input was not a valid integer.")
    
    return print(maxList[0].product,"is for sale!")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
read_shoes_data()

while True:

    menu = input('''\nWelcome to the inventory system. Please indicate your selection:
    c - capture a new shoe
    va - view all the shoes
    rs - restock
    s - search for a shoe
    v - see stock value
    h - highest stock for sale!
    e - exit the programme

    ''')

    if menu == "c":
        inCountry = input("Country of origin:   ")
        inProduct = input("Shoe name:   ")
        inCode = input("Product code:   ")
        inQuantity = input("Quantity of shoe:   ")
        inCost = input("Cost of shoe:   ")

        capture_shoes(shoe_list,inCountry,inProduct,inCode,inQuantity,inCost)

    elif menu == "va":
        view_all()
    
    elif menu == "rs":
        re_stock()
    
    elif menu == "s":
        searchCode = input("Please provide product code to be searched: ")
        print("\n"+ search_shoe(searchCode))
    
    elif menu == "v":
        value_per_item()
    
    elif menu == "h":
        highest_qty()
    
    elif menu == "e":
        fo = open("inventory.txt","w+")                             #Rewriting the text file only upon exit. All changes are held in the shoe list up until then

        fo.write("Country,Code,Product,Cost,Quantity\n")
    
        for shoe in shoe_list:

            fo.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
    
        fo.close()

        print("See you next time!")
        exit()
    
    else:
        print("Wrong choice")
