# login system

attempts = 0
while attempts < 3 :
    username = input("Enter your Username :")
    password = input("Enter your Password :")
    if username == "admin" and password == "admin123":
        print("Access Granted!")
        break
    if username == "" and password == "":
        raise ValueError("Fill empty fields!")
    else:
        print("Access Denied!")
    attempts += 1


# shopping Cart
shopping_cart = [
    "ghee" ,
    "sugar" ,
    "flour" ,
    "oil" ,
    "salt" ,
    "peanuts"
]

try:
    search = int(input("Enter product index you want to search :"))
    print(f"{shopping_cart[search]}")
    
except IndexError:
    print("Index out of bound!")


# student dictionary
student = {
    "name": "Hamna",
    "cgpa": 3.9
}

try :
    keyy = input("Enter key you want to search :")
    print(f"{keyy} : {student[keyy]}")
    
except KeyError :
    print("Enter correct key !")

