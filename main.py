#importing functions
from inventory import sale
from summary import summary
from Calculate import calculate
from inventory import buscar_producto
from inventory import actualizar_producto
from inventory import eliminar_producto 
from archivos import guardar_csv, cargar_csv

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
            "3-buscar producto\n"
            "4-actualizar producto\n"
            "5-eliminar producto\n"
            "6-calculate statistics\n"
            "7-Guardar CSV\n"
            "8-Cargar CSV\n"
            "9-Exit\n"
            "Enter product number (1-4): "
        ))
        
        #Conditional statements validating the user's input
        if number<=0:
            print("You must enter a valid product (1-4)")
            continue
        # agregar producto
        if number ==1:
            all_sales.append(sale())
            continue
        
        # mostrar inventario resumen
        elif number ==2:
            summary(all_sales)
            continue
        
        # buscar producto
        elif number ==3:
            buscar_producto(all_sales)
            continue
        
        # actualizar producto
        elif number ==4:
            actualizar_producto(all_sales)
            continue
        
        # Eliminar producto
        elif number ==5:
            eliminar_producto(all_sales)
            continue
        
        # calculo de estadistica
        elif number ==6:
            calculate(all_sales)
            continue
        
        # cGuardar CSV
        elif number ==7:
            ruta = input("Ingrese ruta del archivo (ej: inventario.csv): ")
            guardar_csv(all_sales, ruta)
            continue
        
        # Cargar CSV
        elif number ==8:
            ruta = input("Ingrese ruta del archivo: ")
            nuevos_datos = cargar_csv(ruta)

            if nuevos_datos:
                opcion = input("¿Sobrescribir inventario actual? (si/no): ").upper()

                if opcion == "SI":
                    all_sales = nuevos_datos
                    print("\n Inventario reemplazado\n")

                elif opcion == "NO":
                    # fusionar
                    for nuevo in nuevos_datos:
                        encontrado = False

                        for actual in all_sales:
                            if actual["product"] == nuevo["product"]:
                                actual["quantity"] += nuevo["quantity"]
                                actual["price"] = nuevo["price"]
                                actual["total_cost"] = actual["price"] * actual["quantity"]
                                encontrado = True
                                break

                        if not encontrado:
                            all_sales.append(nuevo)

                    print("\n Inventario fusionado\n")

            continue
        
        elif number ==9:
            cont =2
        else:
            print("You must enter a valid value (1-4)") 
            continue  
        
    #The error is detected and an error message is displayed.
    except ValueError:
        print("the value must be numeric (1-4)")
        continue
