# Function to find sub-list with sum zero
def has_zero_sum_sublist(lst):
    sum_set = set()
    current_sum = 0
    for num in lst:
        current_sum += num
        if current_sum == 0 or current_sum in sum_set:
            return True
        sum_set.add(current_sum)
    return False

# Example usage
numbers = [4, 2, -3, 1, 6]
result = has_zero_sum_sublist(numbers)
print(f'Is there a sub-list with sum zero? {result}')
