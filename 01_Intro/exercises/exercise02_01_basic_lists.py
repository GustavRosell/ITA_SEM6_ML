"""
Exercise 2.1: Basic Lists and For Loops

This exercise demonstrates:
- List creation and initialization (similar to arrays/Lists in C#)
- For loops with lists (simpler syntax than C# foreach)
- Printing each element on separate lines

For C# developers: Python lists are like List<T> but don't need type declarations.
The for loop syntax is much simpler: "for item in list" vs "foreach(var item in list)"
"""


def main():
    """
    Demonstrates basic list creation and iteration.
    Shows Python's simple approach to working with collections.
    """
    # Create a list of favorite authors (last names only)
    # In C#: List<string> authors = new List<string> {"Tolkien", "Rowling", "King", "Orwell", "Hemingway"};
    # Python is much simpler:
    forfattere = ["Tolkien", "Rowling", "King", "Orwell", "Hemingway"]
    
    print("My 5 favorite authors:")
    print("-" * 20)  # Print a separator line
    
    # For loop to print each author on their own line
    # Much simpler than C#'s for(int i = 0; i < authors.Count; i++)
    for forfatter in forfattere:
        print(forfatter)
    
    print("-" * 20)  # Print another separator
    print("List printed successfully!")


# Additional demonstration of different ways to work with lists
def demonstrate_list_access():
    """
    Shows different ways to access list elements.
    Educational function to compare with C# array/list access.
    """
    authors = ["Tolkien", "Rowling", "King", "Orwell", "Hemingway"]
    
    print("\nDemonstrating list access:")
    print(f"First author: {authors[0]}")      # Same as C#: authors[0]
    print(f"Last author: {authors[-1]}")      # Python special: negative indexing
    print(f"Second author: {authors[1]}")     # Same as C#: authors[1]
    
    # Print with index numbers (like C# for loop with counter)
    print("\nAuthors with numbers:")
    for i, author in enumerate(authors):  # enumerate() gives both index and value
        print(f"{i + 1}. {author}")


if __name__ == "__main__":
    main()
    demonstrate_list_access()


# Note: This is the first part of Exercise 2
# Next: exercise02_02_list_operations.py (append, delete, length)
# Then: exercise02_03_list_reverse.py (reverse operations)