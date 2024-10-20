# Function to find the sum of the first and last digit
def sum_first_last_digit(num):
    num_str = str(num)
    return int(num_str[0]) + int(num_str[-1])

# Example usage
number = 12345  # Change this to test different values
result = sum_first_last_digit(number)
print(f'Sum of the first and last digit: {result}')
