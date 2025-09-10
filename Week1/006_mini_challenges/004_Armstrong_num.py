# Create a program that asks for a number and prints whether it is an Armstrong number (e.g., 153 → 1³+5³+3³=153).


num = int(input("Enter a number: "))
sum_of_cubes = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10
if sum_of_cubes == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    
# Example usage:
# num = 153

# Output: 153 is an Armstrong number.
# num = 123
# Output: 123 is not an Armstrong number.
