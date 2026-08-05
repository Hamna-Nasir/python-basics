import requests

def search_user(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("Success!")
        print("Username:", data["login"])
        print("Name:", data.get("name", "N/A"))
        print("Followers:", data["followers"])
        print("Public Repositories:", data["public_repos"])
    else:
        print("User not found!")


def view_repos(username):
    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()

        if len(repos) == 0:
            print("No repositories found.")
        else:
            print(f"\nRepositories of {username}:")
            for repo in repos:
                print("-", repo["name"])
    else:
        print("User not found!")


def save_history(username):
    with open("history.txt", "a") as file:
        file.write(username + "\n")


def view_history():
    try:
        with open("history.txt", "r") as file:
            print("\nSearch History:")
            print(file.read())
    except FileNotFoundError:
        print("No search history found.")

def delete_history():
    with open("history.txt", "w") as file:
        file.write("")
    print("Search history deleted successfully!")


def exit_program():
    print("Thank you for using GitHub Profile Viewer!")
    exit()
