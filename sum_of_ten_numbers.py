
#Ask the user to input 10 numbers and print their sum

total = 0

for i in range(10):
    number = float(input(f"Enter number {i + 1}: "))
    total += number

print(f"\nThe sum of all the numbers is: {total}")
