# 📝 Tkinter Account Control App

A simple **Account Management Application** built with Python and Tkinter.  
This project allows users to **create, login, and delete accounts** with password hashing and password show/hide functionality.

---

## ⚡ Features

- **🔐 Account Creation**
  - Users can create accounts with **Name, Surname, Username, and Password**.
  - Passwords are securely hashed using `hashlib.sha256`.

- **🔑 Login System**
  - Login using **Username and Password**.
  - Validates credentials against the stored hashed passwords.
  - Displays login status with **informative messages**.

- **🗑 Account Deletion**
  - Delete an account using **Username and Password**.
  - Shows a **confirmation dialog** before deletion using `tkinter.messagebox`.

- **💻 User-friendly GUI**
  - Built entirely with **Tkinter**.
  - Responsive buttons and labels with clear layout.
  - Input validation and informative message boxes.

- **🛡 Security**
  - Passwords are stored as **SHA-256 hashes**, not plaintext.
  - SQL injection risk minimized with parameterized queries.

- **🏠 Window Navigation**
  - Seamless transition between **Login Page** and **Sign Up Page**.
  - Prevents window resizing for consistent design.
- ## 📸 Screenshots
- <div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
  <img alt="loginpage.png" src="https://github.com/yusuf-tufan/AccountSQLite/blob/master/screenshots/loginpage.png?raw=true" data-hpc="true" weight=500 height=300 class="Box-sc-g0xbh4-0 fzFXnm">
  <img src="https://github.com/yusuf-tufan/AccountSQLite/blob/master/screenshots/signuppage.png?raw=true" alt="Sign Up Page"  weight=500 height=300 border-radius: 5px;">
  <img alt="loginresult.png" src="https://github.com/yusuf-tufan/AccountSQLite/blob/master/screenshots/loginresult.png?raw=true" data-hpc="true" weight=500 height=300 class="Box-sc-g0xbh4-0 fzFXnm">
  </div>
---



