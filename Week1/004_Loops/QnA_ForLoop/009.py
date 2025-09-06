# Accept the number and check if it a perfect number or not 

num = int(input("Enter the number : "))
total =0

for i in range(1,num):
    if(num%i == 0):
        total += i
        
        print(i)
        
if(total == num):
    print(f"Number is a perfect number: {num}")
else:
    print("Number is not a perfect number")
    
    
# print(total)
        