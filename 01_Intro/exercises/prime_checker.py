import tkinter as tk

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime():
    try:
        number = int(entry.get())
        if is_prime(number):
            result_label.config(text=f"{number} is prime")
        else:
            result_label.config(text=f"{number} is not prime")
    except:
        result_label.config(text="Enter a valid number")

root = tk.Tk()
root.title("Prime Checker")

tk.Label(root, text="Enter number:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check", command=check_prime).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()