
#Ask the user to input 10 numbers
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

#Check for duplicate numbers
unique_numbers = set()
duplicates = set()
for num in numbers:
    if num in unique_numbers:
        duplicates.add(num)
    else:
        unique_numbers.add(num)
