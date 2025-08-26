"""
Exercise 2.2: List Operations - Append, Delete, and Length

This exercise demonstrates:
- Adding elements to lists with append() (like List.Add() in C#)
- Removing elements by index (like List.RemoveAt() in C#)
- Getting list length with len() (like List.Count in C#)
- Printing lists before and after modifications

For C# developers: Python's append() = C#'s Add(), del list[index] = RemoveAt(index),
len(list) = list.Count
"""


def main():
    """
    Demonstrates list modification operations.
    Shows the dynamic nature of Python lists compared to C# arrays.
    """
    # Start with our list of 5 authors from previous exercise
    forfattere = ["Tolkien", "Rowling", "King", "Orwell", "Hemingway"]
    
    print("Original list of 5 authors:")
    print_numbered_list(forfattere)
    
    # Add a new author with append (like authors.Add("Asimov") in C#)
    print("\n--- Adding a new author with append() ---")
    forfattere.append("Asimov")
    
    print("After adding Asimov:")
    print_numbered_list(forfattere)
    
    # Remove author #2 (index 1, since Python is 0-indexed)
    # This will remove "Rowling" to get back to 5 authors
    print("\n--- Removing author #2 (Rowling) ---")
    del forfattere[1]  # In C#: authors.RemoveAt(1)
    
    print("After removing author #2:")
    print_numbered_list(forfattere)
    
    # Get and display the length of the list
    print("\n--- Getting list length ---")
    list_length = len(forfattere)  # In C#: int length = authors.Count
    print(f"Current number of authors: {list_length}")
    
    # Store length in variable as requested in exercise
    antal_forfattere = len(forfattere)
    print(f"Stored in variable 'antal_forfattere': {antal_forfattere}")


def print_numbered_list(authors_list):
    """
    Helper function to print a list with numbers.
    Makes the output cleaner and more readable.
    
    Args:
        authors_list: List of author names to print
    """
    for i, author in enumerate(authors_list, 1):  # Start counting from 1
        print(f"{i}. {author}")


def demonstrate_different_removal_methods():
    """
    Additional demonstration of different ways to remove items from lists.
    Educational comparison with C# removal methods.
    """
    print("\n" + "="*50)
    print("BONUS: Different ways to remove items from lists")
    print("="*50)
    
    test_list = ["A", "B", "C", "D", "E"]
    print(f"Original: {test_list}")
    
    # Method 1: del by index (like RemoveAt in C#)
    test_list1 = test_list.copy()
    del test_list1[2]  # Removes "C"
    print(f"After del test_list[2]: {test_list1}")
    
    # Method 2: remove by value (like Remove in C#)
    test_list2 = test_list.copy()
    test_list2.remove("C")  # Removes first occurrence of "C"
    print(f"After remove('C'): {test_list2}")
    
    # Method 3: pop (removes and returns item)
    test_list3 = test_list.copy()
    removed_item = test_list3.pop(2)  # Removes and returns "C"
    print(f"After pop(2): {test_list3}, removed: {removed_item}")


if __name__ == "__main__":
    main()
    demonstrate_different_removal_methods()


# This is part 2 of Exercise 2
# Previous: exercise02_01_basic_lists.py (basic lists and loops)
# Next: exercise02_03_list_reverse.py (reverse operations)