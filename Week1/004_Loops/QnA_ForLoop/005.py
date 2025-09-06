#sum upto n terms

num = int(input("Enter the number : "))
total =0 
for i in range(1,num+1,1):
    if(i <= num):
        total += i
print(total)