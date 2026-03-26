import math

# validations
def sale():
    # name validation
    counter_name=1
    while counter_name ==1:
            # Request user data
            name = str(input("enter product name: ")).strip()
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

    # data storage library
    sales ={ 
        "product"   : name,
        "price"     :price,
        "quantity"  : quantity,
        "total_cost":price * quantity
        
    }
    # the created dictionary is returned
    return sales


# buscar producto ingresado por el usuario
def buscar_producto(inventario):
    
    # name validation
    counter_name=1
    while counter_name ==1:
            # Request user data
            name = str(input("enter product name: ")).strip()
            if not name.isalpha():
                print("Symbols and Numbers are not allowed")
                continue
            
            counter_name +=2
            
    for dictionary in inventario:
        if dictionary["product"] == name:
            print(f"product: {dictionary["product"]} | " 
                f"precio: {dictionary["price"]}  |  "
                f"quantity: {dictionary["quantity"]}\n")    
            
    return None    

def actualizar_producto(inventario):
 
 # name validation
    counter_name=1
    while counter_name ==1:
            # Request user data
            name_update = str(input("Enter product name to update : ")).strip()
            if not name_update.isalpha():
                print("Symbols and Numbers are not allowed")
                continue
            
            counter_name +=2
            
    # mostrar producto
    for dictionary in inventario:
        cont=1
        if dictionary["product"] == name_update:
                cont=2
                #menu creation and validation
                try:
                    print(f"\n que valor quiere editar del producto: {name_update}")
                    number= int(input(
                        "1-price\n"
                        "2-quantity\n"
                    ))
                    
                    #Conditional statements validating the user's input
                    if number<=0:
                        print("You must enter a valid product (1-4)")
                        continue
                    
                    # editar precio
                    if number ==1:
                        
                        # price validation
                        counter_price=1
                        while counter_price ==1:        
                            try:
                                # Request user data
                                price_new = float(input("enter new product price: "))
                                if price_new <=0:
                                    print("ERRO: Enter a valid value")
                                    continue
                            
                                break
                            except ValueError:
                                print("Enter a valid value")
                                continue
                        dictionary["price"] = price_new
    
                    
                    # editar cantidad
                    elif number ==2:
                        
                        # quantity validation
                        counter_quantity=1
                        while counter_quantity ==1:  
                            try:
                                # Request user data
                                quantity_new = int(input("enter new product quantity: "))
                                if quantity_new <=0:
                                    print("ERRO: Enter a valid value")
                                    continue
                                break
                            except ValueError:
                                print("Enter a valid value")
                                continue
                        dictionary["quantity"] = quantity_new
                
                    else:
                        print("You must enter a valid value (1-2)") 
                        continue  
                #The error is detected and an error message is displayed.
                except ValueError:
                    print("the value must be numeric (1-2)")
                    continue
                break
    
    if cont == 1:
        print("Producto no encontrado")
