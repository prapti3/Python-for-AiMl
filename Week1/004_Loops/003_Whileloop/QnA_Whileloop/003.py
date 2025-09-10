# Accept the number and check if it is a pallindromic number (if number and its reverse are equal)


num = int(input("Enter the number : "))
original_num = num  # Store the original number
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original_num == reverse:
    print(f"{original_num} is Palindrome")
else:
    print(f"{original_num} is Not Palindrome")