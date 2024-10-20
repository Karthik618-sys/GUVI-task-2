# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create lists for even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print results
print(f'Even numbers: {even_numbers}')
print(f'Odd numbers: {odd_numbers}')
