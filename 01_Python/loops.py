# for loop
for i in range(5):
    print("Hello, World!")

for i in range(1,11):
    print(i)
    
for i in range(0,11,2):
    print(i)
    
for num in range(1, 11):
    print(num)
    
# while loop 
count = 0
while count <= 5:
    print("Count:", count)
    count += 1
    
var = 0
while var<=2:
    print("Welcome")
    var += 1
    
    
# break keyword
for i in range(1, 11):
    if i == 5:
        break #aagy poora loop ko break kar dega
    print(i)
    
# continue keyword
for i in range(1, 11):
    if i == 5:
        continue #ye srf condition ko skip kar dega aur loop continue karega
    print(i)
    
    