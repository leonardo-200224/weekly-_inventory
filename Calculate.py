
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
            # total cost per product
            total_units += dictionary["quantity"]
            
        # Units and total sold are shown.
        print("\nCalculate")
        print(f"total_units: {total_units}\n"
            f"total_sold: {total_sold}")
