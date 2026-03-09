initial = 0
rate = 0
time = 0
while initial <= 0:
    initial = float(input("Enter the initial amount: "))
    if initial <= 0:
        print("initial can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the rate (%): "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")

while time <= 0:
    time = float(input("Enter the time (in years): "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

total = initial * (1 + (rate * time) / 100)

print(f"Total amount after {time} years: ₹{round(total, 2)}")
print(f"Interest earned: ₹{round(total - initial, 2)}")
