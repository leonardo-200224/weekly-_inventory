
def sale():
    # name validation
    counter_name=1
    while counter_name ==1:
        try:
            name = str(input("enter product name: "))
            if not name.isalpha():
                print("Symbols and Numbers are not allowed")
                continue
            break
        
        except ValueError:
            print("Enter a valid value")
            continue
            
    counter_name +=2
    
    # price validation
    counter_price=1
    while counter_price ==1:        
        try:
            price = float(input("enter product price: "))
        
            break
        except ValueError:
            print("Enter a valid value")
            continue
        
    counter_price +=2    
       
    # quantity validation
    counter_quantity=1
    while counter_quantity ==1:  
        try:
            quantity = int(input("enter product quantity: "))
            break
        except ValueError:
            print("Enter a valid value")
            continue
        
    counter_quantity +=2
    
    sales ={ 
        "product" : name,
        "price"   :price,
        "quantity": quantity
        
    }
    
    return sales

venta=sale()
print(venta)
        