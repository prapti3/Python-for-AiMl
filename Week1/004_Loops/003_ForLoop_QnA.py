# 1. accept an integer and print hello world n times

number = input("Enter the number : ")
print(f"Your enter number is : {number}")

repetition = int(input("Enter how many times you need to print number : "))

for i in range(repetition):
    print(number)