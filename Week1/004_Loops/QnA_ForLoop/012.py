# check string is palindrome or not

name = input("Enter your name : ")
name_rev = name[::-1];
if name == name_rev:
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")
