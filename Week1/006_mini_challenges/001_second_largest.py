# Write a program to find the second largest number in a list.

def second_largest(numbers):
    first = second = float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None


# Example usage:
numbers = [10, 20, 4, 45, 99]
result = second_largest(numbers)
print("The second largest number is:", result)
