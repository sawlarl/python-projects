import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Arial", 18),
    borderwidth=5,
    relief="ridge",
    justify="right"
)
entry.pack(fill="both", padx=10, pady=10)

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(0, str(result))
    except:
        clear()
        entry.insert(0, "Error")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for btn in buttons:
    if btn == "=":
        action = calculate
    else:
        action = lambda x=btn: click(x)

    tk.Button(
        frame,
        text=btn,
        width=5,
        height=2,
        font=("Arial", 14),
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    root,
    text="Clear",
    width=20,
    height=2,
    font=("Arial", 12),
    command=clear
).pack(pady=10)

root.mainloop()
