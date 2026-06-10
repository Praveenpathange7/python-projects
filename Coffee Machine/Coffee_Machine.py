# Coffee Machine

milk = 2000
water = 1000
coffee = 500
money = 0

def cal(cost):
    fiv = int(input("Enter how many 5rs coins : "))
    ten =  int(input("Enter how many 10rs coins : "))
    fif =  int(input("Enter how many 50rs coins : "))
    total = 5 * fiv + 10 * ten + 50 * fif
    if total < cost:
        print("Sorry, insufficient money. Money refunded.")
        return False

    change = total - cost
    print(f"{change}rs Here is your change")
    print("---- THANK YOU ----")
    return True

def working(option):
    global milk, water, coffee, money
    if option == 1:
        if milk >= 120 and  water >= 50 and coffee >= 50:
            if cal(180):
                milk -= 120
                water -= 50
                coffee -= 50
                money += 180
                print("Here is your Latte ☕ Enjoy!")
        else:
            print("There is no enough ingrediants to prepare Lattee")
    elif option == 2:
        if milk >= 180 and  water >= 50 and coffee >= 80:
            if cal(250):
                milk -= 180
                water -= 50
                coffee -= 80
                money += 250
                print("Here is your Cappuccino ☕ Enjoy!")
        else:
            print("There is no enough ingrediants to prepare Cappuccino")
    elif option == 3:
        if milk >= 100 and  water >= 30 and coffee >= 30:
           if cal(150):
                milk -= 100
                water -= 30
                coffee -= 30
                money += 150
                print("Here is your Espresso ☕ Enjoy!")
        else:
            print("There is no enough ingrediants to prepare espresso")
    

is_on = True
while is_on:
    print("---- Menu ----")
    print("1. Latte      - ₹180")
    print("2. Cappuccino - ₹250")
    print("3. Espresso   - ₹150")
    option = input ("Enter your choice : ")
    if option == 'report':
        print("\n---- REPORT ----")
        print(f"Milk   : {milk} ml")
        print(f"Water  : {water} ml")
        print(f"Coffee : {coffee} g")
        print(f"Money  : ₹{money}")
    elif option == 'off':
        is_on = False
    else:
        if option in ['1', '2', '3']:
            working(int(option))
        else:
            print("Invalid option")
