# Separate each digit of a number and print it on the new line

num = int(input("Enter the number: "))
digits = []


while num >0:
    digit = num %10
    # print(digit)
    digits.append(digit)
    num = num//10  
     
    
for d in digits[::-1]:
    print(d)
    

