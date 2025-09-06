# print the sum of all even & odd numbers in a range separately

num = 10
even_sum =0
odd_sum = 0

for i in range(1,num+1,1):
    if(i%2 ==0):
        even_sum += i
    elif(i%2 != 0):
        odd_sum +=i 
print(f"Even num addition : ",even_sum )
print("Odd num addition : ",odd_sum)