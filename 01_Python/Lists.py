shoppiing = ["milk", "eggs", "bread", "butter"]
print(shoppiing[0])  # Output: milk
print(shoppiing[1])  # Output: eggs 
print(shoppiing[2])  # Output: bread
print(shoppiing[3])  # Output: butter


languages = ["Python", "Java", "C++", "JavaScript"]
# list slicing
print(languages[1:3])  # Output: ['Java', 'C++']
print(len(languages))  # Output: 4
languages.append("Ruby")
print(languages)  
languages.insert(2, "PHP")
print(languages)
languages.remove("C++")
print(languages)
languages.pop()
print(languages)

languages[0] = "Go"
print(languages)  


for shopping in shoppiing:
    print(shopping)
    
    
shoppiing.reverse()
print(shoppiing)

numbers = [12 , 45, 34, 27 ,67 , 12 , 62 , 13, 18, 94]
numbers.sort()
print(numbers)
print(numbers.count(12))

print(numbers.index(67)) 


# favourite movies
movies = ["Inception", "The Dark Knight", "Interstellar", "The Matrix" , "Pulp Fiction"]
print(movies[0])
print(movies[-1])
print(len(movies))

# Student list manager
students = []
for i in range(5):
    name = input("Enter student name: ")
    students.append(name)
print("Student List:", students)

# shopping list manager
shopping_list = []
for i in range(3):
    item = input("Enter an item for the shopping list: ")
    shopping_list.append(item)
print("Shopping List:", shopping_list)
shopping_list.append("eggs")
print("Updated Shopping List:", shopping_list)
shopping_list.remove("butter")
print("Updated Shopping List after removing butter:", shopping_list)

# marks analyzer
marks = [67, 78, 92, 85, 74]
print(max(marks))
print(min(marks))
print(sum(marks))
print(sum(marks)/len(marks))


# To-Do List
tasks = []
operation = input("Enter action you want to perform(1. add task 2. view task 3. remove task ): ")
if operation == "1":
    task = input("enter task you wanna add:")
    tasks.append(task)
    print(tasks)
if operation == "2":
    print(tasks)
if operation == "3":
    print(tasks)
    task = input("enter task you wanna remove:")
    tasks.remove(task)
    print(tasks)
    
    
