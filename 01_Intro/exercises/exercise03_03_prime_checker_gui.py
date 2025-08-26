"""
Exercise 3.3: Prime Number Checker with GUI

This is the main assignment for Exercise 3: Create a GUI application that checks
if a number is prime or not. This combines all concepts learned in the previous
GUI exercises.

This exercise demonstrates:
- Complete GUI application with user input validation
- Prime number calculation algorithm
- Error handling for invalid input
- Professional GUI layout and user experience

For C# developers: This is similar to creating a Windows Forms application with
input validation, business logic, and user feedback.
"""

import tkinter as tk
from tkinter import messagebox
import math


def is_prime(n):
    """
    Determines if a number is prime.
    
    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
        
    Algorithm explanation:
    - Numbers ≤ 1 are not prime
    - 2 is prime (only even prime)
    - Even numbers > 2 are not prime
    - For odd numbers, check divisibility up to √n
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Only check odd divisors up to sqrt(n)
    # This is much more efficient than checking all numbers up to n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def check_prime():
    """
    Event handler for the "Check Prime" button.
    Gets user input, validates it, and displays the result.
    """
    try:
        # Get the input from the entry field
        user_input = number_entry.get().strip()
        
        if not user_input:
            # Show error if input is empty
            result_label.config(
                text="Please enter a number!",
                fg="red",
                font=("Arial", 12, "bold")
            )
            return
        
        # Convert input to integer
        number = int(user_input)
        
        if number < 0:
            # Handle negative numbers
            result_label.config(
                text="Please enter a positive number!",
                fg="red",
                font=("Arial", 12, "bold")
            )
            return
        
        # Check if the number is prime
        if is_prime(number):
            result_text = f"{number} is a PRIME number! ✓"
            result_color = "green"
        else:
            result_text = f"{number} is NOT a prime number ✗"
            result_color = "red"
        
        # Display result
        result_label.config(
            text=result_text,
            fg=result_color,
            font=("Arial", 12, "bold")
        )
        
        # Show additional information for educational purposes
        show_prime_info(number)
        
    except ValueError:
        # Handle non-numeric input
        result_label.config(
            text="Please enter a valid integer!",
            fg="red",
            font=("Arial", 12, "bold")
        )


def show_prime_info(number):
    """
    Shows additional information about the number in the info text area.
    Educational feature to help understand prime numbers better.
    
    Args:
        number (int): The number that was checked
    """
    info_text.delete('1.0', tk.END)  # Clear previous info
    
    if number <= 1:
        info = f"Numbers ≤ 1 are not considered prime by definition.\n"
    elif number == 2:
        info = f"2 is the only even prime number.\n"
    elif is_prime(number):
        info = f"Prime number analysis for {number}:\n"
        info += f"• Only divisible by 1 and {number}\n"
        info += f"• Checked divisors up to {int(math.sqrt(number))}\n"
        info += f"• No divisors found - it's prime!\n"
    else:
        info = f"Composite number analysis for {number}:\n"
        info += f"• Found at least one divisor other than 1 and {number}\n"
        
        # Find and show the first few divisors
        divisors = []
        for i in range(2, min(number, 20)):  # Limit to first 20 for display
            if number % i == 0:
                divisors.append(i)
                if len(divisors) >= 3:  # Show first 3 divisors
                    break
        
        if divisors:
            info += f"• Some divisors: {', '.join(map(str, divisors))}\n"
    
    info_text.insert('1.0', info)


def clear_input():
    """
    Clears the input field and result display.
    Convenience function for user experience.
    """
    number_entry.delete(0, tk.END)
    result_label.config(text="Enter a number and click 'Check Prime'", fg="gray")
    info_text.delete('1.0', tk.END)
    number_entry.focus()


def show_about():
    """
    Shows information about prime numbers.
    Educational dialog to help users understand the concept.
    """
    about_text = """Prime Numbers Information:

A prime number is a natural number greater than 1 
that has exactly two distinct positive divisors: 
1 and itself.

Examples:
- 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...

Non-prime examples:
- 1 (not prime by definition)
- 4 (divisible by 1, 2, 4)
- 6 (divisible by 1, 2, 3, 6)
- 8 (divisible by 1, 2, 4, 8)

Fun facts:
- 2 is the only even prime number
- There are infinitely many prime numbers
- Large primes are used in cryptography"""
    
    messagebox.showinfo("About Prime Numbers", about_text)


def main():
    """
    Creates the main prime checker GUI application.
    Combines all GUI elements into a professional-looking interface.
    """
    global root, number_entry, result_label, info_text
    
    # Create main window
    root = tk.Tk()
    root.title("Prime Number Checker")
    root.geometry("500x450")
    root.resizable(True, True)  # Allow resizing
    
    # Title
    title_label = tk.Label(
        root,
        text="Prime Number Checker",
        font=("Arial", 16, "bold"),
        bg="lightblue",
        fg="darkblue",
        pady=10
    )
    title_label.pack(fill=tk.X)
    
    # Main input frame
    input_frame = tk.Frame(root)
    input_frame.pack(pady=20)
    
    tk.Label(
        input_frame,
        text="Enter a number to check:",
        font=("Arial", 12)
    ).pack()
    
    # Number entry with larger font
    number_entry = tk.Entry(
        input_frame,
        font=("Arial", 14),
        width=20,
        justify=tk.CENTER
    )
    number_entry.pack(pady=10)
    number_entry.focus()  # Set initial focus
    
    # Bind Enter key to check prime
    number_entry.bind('<Return>', lambda event: check_prime())
    
    # Button frame
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    
    # Check Prime button (main action)
    check_button = tk.Button(
        button_frame,
        text="Check Prime",
        font=("Arial", 12, "bold"),
        bg="lightgreen",
        fg="darkgreen",
        command=check_prime,
        width=12
    )
    check_button.pack(side=tk.LEFT, padx=5)
    
    # Clear button
    clear_button = tk.Button(
        button_frame,
        text="Clear",
        font=("Arial", 10),
        command=clear_input,
        width=8
    )
    clear_button.pack(side=tk.LEFT, padx=5)
    
    # About button
    about_button = tk.Button(
        button_frame,
        text="About",
        font=("Arial", 10),
        command=show_about,
        width=8
    )
    about_button.pack(side=tk.LEFT, padx=5)
    
    # Result display
    result_label = tk.Label(
        root,
        text="Enter a number and click 'Check Prime'",
        font=("Arial", 12),
        fg="gray",
        pady=15
    )
    result_label.pack()
    
    # Information text area
    info_frame = tk.Frame(root)
    info_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
    
    tk.Label(info_frame, text="Analysis:", font=("Arial", 10, "bold")).pack(anchor="w")
    
    info_text = tk.Text(
        info_frame,
        height=6,
        width=60,
        font=("Arial", 10),
        wrap=tk.WORD,
        bg="lightyellow"
    )
    info_text.pack(fill=tk.BOTH, expand=True)
    
    # Bottom frame with quit button
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(pady=10)
    
    quit_button = tk.Button(
        bottom_frame,
        text="QUIT",
        font=("Arial", 10, "bold"),
        fg="red",
        command=root.quit,
        width=10
    )
    quit_button.pack()
    
    # Start the application
    root.mainloop()


def test_prime_function():
    """
    Tests the prime checking function with known values.
    Useful for debugging and verification.
    """
    test_cases = [
        (1, False), (2, True), (3, True), (4, False), (5, True),
        (6, False), (7, True), (8, False), (9, False), (10, False),
        (11, True), (12, False), (13, True), (17, True), (25, False),
        (29, True), (100, False), (101, True)
    ]
    
    print("Testing prime function:")
    for number, expected in test_cases:
        result = is_prime(number)
        status = "✓" if result == expected else "✗"
        print(f"{status} {number}: {result} (expected {expected})")


if __name__ == "__main__":
    print("Starting Exercise 3.3 - Prime Number Checker GUI")
    print("This is the complete GUI application that combines:")
    print("- User input with validation")
    print("- Prime number algorithm")
    print("- Professional GUI layout")
    print("- Error handling and user feedback")
    print("-" * 50)
    
    # Uncomment to run tests first
    # test_prime_function()
    
    main()


# This completes Exercise 3 (parts 3.1, 3.2, 3.3)
# This is the final exercise for the introduction to Python with GUI programming.
# You now have experience with:
# - Basic Python syntax and data structures
# - List operations and control structures  
# - GUI programming with tkinter
# - User input validation and error handling