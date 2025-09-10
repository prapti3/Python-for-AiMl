# Write a function to find the greatest common divisor (GCD) of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
# Example usage:
num1 = 56
num2 = 98
result = gcd(num1, num2)


print(f"The GCD of {num1} and {num2} is: {result}")
# Output: The GCD of 56 and 98 is: 14
# num = int(input("Enter the number: --- IGNORE ---
# while num > 0:
#     digit = num % 10
#     print(digit)
#     num = num // 10
# Output:
# 3
# 2
# 1
# 4
