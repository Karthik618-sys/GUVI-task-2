# Define three lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 8, 9, 10, 11]

# Find duplicates in three lists
duplicates = set(list1) & set(list2) & set(list3)
print(f'Duplicates in the three lists: {duplicates}')
