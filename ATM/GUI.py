import tkinter as tk
from tkinter import messagebox

PIN = "123456"
balance = 1000

root = tk.Tk()
root.title("ATM System")
root.geometry("300x350")
root.resizable(False, False)

def login():
    if pin_entry.get() == PIN:
        login_frame.pack_forget()
        menu_frame.pack()
    else:
        messagebox.showerror("Error", "Incorrect PIN")

def check_balance():
    messagebox.showinfo("Balance", f"Your balance is ${balance}")

def deposit():
    global balance
    amount = amount_entry.get()
    if amount.isdigit():
        balance += int(amount)
        messagebox.showinfo("Success", "Deposit successful")
    else:
        messagebox.showerror("Error", "Invalid amount")
    amount_entry.delete(0, tk.END)

def withdraw():
    global balance
    amount = amount_entry.get()
    if amount.isdigit() and int(amount) <= balance:
        balance -= int(amount)
        messagebox.showinfo("Success", "Withdrawal successful")
    else:
        messagebox.showerror("Error", "Invalid or insufficient balance")
    amount_entry.delete(0, tk.END)

def logout():
    menu_frame.pack_forget()
    login_frame.pack()
    pin_entry.delete(0, tk.END)

login_frame = tk.Frame(root)
login_frame.pack(pady=40)

tk.Label(login_frame, text="Enter PIN", font=("Arial", 14)).pack(pady=10)
pin_entry = tk.Entry(login_frame, show="*", font=("Arial", 14))
pin_entry.pack()

tk.Button(login_frame, text="Login", width=15, command=login).pack(pady=10)

menu_frame = tk.Frame(root)

tk.Label(menu_frame, text="ATM Menu", font=("Arial", 14)).pack(pady=10)

tk.Button(menu_frame, text="Check Balance", width=20, command=check_balance).pack(pady=5)

tk.Label(menu_frame, text="Enter amount:", font=("Arial", 12)).pack(pady=10)

amount_entry = tk.Entry(menu_frame, font=("Arial", 12))
amount_entry.pack(pady=5)

tk.Button(menu_frame, text="Deposit", width=20, command=deposit).pack(pady=5)
tk.Button(menu_frame, text="Withdraw", width=20, command=withdraw).pack(pady=5)
tk.Button(menu_frame, text="Logout", width=20, command=logout).pack(pady=10)

root.mainloop()
