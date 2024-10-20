# Function to find first non-repeating element
def first_non_repeating(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    for item in lst:
        if frequency[item] == 1:
            return item
    return None

# Example usage
lst = [1, 2, 2, 3, 4, 4, 5]
result = first_non_repeating(lst)
print(f'First non-repeating element: {result}')
