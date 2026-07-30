# tuple
students = ("Hamna" , 21 , "SSUET")
# students[0] = "Hammad" # error as tuple is immutable
print(students)

months = (
    "January",
    "Febuary",
    "March",
    "April"
)
print(months[0])
print(months[-1])
print(len(months))


numbers = (1 ,3, 5, 7,1, 4, 8)
print(numbers.count(1))
print(numbers.index(5))


# sets
number = {1 , 3, 5, 1, 4, 6, 3, 2, 9, 10}  
number1 = { 34 , 53, 64,6 , 92, 122}# auto removes duplicates 
print(numbers)

number.add(22)
print(number)

number.remove(5)
print(number)

number.discard(44) # won't raise error if number is missing 

for numb in number:
    print(numb) 

print(number | number1)
print(number & number1) # print common value 
print(number - number1) # print difference


frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "JavaScript"}

print(frontend | backend)
print(frontend & backend)
print(frontend - backend)


# favourite fruits 
fav_fruits = ("kiwi" , "mango" , "pineapple" , "strawberry" , "cherry")
print(fav_fruits[0])
print(fav_fruits[-1])
print(len(fav_fruits))

# unique skills
skills = set()
for i in range(5):
    skill = input("enter skill:")
    skills.add(skill)
print(skills)
common_skills = {"java" , "python"}
print(f"unique skills are :{skills - common_skills}") 
