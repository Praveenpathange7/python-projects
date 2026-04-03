# 🔐 Random Password Generator (Python)

## 📌 Description

This is a simple Python program that generates a **random password** based on user preferences.
The user can specify how many **letters, numbers, and symbols** they want in the password.

---

## ⚙️ Features

* Generates secure random passwords
* User-defined password composition:

  * Letters (uppercase + lowercase)
  * Numbers (0–9)
  * Symbols (!, #, $, %, etc.)
* Randomly shuffles characters for better security

---

## 🧠 How It Works

1. The program stores:
   * Letters (a–z, A–Z)
   * Numbers (0–9)
   * Symbols (!, #, $, etc.)
   * 
2. It asks the user:
   * Number of letters
   * Number of numbers
   * Number of symbols

3. It randomly selects characters from each category.

4. All characters are combined into a list.

5. The list is shuffled to make the password unpredictable.

6. Finally, the password is printed.

---

## ▶️ How to Run

1. Make sure Python is installed.
2. Copy the code into a `.py` file (e.g., `password_generator.py`)
3. Run the file:

   ```
   python password_generator.py
   ```
---

## 💡 Example

```
How many number of letters you want in your password : 4
How many number of symbols you want in your password : 2
How many number of numbers you want in your password : 2

Output: aB3#d7$K
```

---

## 🛠️ Code Highlights

* `random.choice()` → selects random characters
* `random.shuffle()` → mixes password characters
* Lists are used to store and build the password

---

## 📄 License

This project is free to use for learning purposes.
