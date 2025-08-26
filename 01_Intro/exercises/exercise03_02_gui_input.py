"""
Exercise 3.2: GUI with User Input - Entry Widgets and Text Areas

This exercise demonstrates:
- Adding Entry widgets for user input (like TextBox in C#)
- Text widgets with scrollbars for larger text display
- Getting user input and updating the interface
- Layout management with frames and positioning

For C# developers: Entry ~ TextBox, Text ~ RichTextBox/TextArea,
Scrollbar ~ ScrollBar, but tkinter uses pack() instead of anchor points.
"""

import tkinter as tk
from tkinter import scrolledtext


def change_text():
    """
    Event handler that gets user input and updates the main label.
    Demonstrates how to read from Entry widgets and update other widgets.
    """
    # Get the text that user typed in the entry field
    user_input = name_entry.get()  # Like textBox.Text in C#
    
    if user_input.strip():  # Check if input is not empty
        # Update the main label with user's input
        welcome_label.config(text=f"Hej {user_input}!\nWelcome to my program!")
    else:
        # Show default message if no input
        welcome_label.config(text="Please enter your name first!")


def main():
    """
    Creates GUI with input fields and text display areas.
    Demonstrates more advanced tkinter layout and widgets.
    """
    global root, welcome_label, name_entry
    
    # Create main window
    root = tk.Tk()
    root.title("Exercise 3.2 - GUI with Input")
    root.geometry("500x400")
    
    # Main frame for the top part (label and buttons)
    main_frame = tk.Frame(root)
    main_frame.pack(pady=10)
    
    # Welcome label (will be updated when user clicks button)
    welcome_label = tk.Label(
        main_frame,
        text="Hej, velkommen til mit program\n\n\n",
        font=("Arial", 12)
    )
    welcome_label.pack()
    
    # Buttons frame
    button_frame = tk.Frame(main_frame)
    button_frame.pack(pady=10)
    
    # QUIT button
    quit_button = tk.Button(
        button_frame,
        text="QUIT",
        fg="red",
        font=("Arial", 10, "bold"),
        command=quit
    )
    quit_button.pack(pady=5)
    
    # Change text button
    change_button = tk.Button(
        button_frame,
        text="Change text",
        font=("Arial", 10),
        command=change_text
    )
    change_button.pack()
    
    # Text area with scrollbar (similar to RichTextBox in C#)
    text_frame = tk.Frame(root)
    text_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    # Create Text widget with Scrollbar
    text_area = tk.Text(
        text_frame,
        height=6,
        width=60,
        wrap=tk.WORD,  # Wrap words at line end
        font=("Arial", 10)
    )
    
    # Scrollbar for the text area
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Pack text area and connect to scrollbar
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Connect scrollbar to text widget
    text_area.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_area.yview)
    
    # Add some sample text (like the Hamlet quote from the exercise)
    sample_text = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
    
    text_area.insert(tk.END, sample_text)
    
    # Input frame at the bottom
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)
    
    # Label for input instruction
    name_label = tk.Label(
        input_frame,
        text="Indtast navn:",
        font=("Arial", 10)
    )
    name_label.pack(side=tk.LEFT, padx=(10, 5))
    
    # Entry widget for user input (like TextBox in C#)
    name_entry = tk.Entry(
        input_frame,
        font=("Arial", 10),
        width=20
    )
    name_entry.pack(side=tk.LEFT, padx=5)
    
    # Set focus to entry field so user can type immediately
    name_entry.focus()
    
    # Bind Enter key to change_text function (convenience feature)
    name_entry.bind('<Return>', lambda event: change_text())
    
    # Start the GUI
    root.mainloop()


def create_advanced_input_demo():
    """
    Demonstrates more advanced input widgets and validation.
    Educational example showing different types of input handling.
    """
    demo_window = tk.Tk()
    demo_window.title("Advanced Input Demo")
    demo_window.geometry("400x350")
    
    # Different input types
    tk.Label(demo_window, text="Advanced Input Examples", font=("Arial", 14, "bold")).pack(pady=10)
    
    # Regular text entry
    tk.Label(demo_window, text="Text Input:").pack()
    text_entry = tk.Entry(demo_window, width=30)
    text_entry.pack(pady=5)
    
    # Password entry (shows * instead of characters)
    tk.Label(demo_window, text="Password Input:").pack()
    password_entry = tk.Entry(demo_window, width=30, show="*")
    password_entry.pack(pady=5)
    
    # Multiline text input
    tk.Label(demo_window, text="Multiline Text:").pack()
    multiline_text = tk.Text(demo_window, height=4, width=40)
    multiline_text.pack(pady=5)
    
    # Display results function
    def show_inputs():
        results = f"""Text: {text_entry.get()}
Password: {'*' * len(password_entry.get())}
Multiline: {multiline_text.get('1.0', tk.END).strip()}"""
        result_label.config(text=results)
    
    # Button to show all inputs
    tk.Button(demo_window, text="Show Inputs", command=show_inputs).pack(pady=10)
    
    # Result display
    result_label = tk.Label(demo_window, text="Results will appear here", 
                           justify=tk.LEFT, anchor="w")
    result_label.pack(pady=10, padx=10, fill=tk.X)
    
    demo_window.mainloop()


if __name__ == "__main__":
    print("Starting Exercise 3.2 - GUI with Input")
    print("This GUI includes:")
    print("- Entry widget for user input")
    print("- Text area with scrollbar")
    print("- Interactive buttons that respond to input")
    print("-" * 50)
    
    main()
    
    # Uncomment to see advanced input demo
    # create_advanced_input_demo()


# This is part 2 of Exercise 3 (GUI Programming)
# Previous: exercise03_01_basic_gui.py (basic labels, buttons, frames)
# Next: exercise03_03_prime_checker_gui.py (complete prime checker application)