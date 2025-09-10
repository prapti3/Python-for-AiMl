# check all letters, digits, special characters in a string
# Given: str1 = "P@#yn26at^&i5ve"
# expected output :
# Total counts of chars, digits, and symbols
# chars = 8
# digits = 3
# symbols = 4

str = "P@#yn26at^&i5ve&&&"
chars =0
digits = 0
symbols =0

for i in str:
    if i.isalpha():
        chars+=1
    elif i.isdigit():
        digits +=1
    else:
        symbols+=1
        
print("Characters are : ", chars)
print("digits are : ", digits)
print("Symbols are : ",symbols)
    

    

    

