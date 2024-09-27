products = {}
products_list= []

while True:
    print("=-="*15)
    print("SuperMarket")
    print("=-="*15)
    print("1 - Add to Stock")
    print("2 - View Stock")
    print("3 - Buy")
    print("4 - Exit")
    option = int(input("Enter the option you want: "))
    
    if option == 1: # add something in to the stock
        print("=-="*15)
        products['name'] = str(input("Name: "))
        products['price'] = float(input("Price: $"))
        products['amount'] = int(input("Amount: "))
        products_list.append(products["name"])
        products_list.append(products["price"])
        products_list.append(products["amount"])
        products.clear()
    elif option == 2: #View stock
        cont = 0
        size = len(products_list) / 3
        size = int(size)
        for p in range(size):
            print(f"Product: {products_list[cont]} | Price: ${products_list[cont+1]} | Amount: {products_list[cont+2]}")
            if cont <= size:
                cont += 3
            else:
                continue
        print("1 - Edit stock")
        print("2 - Return to menu")
        option = int(input("Enter the option you want: "))
        if option == 1: #Remove somethin in the stock option
            search_stock = str(input("Product name: "))
            if search_stock in products_list: #only if product is in the product list
                found = products_list.index(search_stock)
                print(f"Product: {products_list[found]} | Price: ${products_list[found+1]} | Amount:{products_list[found+2]}")
                print("=-="*15)
                print("1 - Remove Product")
                print("2 - Change Price")
                print("3 - Change Amount")
                product_option = int(input("What do you wanna change: "))
                if product_option == 1:
                    products_list.pop(found)
                    products_list.pop(found)
                    products_list.pop(found)
                elif product_option == 2:
                    new_price = float(input("New Price: $"))
                    products_list[found+1] = new_price
                elif product_option == 3:
                    new_amount = int(input("New Amount: "))
                    products_list[found+2] = new_amount
    
    elif option == 3: #Buy something that's in the stock
        search_stock = str(input("Product name: "))
        if search_stock in products_list: #only if product is in the product list
            found = products_list.index(search_stock)
            amount_wanted = int(input("Amount you want: "))

            if amount_wanted <= products_list[found+2]:
                total_pay = amount_wanted * products_list[found+1]
                print(f"Your total to pay is ${total_pay}")
                paying = float(input("Pay: "))

                if paying >= total_pay:
                    change = paying - total_pay
                    if change > 0:
                        print(f"Thank's for buying in our SuperMarket! Your change will be ${change}")
                        new_amount = products_list[found+2] - amount_wanted
                        products_list[found+2] =  new_amount
                    else:
                        print(f"Thank's for buying in our SuperMarket!")
                        new_amount = products_list[found+2] - amount_wanted
                        products_list[found+2] =  new_amount
                else:
                    print("Not enough money!")

            else:
                print("Amount wanted more than is in the stock!")
        
        else:
            print("Product not found!")
    
    elif option == 4:
        print("See you next time!")
        break
    else:
        print("Option not found! Try again!")
