"""
Exercise 1: Hello World and Variable Conditions

This exercise demonstrates:
- Basic print statements (like Console.WriteLine in C#)
- Variable declaration and input (simpler syntax than C#)
- Conditional statements (similar to if statements in C#)
- Running programs from both IDE and command line

For C# developers: Python doesn't require explicit type declarations
and uses input() instead of Console.ReadLine()
"""


def main():
    """
    Main function that demonstrates basic Python concepts.
    Similar to Main() method in C# but no static keyword needed.
    """
    print("Hello World")
    
    # Get input from user (similar to Console.ReadLine() in C#)
    # Note: input() always returns a string, need int() to convert
    try:
        user_input = int(input("Enter a number: "))
        
        # Conditional check - Python uses 'and' instead of '&&'
        if user_input > 3:
            print(f"Your number {user_input} is greater than 3!")
            print("This message appears when the condition is met.")
        else:
            print(f"Your number {user_input} is 3 or less.")
            
    except ValueError:
        # Handle case where user doesn't enter a valid number
        print("Please enter a valid number next time.")


# Python equivalent of "if __name__ == '__main__'" 
# This ensures main() only runs when script is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()


# Instructions for running:
# From PyCharm: Click the green arrow or press Ctrl+Shift+F10
# From command prompt: navigate to this directory and run: python exercise01_hello_world.py