# Function to find triplet with given sum
def find_triplet_with_sum(lst, target_sum):
    lst.sort()
    for i in range(len(lst) - 2):
        left = i + 1
        right = len(lst) - 1
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            if current_sum == target_sum:
                return [lst[i], lst[left], lst[right]]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return []

# Example usage
numbers = [10, 20, 30, 9]
target_sum = 59
triplet = find_triplet_with_sum(numbers, target_sum)
print(f'Triplet with sum {target_sum}: {triplet}')
