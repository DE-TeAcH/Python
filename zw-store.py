def menu():
    print("                              ZW Store  ") 
    print("Hello dear costumer, How Can I help you today : ")
    print("1 - Display All Items.")
    print("2 - Add An Item to The Item's Menu.")
    print("3 - Add An Item to Cart.")
    print("4 - Remove An Item from Cart.")
    print("5 - Display Cart's Item.")
    print("6 - Confirm Buyig.")
    print("7 - Quit Menu.")
def display(x,y):
    i = 0
    while i < len(x) :
        print(f"Item {i + 1 }:       The phone: {x[i]}       It's price: {y[i]}")
        i = i + 1
    i = 0
def add_item():
    item_add_name = input("Enter The name of the Item we'll sell instead of You: ")
    item_add_price = input("Enter The price of the Item: ")
    item_add_stock = input("Enter How many Item you're putting on sales: ")
    item.append(item_add_name)
    price.append(int(item_add_price))
    stock.append(int(item_add_stock))
item = ['iPhone XR','iPhone XS','iPhone 13' ]
price = [300,350,650]
stock = [2,5,23]
purshased = []
price_pur = []
num_pur=[]
tot = 0
i = 0
while True:
    print()
    menu()
    choice = input("Please enter your choice: ")
    if choice == '1':
        display(item,price)
    elif choice == '2':
        add_item()
    elif choice == '3':
        display(item,price)
        print()
        buy = input ("Enter the Item index: ")
        num_buy = input("How many phone you want to get: ")
        buy_ind = int(buy)
        while i < len(item) :
            if i + 1 == buy_ind:
                if stock[i]-int(num_buy) >= 0:
                    purshased.append(item[i])
                    price_pur.append(price[i])
                    num_pur.append(num_buy)
                    tot = tot + price[i]*int(num_buy)
                    stock[i] = stock[i] - int(num_buy)
                    print("Item added succesfully.")
                else :
                    print(f"Sorry, The number of phone you choosed is out of stock, there's only {stock[i]}")
                break
            i = i + 1
        i = 0
    elif choice == '4':
        print(f"Cart Items:")
        display(purshased,num_pur)
        print(f"The total is: {tot}")
        print()
        cancel = input ("Enter the index of the Item you want to remove: ")
        num_cancel = input("How many phone you want to remove from cart: ")
        cancel_ind = int(cancel)
        while i < len(purshased) :
            if i + 1 == cancel_ind:
                if int(num_pur[i])-int(num_cancel) > 0:
                    num_pur[i] = int(num_pur[i])-int(num_cancel)
                    tot = tot - price_pur[i]*int(num_cancel)
                    print("Item removed succesfully.")
                elif int(num_pur[i])-int(num_cancel) == 0:
                    purshased.remove(purshased[i])
                    num_pur.remove(num_pur[i])
                    tot = tot - price_pur[i]*int(num_cancel)
                    print("Item removed succesfully.")
                else :
                    print(f"Sorry, The number of phone you choosed is more than you ordered [{num_pur[i]}].")
                break
            i = i + 1
        i = 0
    elif choice == '5':
        print(f"Cart Items:")
        display(purshased,num_pur)
        print(f"The total is: {tot}")
    elif choice == '6':
        print(f"Phones bought :")
        display(purshased,num_pur)
        print(f"The total is: {tot}")
        con = input("Type Y to confirm this purchase process or N to not confirm: ")
        con = con.upper()
        if con == 'Y':
            print()
            print("Thnx dear costumer, Wish you a great day!")
            break
        elif con == 'N':
            print()
            print("You decline the purshase!")
        else :
            print()
            print("Invalid Input")
        i = 0
    elif choice == '7':
        print("Bye costumer, See you in another day!")
        break
    else :
        print("Invalid Input")