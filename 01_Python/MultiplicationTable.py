num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    


# sum calculator
number = int(input("Enter a number: "))
sum = 0
for i in range(1, number + 1):
    sum += i
print("The sum of numbers from 1 to", number, "is:", sum)


# countdown 
num = int(input("Enter a number to start countdown: "))
while num >= 1:
    print(num)
    num -= 1
    