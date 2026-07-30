attempt = 0
actual_num = 55
guess_num = int(input("Enter a number: "))
while guess_num != actual_num :
    print("Incorrect guess. Try again.")
    guess_num = int(input("Enter a number: "))
    attempt += 1
print("Congratulation! correct guess")