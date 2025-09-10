# Write a program to count how many times each character appears in a string.


def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Example usage:
input_string = "hello world"
result = count_characters(input_string)
print("Character count:", result)

