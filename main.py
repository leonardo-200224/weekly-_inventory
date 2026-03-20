#importing functions
from inventory import sale
from summary import summary
from Calculate import calculate

#list that stores the dictionaries
all_sales=[]

#loop for menu validations
cont =1
while cont ==1:
    #menu creation and validation
    try:
        print("\nMENU")
        number= int(input(
            "1-Add product\n"
            "2-Show inventory\n"
            "3-calculate statistics\n"
            "4-go out\n"
            "Enter product number (1-4): "
        ))
        
        #Conditional statements validating the user's input
        if number<=0:
            print("You must enter a valid product (1-4)")
            continue
        
        if number ==1:
            all_sales.append(sale())
            continue
            
        elif number ==2:
            summary(all_sales)
            continue
        
        elif number ==3:
            calculate(all_sales)
            continue
        
        elif number ==4:
            cont =2
        else:
            print("You must enter a valid value (1-4)") 
            continue  
    #The error is detected and an error message is displayed.
    except ValueError:
        print("the value must be numeric (1-4)")
        continue



        
# ---------------------------------------------------------
# General program description
# This program allows the user to register a product in a
# simple inventory system. The user must enter the product
# name, price and quantity.
#
# The program validates the input data to ensure that:
# - The product name only contains letters.
# - The price is a positive number.
# - The quantity is a positive integer.
#
# After validating the data, the program calculates the
# total cost of the product (price * quantity) and stores
# the information in a dictionary inside a list.
#
# Finally, the program displays the product information
# and the calculated total cost in the console.
# ---------------------------------------------------------
