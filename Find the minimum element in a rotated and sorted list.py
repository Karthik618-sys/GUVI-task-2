# Function to find minimum in a rotated and sorted list
def find_min_rotated_sorted(arr):
    return min(arr)

# Example usage
rotated_sorted_list = [4, 5, 6, 7, 10, 3, 2]  # Change this to test different lists
min_element = find_min_rotated_sorted(rotated_sorted_list)
print(f'Minimum element: {min_element}')
