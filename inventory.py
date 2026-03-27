from validaciones import *
import math

# validations
def sale():
    # name validation
    name = validacion_str("enter product name")
    
    # price validation
    price= validacion_float("enter product price")
        
    # quantity validation
    quantity= validacion_int("enter product quantit")

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
    name= validacion_str("enter product name")
    
    for dictionary in inventario:
        if dictionary["product"] == name:
            print(f"product: {dictionary["product"]} | " 
                f"precio: {dictionary["price"]}  |  "
                f"quantity: {dictionary["quantity"]}\n")    
            
    return None    

# actualizar producto
def actualizar_producto(inventario):
 
 # name validation
    name_update= validacion_str("Enter product name to update")
            
    # Buscar producto
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
                        price_new= validacion_float("enter new product price")
                        dictionary["price"] = price_new
    
                    
                    # editar cantidad
                    elif number ==2:
                        
                        # quantity validation
                        quantity_new = validacion_float("enter new product quantity")
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
        print("\nProducto no encontrado\n")
    
    
def eliminar_producto(inventario):
     # name validation
    name_delete = validacion_str("Enter product name to delete")
            
     # Buscar producto
    for dictionary in inventario:
        cont=1
        if dictionary["product"] == name_delete:
                cont=2
                inventario.remove(dictionary)
                print("\nProducto Eliminado\n")
                break
                
    
    if cont == 1:
        print("\nProducto no encontrado\n")
