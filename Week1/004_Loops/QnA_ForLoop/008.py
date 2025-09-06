# print all the factors of number

num = int(input("Enter the number : "))


for i in range(1,num+1,1):
    if(num%i == 0):
        print(i)
    