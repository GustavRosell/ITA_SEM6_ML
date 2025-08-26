"""
Exercise 3.1: Basic GUI with Tkinter - Labels, Buttons, and Frames

This exercise demonstrates:
- Creating a basic tkinter window (similar to Windows Forms in C#)
- Adding labels and buttons to the interface
- Using frames to organize UI elements (like panels in C#)
- Button event handling with command functions

For C# developers: tkinter is Python's built-in GUI library, similar to WinForms.
Frame ~ Panel, Label ~ Label, Button ~ Button, but syntax is quite different.
"""

import tkinter as tk


def change_text():
    """
    Event handler for the "Change Text" button.
    Similar to button click event handlers in C# WinForms.
    """
    # Change the main label text when button is clicked
    welcome_label.config(text="Du har trykket på change knappen!\n")


def main():
    """
    Creates and displays the main GUI window.
    Demonstrates basic tkinter setup and widget organization.
    """
    # Create the main window (like Form in C#)
    global root, welcome_label  # Make these accessible to other functions
    root = tk.Tk()
    root.title("Exercise 3.1 - Basic GUI")
    root.geometry("400x300")  # Set window size
    
    # Create a frame to organize our widgets (like Panel in C#)
    # This makes it easier to manage layout when we have multiple UI elements
    main_frame = tk.Frame(root)
    main_frame.pack(pady=20)  # Add some padding around the frame
    
    # Create the main welcome label
    global welcome_label
    welcome_label = tk.Label(
        main_frame, 
        text="Hej, velkommen til mit program\n\n\n",
        font=("Arial", 12)
    )
    welcome_label.pack()
    
    # Create the QUIT button with red text
    quit_button = tk.Button(
        main_frame,
        text="QUIT",
        fg="red",  # Foreground color (text color)
        font=("Arial", 10, "bold"),
        command=quit  # Built-in quit function
    )
    quit_button.pack(pady=(10, 5))  # Add vertical padding
    
    # Create the "Change Text" button
    change_button = tk.Button(
        main_frame,
        text="Change text",
        font=("Arial", 10),
        command=change_text  # Our custom function
    )
    change_button.pack()
    
    # Start the GUI event loop (like Application.Run() in C#)
    root.mainloop()


def demonstrate_widget_properties():
    """
    Creates a second window to demonstrate different widget properties.
    Educational example showing various tkinter options.
    """
    demo_window = tk.Tk()
    demo_window.title("Widget Properties Demo")
    demo_window.geometry("350x250")
    
    # Different label styles
    title_label = tk.Label(
        demo_window,
        text="Different Widget Styles",
        font=("Arial", 14, "bold"),
        bg="lightblue",  # Background color
        fg="darkblue"    # Text color
    )
    title_label.pack(pady=10)
    
    # Different button styles
    style_frame = tk.Frame(demo_window)
    style_frame.pack(pady=10)
    
    # Button with background color
    colored_button = tk.Button(
        style_frame,
        text="Colored Button",
        bg="lightgreen",
        fg="darkgreen",
        font=("Arial", 10, "bold")
    )
    colored_button.pack(pady=5)
    
    # Button with different size
    large_button = tk.Button(
        style_frame,
        text="Large Button",
        font=("Arial", 12),
        width=15,
        height=2
    )
    large_button.pack(pady=5)
    
    # Information label
    info_label = tk.Label(
        demo_window,
        text="This demonstrates various tkinter widget properties.\nClose this window to continue.",
        font=("Arial", 9),
        justify=tk.CENTER
    )
    info_label.pack(pady=20)
    
    demo_window.mainloop()


if __name__ == "__main__":
    print("Starting Exercise 3.1 - Basic GUI")
    print("This will open a GUI window with labels and buttons.")
    print("Click the buttons to see how event handling works.")
    print("-" * 50)
    
    main()
    
    # Optionally run the demo (uncomment next line to see it)
    # demonstrate_widget_properties()


# This is part 1 of Exercise 3 (GUI Programming)
# Next: exercise03_02_gui_input.py (adding user input with Entry widgets)
# Final: exercise03_03_prime_checker_gui.py (complete prime checker application)