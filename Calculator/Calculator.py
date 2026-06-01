def calculator(a,o,b):
    if o =='+':
        s = a+b
        print(f"{a} + {b} = {s}")
        reiterate(s)
    elif o =='-':
        s = a-b
        print(f"{a} - {b} = {s}")
        reiterate(s)
    elif o =='*':
        s = a*b
        print(f"{a} * {b} = {s}")
        reiterate(s)
    elif o =='/':
        if b == 0:
            print("Can't divide by zero")
        else:
            s = a/b
            print(f"{a} / {b} = {s}")
            reiterate(s)
    else:
        print("Invalid operator")
    
def reiterate(s):
    print("Continue(y) | New(n) | Exit(x): ")
    sym = input("Enter the choice : ").lower()
    if sym == 'y':
        b = int(input("Enter the next number : "))
        o = input("Enter the operator : ")
        calculator(s,o,b)
    elif sym == 'n':
        a = int(input("Enter the first number : "))
        o = input("Enter the operator : \n+\n-\n*\n/\n")
        b = int(input("Enter the next number : "))
        calculator(a,o,b)
    elif sym == 'x':
        print('Ended Successfully')
        return
    else:
        print("Enter the valid input...")
        reiterate(s)

a = int(input("Enter the first number : "))
o = input("Enter the operator : \n+\n-\n*\n/\n")
b = int(input("Enter the next number : "))
calculator(a,o,b)
