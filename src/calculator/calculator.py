def main():
    while True:
        print ("Simple Calculator")
        print ("1. Add")
        print ("2. Subtract")
        print ("3. Multiply")
        print ("4. Divide")
        print ("5. Exit")

        operation = input("Choose an operation (1-5): ").strip()
        while operation not in ("1", "2", "3", "4", "5"):
            print ("Invalid input. Please choose a valid operation (1-5).")
            operation = input("Choose an operation (1-5): ").strip()
        
        first_number = input("Enter the first number: ").strip()
        second_number = input("Enter the second number: ").strip()

        try:
            first_number = float(first_number)
            second_number = float(second_number)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if operation == "1":
            result = first_number + second_number
            print(f"The result of addition is: {result}")
            symbol = "+"
        elif operation == "2":
            result = first_number - second_number
            print(f"The result of subtraction is: {result}")
            symbol = "-"
        elif operation == "3":
            result = first_number * second_number
            print(f"The result of multiplication is: {result}")
            symbol = "*"
        elif operation == "4":
            if second_number == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = first_number / second_number
            print(f"The result of division is: {result}")
            symbol = "/"

          print(f"{first_number} {symbol} {second_number} = {result}")

if__name__ == "__main__":
    main()
    

      
