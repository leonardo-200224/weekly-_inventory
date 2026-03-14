#validations
def sale():
    # name validation
    counter_name=1
    while counter_name ==1:
            name = str(input("enter product name: "))
            if not name.isalpha():
                print("Symbols and Numbers are not allowed")
                continue
            
            counter_name +=2
    
    # price validation
    counter_price=1
    while counter_price ==1:        
        try:
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
            quantity = int(input("enter product quantity: "))
            if quantity <=0:
                 print("ERRO: Enter a valid value")
                 continue
            break
        except ValueError:
            print("Enter a valid value")
            continue

    
    sales ={ 
        "product"   : name,
        "price"     :price,
        "quantity"  : quantity,
        "total_cost":price * quantity
        
    }
    
    return sales
        
print(sale())