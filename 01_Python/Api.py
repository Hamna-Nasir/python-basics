import requests

'''

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

data = response.json()
print(data["current_user_url"])


try:

    response = requests.get("https://api.github.com")
    response.raise_for_status()
    data = response.json()

except requests.exceptions.RequestException as e:

    print(e)

name = input("Enter your name: ")
url = f"https://api.github.com/users/{name}"
response = requests.get(url)
if response.status_code == 200:

    data = response.json()
    print(f"User: {data['login']}")
    print(f"Name: {data.get('name', 'N/A')}")
    print(f"Public Repos: {data['public_repos']}")
else:
    print("User not found!")
    
    
'''

'''
url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    joke = response.json()

    print("😂 Here's a joke!")
    print(joke["setup"])
    print(joke["punchline"])
else:
    print("Couldn't fetch a joke.")

'''

'''

url = "https://zenquotes.io/api/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Quote:")
    print(data[0]["q"])
    print("- " + data[0]["a"])
else:
    print("Failed to fetch quote.")
    
'''

url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)
if response.status_code == 200:
    dog = response.json()
    print(dog["message"])
