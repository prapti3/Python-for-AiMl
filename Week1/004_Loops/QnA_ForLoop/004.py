# Take a number as input and print its table


num = int(input("Enter the number : "))
# table
for i in range(1,11,1):
    print(f"{num} * {i} : ",num*i)