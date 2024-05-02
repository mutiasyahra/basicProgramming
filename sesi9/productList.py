#create empty products
products = []
while(True):
    #menu
    print("Choosen the menu: ")
    print("1. List the product")
    print("2. add a product")
    print("3. remove a product by name")
    print("4. remove a product by index")
    print("5. exit")
    #ask to input the menu
    choosen_menu = input("Please input menu: ")
    
    if choosen_menu == "1":
        print("List the product:")
        for i, p in enumerate(products, start=1):
            print(f"{i}. {p}")
    
    elif choosen_menu == "2":
        name_products = input("add a product: ")
        products.append(name_products)
        print("Product added successfully!")
    
    elif choosen_menu == "3":
        name_products = input("Enter the name of the product you want to delete: ")
        if name_products in products:
            products.remove(name_products)
            print("Product successfully deleted!")
        else:
            print("Product not found!")
    
    elif choosen_menu == "4":
        no_products = int(input("Enter the product number that you want to delete: "))
        if no_products <= len(products):
            del products[no_products - 1]
            print("Product successfully deleted!")
        else:
            print("Invalid product number!")
    
    elif choosen_menu == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid menu!")