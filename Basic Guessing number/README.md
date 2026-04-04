# 🎮 Number Guessing Game

A simple Python command-line game where the player tries to guess a randomly generated number.

---

## 📌 Description

This game generates a random number between **1 and 100**, and the user has to guess it.
After each guess, the program gives hints:

* 📉 "Too Low!" if the guess is smaller
* 📈 "Too High!" if the guess is larger

The game continues until the correct number is guessed.

---

## 🚀 Features

* Random number generation using Python
* Continuous guessing using a loop
* Hint system (Too High / Too Low)
* Tracks number of attempts
* Simple and beginner-friendly logic

---

## 🧠 Concepts Used

* `while` loop
* `if-elif-else` conditions
* `break` statement
* Variables and counters
* `random` module
* User input handling

---

## ▶️ How to Run

1. Make sure Python is installed
2. Clone this repository:

   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   ```
3. Navigate to the folder:

   ```bash
   cd number-guessing-game
   ```
4. Run the program:

   ```bash
   python game.py
   ```

---

## 🖥️ Sample Output

```
Welcome to the Number Guessing Game!
Guess a number between 1 and 100

Enter your number : 50
Too Low!

Enter your number : 75
Too High!

Enter your number : 63
Correct! 🎉🎉
You guessed 63 in 3 attempts
```
