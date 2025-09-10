# accept a number and print its reverse

num = int(input("Enter the number : "))
digits = []

while num > 0:
    digit = num % 10
    print(digit)
    num = num //10
    
