import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.resizable(True, True)
entry=tk.Entry(root, width=16, font=("Segoe UI", 24),bg="white", bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)
def press(v):
    entry.insert(tk.END, v)
def clear():
    entry.delete(0, tk.END)
def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")        
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
]
r=1
c=0
for b in buttons:
    cmd=calc if b=="=" else lambda x=b: press(x)
    tk.Button(root, text=b, width=5, height=2, font=("Segoe UI", 14), bg="Orange" if b in "+-*/=" else "Dark Gray", fg="white", bd=0, command=cmd).grid(row=r, column=c, padx=6, pady=6)
    c+=1
    if c==4:
        c=0
        r+=1
tk.Button(root, text="C", width=22, height=2, font=("Segoe UI", 14), bg="Red", fg="white", bd=0, command=clear).grid(row=r, column=0, columnspan=4, pady=8)
root.mainloop()    