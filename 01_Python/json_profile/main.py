import json
with open(r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\json_profile\profile.json", "w") as file:
    profile_data = {
        "name": "Hamna",
        "age": 20,
        "city": "Karachi",
        "favourite_language": "Python"
    }
    json.dump(profile_data, file, indent=4)

with open(
    r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\json_profile\profile.json",
    "r",
) as file:
    student = json.load(file)

print(student)
