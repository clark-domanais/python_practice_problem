
numbers = []

# Ask user to input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Find the numbers that are duplicated in the list
from collections import Counter
count = Counter(numbers)
duplicates = [num for num, freq in count.items() if freq > 1]

# Display duplicates
if duplicates:
    print("Numbers that have duplicates:", duplicates)
else:
    print("No duplicates found in the list.")
