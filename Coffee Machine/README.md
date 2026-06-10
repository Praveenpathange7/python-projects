# ☕ Coffee Machine Simulator

A simple command-line Coffee Machine built using Python.

This project simulates a real coffee vending machine where users can:

* Select different coffee types
* Insert coins for payment
* Receive change
* Check available resources
* Turn off the machine
* Track machine earnings

## 🚀 Features

### Coffee Menu

| Coffee     | Price |
| ---------- | ----- |
| Latte      | ₹180  |
| Cappuccino | ₹250  |
| Espresso   | ₹150  |

### Resource Management

The machine keeps track of:

* Milk
* Water
* Coffee
* Money earned

### Payment System

Accepted coins:

* ₹5
* ₹10
* ₹50

The machine:

* Calculates the total amount inserted
* Verifies sufficient payment
* Returns change when necessary
* Refunds money if payment is insufficient

### Reports

Type:

```text
report
```

to view the current machine resources and earnings.

### Turn Off Machine

Type:

```text
off
```

to stop the coffee machine.

---

## 📂 Project Structure

```text
coffee_machine.py
README.md
```

---

## 🛠 Technologies Used

* Python 3
* Functions
* Loops
* Conditional Statements
* Global Variables
* User Input Handling

---

## 💻 Sample Usage

```text
---- Menu ----
1. Latte      - ₹180
2. Cappuccino - ₹250
3. Espresso   - ₹150

Enter your choice : 1

Enter how many 5rs coins : 2
Enter how many 10rs coins : 5
Enter how many 50rs coins : 3

20rs Here is your change
---- THANK YOU ----
Here is your Latte ☕ Enjoy!
```

---

## 📚 Concepts Practiced

This project helped me practice:

* Python Functions
* Return Values
* Loops
* Conditional Logic
* Input Validation
* Resource Tracking
* Simple Payment Processing
* Command-Line Applications

---

## 🎯 Future Improvements

* Add more coffee options
* Save reports to a file
* Create a GUI version using Tkinter
* Add unit tests

---

