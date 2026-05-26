# Caesar Cipher 🔐

A simple Python program that encrypts and decrypts text using the Caesar Cipher technique.

---

## 📖 Description

This project is a beginner-friendly implementation of the classic Caesar Cipher encryption algorithm.
The program allows users to:
- Encrypt text by shifting letters forward
- Decrypt text by shifting letters backward
- Choose a custom shift value
- Repeat the process until they decide to exit

---

## ✨ Features

- Supports lowercase alphabet letters
- Keeps spaces, numbers, and symbols unchanged
- Interactive command-line interface
- Beginner-friendly Python project
- Uses ASCII conversion with `ord()` and `chr()`

---

## 🧠 How Caesar Cipher Works

Each letter in the text is shifted by a fixed number of positions in the alphabet.

Encryption formula:  
    Encrypted Letter = (Plain Letter + Shift Key) mod 26

Decryption formula:  
    Decrypted Letter = (Encrypted Letter - Shift Key) mod 26

Example with shift `3`:

```text
Plain Text : hello
Encrypted : khoor
```

---

## 💻 Example Usage

```text
Type 'encrypt' for encryption, type 'decrypt' for decryption: encrypt
Number of Shifts: 3
Enter the text: hello world

Encrypted: khoor zruog
```

---

## 📚 Concepts Used

- Python Functions
- Loops
- Conditional Statements
- String Manipulation
- ASCII Conversion (`ord()` and `chr()`)
- Modulo Arithmetic

---

## 🎯 Future Improvements

- Support uppercase letters
- Add brute-force decrypt mode
---

## 📜 License

This project is open-source and free to use.
