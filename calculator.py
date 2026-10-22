class Calculator:

    def add(self, a, b):

        return a + b



    def subtract(self, a, b):

        return a - b



    def multiply(self, a, b):

        return a * b



    def divide(self, a, b):

        if b == 0:

            raise ValueError("Cannot divide by zero")

        return a / b





def main():

    calculator = Calculator()



    print("Python Calculator")

    print("1. Add")

    print("2. Subtract")

    print("3. Multiply")

    print("4. Divide")



    choice = input("Select an operation: ")

    first_number = float(input("Enter first number: "))

    second_number = float(input("Enter second number: "))



    try:

        if choice == "1":

            result = calculator.add(first_number, second_number)

        elif choice == "2":

            result = calculator.subtract(first_number, second_number)

        elif choice == "3":

            result = calculator.multiply(first_number, second_number)

        elif choice == "4":

            result = calculator.divide(first_number, second_number)

        else:

            print("Invalid choice")

            return



        print("Result:", result)



    except ValueError as error:

        print(error)





if __name__ == "__main__":

    main()
