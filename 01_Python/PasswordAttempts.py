attempt = 0
while attempt < 3:
    password = input("Enter the password: ")
    if password == "1234":
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
        attempt += 1