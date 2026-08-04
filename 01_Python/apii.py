import requests
url = "https://jsonplaceholder.typicode.com/posts"
student = {
    "name": "Hamna",
    "age" : 21
}

response = requests.post(url ,json=student)

if response.status_code == 201:
    result = response.json()

    print("Post created successfully!")
    print("Name:", result["name"])
    print("Age:", result["age"])
else:
    print("Failed to create post.")


delete = requests.delete(url)

