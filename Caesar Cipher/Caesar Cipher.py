def Encript(Choice):
    shift_key = int(input("Number of Shifts : "))
    text = input("Enter the text : ")
    x = []
    if Choice == 'encrypt':
        for i in text:
            if i.isalpha():
                i = chr(((ord(i) - ord('a') + shift_key) % 26) + ord('a'))
            x.append(i)
        print(f"Encrpted : {''.join(x)}")
    else:
        for i in text:
            if i.isalpha():
                i = chr(((ord(i) - ord('a') - shift_key) % 26) + ord('a'))
            x.append(i)
        print(f"Decrpted : {''.join(x)}")
    
while True:
    Choice = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:").lower()
    if Choice not in ['encrypt', 'decrypt']:
        print("Invalid input")
        continue
    Encript(Choice) 

    end = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower() 
    if end != 'yes':
       print("Thank you!")
       break
