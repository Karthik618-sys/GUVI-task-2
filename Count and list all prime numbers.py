# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create list for prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]

# Print results
print(f'Prime numbers: {prime_numbers}')
print(f'Number of prime numbers: {len(prime_numbers)}')
