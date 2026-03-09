
#Ask the user to input 10 numbers and print how many of them are odd

odd_count = 0

for i in range(10):
    number = float(input(f"Enter number {i + 1}: "))
    if number % 2 != 0:
        odd_count += 1

print(f"\nThe number of odd numbers is: {odd_count}")