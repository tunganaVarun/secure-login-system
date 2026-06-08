# 🔐 Secure Login System

A secure web-based authentication system built using Flask, SQLite, and bcrypt. The application allows users to register, log in, and securely manage sessions while protecting passwords through hashing and validating user input.

## Features

* User Registration
* Secure Login Authentication
* Password Hashing using bcrypt
* Password Strength Validation
* Duplicate Username/Email Prevention
* Session Management
* Protected Dashboard
* Logout Functionality
* Flash Messages
* SQL Injection Protection using Parameterized Queries
* Responsive User Interface

## Technologies Used

* Python
* Flask
* SQLite
* bcrypt
* HTML
* Bootstrap 5

## Installation

1. Clone the repository

```bash
git clone https://github.com/tunganaVarun/secure-login-system.git
```

2. Navigate to the project folder

```bash
cd secure-login-system
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the database initialization script

```bash
python init_db.py
```

5. Start the application

```bash
python app.py
```

6. Open in browser

```text
http://127.0.0.1:5000
```

## Security Features

* Passwords are stored using bcrypt hashing.
* Parameterized SQL queries prevent SQL Injection attacks.
* Password strength validation improves account security.
* User sessions are protected through Flask session management.

## Future Improvements

* Two-Factor Authentication (2FA)
* Password Reset Functionality
* Email Verification
* CSRF Protection
* Account Lockout After Multiple Failed Attempts

## Author

Varun Sai Tungana
