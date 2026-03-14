import math
all_sales = []
#validations
def sale():
    # name validation
    counter_name=1
    while counter_name ==1:
            # Request user data
            name = str(input("enter product name: "))
            if not name.isalpha():
                print("Symbols and Numbers are not allowed")
                continue
            
            counter_name +=2
    
    # price validation
    counter_price=1
    while counter_price ==1:        
        try:
            # Request user data
            price = float(input("enter product price: "))
            if price <=0:
                print("ERRO: Enter a valid value")
                continue
        
            break
        except ValueError:
            print("Enter a valid value")
            continue
        

    # quantity validation
    counter_quantity=1
    while counter_quantity ==1:  
        try:
            # Request user data
            quantity = int(input("enter product quantity: "))
            if quantity <=0:
                print("ERRO: Enter a valid value")
                continue
            break
        except ValueError:
            print("Enter a valid value")
            continue

    #data storage library
    sales ={ 
        "product"   : name,
        "price"     :price,
        "quantity"  : quantity,
        "total_cost":price * quantity
        
    }
    
    return sales

# Mostrar resultados en consola
all_sales.append(sale())
print("\nResult\n")
print(
    f"Product: {all_sales[0]['product']}\n"
    f"price: {math.trunc(all_sales[0]['price'])}\n"
    f"Quantity: {all_sales[0]['quantity']}\n"
    f"Total cost: {math.trunc(all_sales[0]['total_cost'])}\n"
        )

        
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