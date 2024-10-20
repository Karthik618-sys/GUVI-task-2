# Function to check if a number is happy
def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(char)**2 for char in str(num))
    return num == 1

# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create list for happy numbers
happy_numbers = [num for num in numbers if is_happy(num)]

# Print results
print(f'Happy numbers: {happy_numbers}')
print(f'Number of happy numbers: {len(happy_numbers)}')
