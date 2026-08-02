class Student:

    def __init__(self, name ,age ,dept):

        self.name = name
        self.age = age
        self.dept = dept

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am from the {self.dept} department.")


student1 = Student("Hamna", 21, "Computer Science")
student2 = Student("Hammad", 20, "Mathematics")

student1.introduce()
student2.introduce()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)
car4 = Car("Chevrolet", "Malibu", 2018)
car5 = Car("BMW", "3 Series", 2022)

car1.display_info()
car2.display_info()
car3.display_info()
car4.display_info()
car5.display_info()



class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount.")
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance}")

account1 = BankAccount("123456", "Alice", 1000)
account1.display_balance()
account1.deposit(500)
account1.withdraw(200)

account2 = BankAccount("789012", "Bob", 2000)
account2.display_balance()
account2.deposit(1000)
account2.withdraw(500)



class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rec1 = rectangle(5, 10)
print(f"Area of rectangle: {rec1.area()}")
rec2 = rectangle(3, 7)
print(f"Perimeter of rectangle: {rec2.perimeter()}")



class employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def display_info(self):
        print(f"Employee Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")
        
emp1 = employee("Hamna", "Manager", 60000)
emp1.display_info()

emp2 = employee("Hammad", "Developer", 50000)
emp2.display_info()