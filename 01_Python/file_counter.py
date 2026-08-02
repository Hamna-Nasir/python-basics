file = input("Enter the file path: ")
with open(file, "r") as file:
    content = file.read()
    line_count = content.count('\n')
    print(f"Number of lines in the file: {line_count}")
    number_of_words = len(content.split())
    print(f"Number of words in the file: {number_of_words}")
    number_of_characters = len(content)
    print(f"Number of characters in the file: {number_of_characters}")
    