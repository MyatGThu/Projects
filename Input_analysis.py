# Optimized by CHATGPT

# Getting input from user

input_numbers = input("Enter a list of numbers separated by a comma: ")

# Convert the input string into a list

numbers = [int(number) for number in input_numbers.split(",")]

sum_of_numbers = sum(numbers)

avg_of_numbers = sum_of_numbers / len(numbers)

max_number = max(numbers)

min_number = min(numbers)

print("Sum of numbers: ")