"""
Password strength checker
Author: Emeraude Mputu Muhindo
Description: A Python program that evaluate password strength
and provides suggestions for creating stronger passwords.
"""

# Project: Password Strength Checker
# Version: 1.0
# Python Version: 3.14

import string

def check_password_strength(password):
    if len(password) < 8:
        return "Weak : Password must contain at least 8 characters"

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digits = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = sum([has_uppercase, has_lowercase, has_digits, has_special])


    suggestions = []

    if not has_uppercase:
        suggestions.append("an uppercase letter")

    if not has_lowercase:
        suggestions.append("a lowercase letter")

    if not has_digits:
        suggestions.append("a digit")

    if not has_special:
        suggestions.append("a special character")

    if score <= 1:
        return "Weak : consider adding " + ", ".join(suggestions) + "."

    elif score == 2:
        return "Moderate : consider adding " + ", ".join(suggestions) + "."

    elif score == 3:
        return "Good: Consider adding " + ", ".join(suggestions) + "."

    else:
        return "Strong : Your password passes all your characters-variety checks."


password = input("Enter your password: ")
print(check_password_strength(password))




