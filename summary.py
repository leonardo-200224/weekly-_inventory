
# final summary of products
def summary(product_list):
    print("\nSUMMARY")
    # validation that the list is not empty
    if not product_list:
          print("\n-----There are no products stored-----\n")
    else:
            
        #It goes through all the products on the list
        for dictionary in product_list:
            
            #The product, price, and quantity of each sale are displayed.
            print(f"product: {dictionary["product"]} | " 
                f"precio: {dictionary["price"]}  |  "
                f"quantity: {dictionary["quantity"]}\n")
                    