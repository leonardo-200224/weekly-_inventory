
def summary(product_list):
    print("\nSUMMARY")
    if not product_list:
          print("There are no products stored")
    for dictionary in product_list:
         print(f"product: {dictionary["product"]} | " 
              f"precio: {dictionary["price"]}  |  "
              f"quantity: {dictionary["quantity"]}\n")
                