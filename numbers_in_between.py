
#Ask the user to input 2 numbers
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter a number: "))

#Print the numbers in between the 2 numbers that's been inputted
if num_1 < num_2:
    for i in range(num_1 + 1, num_2):
        print(i)