
#Ask the program to print all number from 0-100 except the numbers with 0 in them
for number in range(101):
    if '0' not in str(number):
        print(number)