import random

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")
num = random.randint(1,101)
attempt = 0
while True:
    guess = int(input("Enter your number : "))
    attempt+=1
    if guess>num:
        print("Too High!")
    elif guess<num:
        print("Too Low!")
    else:
        print("Correct!🎉🎉")
        print(f"You guessed {num} in {attempt} attempts")
        break
