'''# product inventory
products = {"Laptop": 120000, "Mouse": 2500, "Keyboard": 4000}
prod = input("Enter product you want to search:")
if prod in products:
    print(f"{prod} price is {products.get(prod)}")
else:
    print("Product not found in inventory")


# student marks
marks = {"Math": 90, "English": 85, "Physics": 80}
def sumup():
    total = 0
    for value in marks.values():
        total = total + value
    return total
print(f"Total Marks : {sumup()}")
total = sumup()
no_of_marks = len(marks)
        
def avg():
    avg_marks = total / no_of_marks
    return avg_marks
print(f"Average Marks : {avg()}")'''


# favourite foods
foods = {"Hamna": "Pasta", "Ali": "Biryani", "Sara": "Pizza"}
name = input("Enter your name :")
if name in foods.keys():
    print(foods.get(name))
else:
    print("Name not found!")