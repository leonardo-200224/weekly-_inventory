
# str
def validacion_str(mensaje):
    counter_name=1
    while counter_name ==1:
            # Request user data
            name = str(input(f"{mensaje}: ")).strip()
            if not name.isalpha():
                print("Symbols and Numbers are not allowed")
                continue
            
            counter_name +=2
            
    return name
    
    
# int 
def validacion_float(mensaje):
    counter_price=1
    while counter_price ==1:        
        try:
            # Request user data
            price = float(input(f"{mensaje}: "))
            if price <=0:
                print("ERRO: Enter a valid value")
                continue
        
            break
        except ValueError:
            print("Enter a valid value")
            continue
        
    return price

    
    
# float
def validacion_int(mensaje):
# quantity validation
    counter_quantity=1
    while counter_quantity ==1:  
        try:
            # Request user data
            quantity = int(input(f"{mensaje}: "))
            if quantity <=0:
                print("ERRO: Enter a valid value")
                continue
            break
        except ValueError:
            print("Enter a valid value")
            continue
        
    return quantity
