# 🔍 Single Number Finder (Python)

## 📌 Description

This Python program finds the **unique element** in a list where every other element appears exactly **twice**.

---

## ⚙️ Features

* Accepts user input as a list of numbers
* Identifies the element that appears only once
* Uses sorting for efficient comparison
* Simple and beginner-friendly logic

---

## 🧠 How It Works

1. The input list is **sorted**.
2. The program checks elements in pairs:

   * Since duplicate numbers appear together after sorting,
   * It compares `nums[i]` with `nums[i+1]`.
3. If a mismatch is found:

   * That element is the **unique number**.
4. If no mismatch occurs in the loop:

   * The first element is returned as the unique number.

---

## ▶️ How to Run

1. Ensure Python is installed.
2. Save the code in a file (e.g., `single_number.py`)
3. Run the program:

   ```
   python single_number.py
   ```

---

## 💡 Example

```
Enter the number: 2 2 1 4 4
Output: 1
```

---

## 🛠️ Code Highlights

* `nums.sort()` → sorts the list
* `range(0, len(nums)-1, 2)` → checks elements in pairs
* Efficient comparison of adjacent elements

---

## ⚠️ Important Notes

* The program assumes:

  * Every element appears **twice except one**
* If input does not follow this rule, the result may be incorrect

---

## 📄 License

This project is free to use for learning purposes.
