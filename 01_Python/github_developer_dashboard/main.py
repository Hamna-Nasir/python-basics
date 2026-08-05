import user
import config
from github_api import *


while True:
    print("=" * 50)
    print("Welcome to Github Developer Dashboard")
    print("=" * 50)

    print("\nMenu:")
    print("1. Search GitHub User")
    print("2. View Repository List")
    print("3. View Previous Searches")
    print("4. Delete Search History")
    print("5. Exit")
    print("="*5)
    
    try:
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1 :
            username = input("Enter Usename you want to search:")
            search_user(username)
            save_history(username)
        elif choice == 2 :
            username = input("Enter Username you want to view repositories:")
            view_repos(username)
        elif choice == 3 :
            view_history()
        elif choice == 4 :
             delete_history()
        elif choice == 5 :
            exit_program()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")