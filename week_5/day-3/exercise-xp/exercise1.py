def built_in_functions():
    """
    This function demonstrates the use of built-in Python functions: abs(), int(), and input().
    It prints the results of these functions and takes user input using the input() function.

    Parameters:
    None

    Returns:
    None
    """

    # Absolute value of a number
    num1 = -10
    print(f"The absolute value of {num1} is {abs(num1)}")

    # Converting a string to an integer
    num2 = "20"
    print(f"The integer equivalent of {num2} is {int(num2)}")

    # Taking user input and converting to integer
    num3 = input("Enter a number: ")
    print(f"The integer equivalent of {num3} is {int(num3)}")

built_in_functions()