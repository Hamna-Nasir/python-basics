password = input("Enter your password: ")
def password_validator(password):
    if len(password) < 8:
        return "password is weak"
    elif len(password) >= 8:
        return "password is strong"
print(password_validator(password))