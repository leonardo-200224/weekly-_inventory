
# function to calculate
def calculate(product_list):
    # validation that the list is not empty
    if not product_list:
        print("\n-----There are no products stored-----\n")
    else:
        # Variables are created for the total and units sold
        total_sold =0
        total_units =0
        
        # The products on the list are reviewed.
        for dictionary in product_list:
            # total cost per product
            total_sold += dictionary["total_cost"]
            for dictionary2 in product_list:
                if dictionary["price"] > dictionary2["price"]:
                    mas_name= dictionary["product"]
                    mas_price= dictionary["price"]

            # total cost per product
            total_units += dictionary["quantity"]
            for dictionary2 in product_list:
                if dictionary["quantity"] > dictionary2["quantity"]:
                    mas_name_quantity = dictionary["product"]
                    mas_quantity= dictionary["price"]

        # Units and total sold are shown.
        print("\nCalculate")
        print(f"total_units: {total_units}\n"
            f"total_sold: {total_sold}\n"
            f"producto_mas_caro: {mas_name} | {mas_price}\n"
            f"producto_mayor_stock : {mas_name_quantity} | {mas_quantity}")
