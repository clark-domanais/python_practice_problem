def main():
    #Ask the user to input 10 numbers
    numbers = []
    for i in range(10):
        while True:
            try:
                value = float(input(f"Enter number {i + 1}: "))
                numbers.append(value)
                break
            except ValueError:
                print("Please enter a valid number.")

    #Compute first number minus the remaining numbers
    result = numbers[0]
    for n in numbers[1:]:
        result -= n

    print("Result:", result)


if __name__ == "__main__":
    main()