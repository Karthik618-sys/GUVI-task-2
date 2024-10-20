# Function to find minimum difference
def min_diff_mangoes(mangoes, students):
    mangoes.sort()
    min_diff = float('inf')
    for i in range(len(mangoes) - students + 1):
        diff = mangoes[i + students - 1] - mangoes[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

# Example usage
mangoes = [10, 15, 30, 20, 25, 35]
students = 3
result = min_diff_mangoes(mangoes, students)
print(f'Minimum difference: {result}')
