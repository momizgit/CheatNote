try:
    import tkinter as tk  # using Python 3
    from tkinter import ttk
except ImportError:
    import Tkinter as tk  # falls back to import from Python 2


root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Label(frm, text="c1r1").grid(column=100, row=1)
tk.mainloop()