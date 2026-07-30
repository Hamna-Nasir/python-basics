name = "Hamna"
lname = "NASIR"
favourite_language = "Python"
hobby = "Crochetting"
city = "Karachi"
sentence = "I am a student of AI Product Engineering"
text = "banana"

# String Indexing
print(name[0])
print(name[3])
print(name[-1])

# String Slicing
print(favourite_language[0:4])

# String Methods
print(name.upper())
print(lname.lower())
print(city.title())
print(sentence.replace("AI Product Engineering", "Data Science"))
print(text.count("a"))
print(text.find("n"))
print(len(name))

# f-Strings
print(f"My name is {name} {lname} and I live in {city}. My favourite programming language is {favourite_language} and my hobby is {hobby}.")

