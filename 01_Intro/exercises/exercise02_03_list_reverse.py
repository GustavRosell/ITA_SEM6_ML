"""
Exercise 2.3: List Reverse Operations

This exercise demonstrates:
- Reversing a list with the reverse() method (modifies original list)
- Different ways to reverse lists in Python
- Understanding the difference between in-place and non-destructive operations

For C# developers: Python's list.reverse() modifies the original list (like Array.Reverse()),
while reversed() or slicing [::-1] creates a new reversed sequence.
"""


def main():
    """
    Demonstrates list reversal operations.
    Shows both destructive and non-destructive ways to reverse lists.
    """
    # Start with our authors list from previous exercises
    forfattere = ["Tolkien", "Rowling", "King", "Orwell", "Hemingway"]
    
    print("Original list of authors:")
    print_numbered_list(forfattere)
    
    # Method 1: reverse() - modifies the original list (destructive)
    print("\n--- Using reverse() method ---")
    print("This will permanently change the original list order!")
    
    forfattere.reverse()  # In C#: Array.Reverse(authors) or authors.Reverse()
    
    print("After using reverse():")
    print_numbered_list(forfattere)
    
    print(f"List is now permanently reversed: {forfattere}")


def demonstrate_different_reverse_methods():
    """
    Shows different ways to reverse lists in Python.
    Educational comparison of destructive vs non-destructive methods.
    """
    print("\n" + "="*50)
    print("BONUS: Different ways to reverse lists")
    print("="*50)
    
    original_list = ["A", "B", "C", "D", "E"]
    print(f"Original list: {original_list}")
    
    # Method 1: reverse() - modifies original (destructive)
    list1 = original_list.copy()
    list1.reverse()
    print(f"Method 1 - reverse(): {list1}")
    print(f"Original after reverse(): {original_list} (unchanged)")
    
    # Method 2: reversed() - returns iterator (non-destructive)
    list2 = list(reversed(original_list))
    print(f"Method 2 - reversed(): {list2}")
    print(f"Original after reversed(): {original_list} (unchanged)")
    
    # Method 3: slicing [::-1] - creates new list (non-destructive)
    list3 = original_list[::-1]
    print(f"Method 3 - slicing [::-1]: {list3}")
    print(f"Original after slicing: {original_list} (unchanged)")
    
    print("\nKey differences:")
    print("- reverse(): Modifies original list, returns None")
    print("- reversed(): Returns iterator, original unchanged")
    print("- [::-1]: Creates new list, original unchanged")


def print_numbered_list(authors_list):
    """
    Helper function to print a list with numbers.
    
    Args:
        authors_list: List of author names to print
    """
    for i, author in enumerate(authors_list, 1):  # Start counting from 1
        print(f"{i}. {author}")


def practical_example():
    """
    Practical example showing when you might want to reverse a list.
    """
    print("\n" + "="*50)
    print("PRACTICAL EXAMPLE: Processing items in reverse order")
    print("="*50)
    
    # Example: Processing a queue in LIFO order (Last In, First Out)
    task_queue = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]
    
    print("Processing tasks in reverse order (newest first):")
    
    # Create reversed copy for processing (non-destructive)
    reversed_tasks = task_queue[::-1]
    
    for i, task in enumerate(reversed_tasks, 1):
        print(f"Processing {i}: {task}")
    
    print(f"\nOriginal queue remains intact: {task_queue}")


if __name__ == "__main__":
    main()
    demonstrate_different_reverse_methods()
    practical_example()


# This completes Exercise 2 (parts 2.1, 2.2, 2.3)
# Previous: exercise02_02_list_operations.py (append, delete, length)
# Next: exercise03_01_basic_gui.py (GUI programming begins)