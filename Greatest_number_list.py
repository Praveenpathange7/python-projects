lis = list(map(int,input("Enter the numbers : ").split(' ')))
if len(lis) == 0:
    print("List is empty")
else:
    maximum = lis[0]
    for i in lis:
     if i > maximum :
        maximum  = i
    print(maximum)