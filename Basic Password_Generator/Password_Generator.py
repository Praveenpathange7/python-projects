import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' , 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y' , 'z' , 'A' , 'B' , 'C' , 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4' , '5' , '6' , '7', '8' , '9' ]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
num_letter = int(input("How many number of letters you want in your password : "))
num_symbols = int(input("How many number of symbols you want in your password : "))
num_numbers = int(input("How many number of numbers you want in your password : "))

for i in range(1,num_letter+1):
    char = random.choice(letters)
    password+=char
for i in range(1,num_numbers+1):
    num = random.choice(numbers)
    password+=num
for i in range(1,num_symbols+1):
    sym = random.choice(symbols)
    password+=sym
random.shuffle(password)
for i in password:
    print(i,end='')
    
