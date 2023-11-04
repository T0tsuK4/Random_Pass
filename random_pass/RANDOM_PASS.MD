# RANDOM_PASS - Random Password Generator

This is a simple Python program for generating random passwords with options for security, encryption, and storage. You can adjust the password length, choose whether it should be secure, and opt to save the password to a file or copy it to the clipboard.

## Requirements

Make sure you have Python installed on your system. The program uses the `random`, `time`, `sys`, `pyperclip`, and `hashlib` libraries.

## Usage

Run the `random_pass.py` program and follow the instructions. It will prompt you for the password length and whether you want to generate a secure password.

## Features

- Generation of random passwords.
- Option to generate secure passwords (with at least one uppercase letter, lowercase letter, number, and symbol).
- Ability to save the password to a file.
- Option to copy the generated password to the clipboard.
- Password encryption using SHA-256.

## Example Usage

```shell
$ python random_pass.py
Enter password length (between 8 and 36 characters): 12
Do you want to generate a secure password? (Y/n): Y
Generating password with length 12
Generating password: [100%] [===================================================>]
Generated password: kM7^Zg4cNtW3
What do you want to do with the password? (1 - Save to file, 2 - Copy to clipboard, 3 - Exit): 2
Password copied to the clipboard
Encrypted password (SHA-256): 39c9b1ea13e973dcb5a5c4eabeff1ec7c899366889c1d6c4f665080e87e24bbf5
```

## Author

Developed by [T0tsuK4]

## License

This project is licensed under the MIT License - see the [MIT](LICENSE) file for details.
