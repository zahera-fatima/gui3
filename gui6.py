import tkinter as tk 
from tkinter import ttk
win = tk.Tk()
win.title('Menubar')
def func():
    print('func called')
# menubar = tk.Menu(win)
# menubar.add_command(label='Save', command=func)
# menubar.add_command(label='Save as', command=func)
# menubar.add_command(label='copy', command=func)
# menubar.add_command(label='paste', command=func)

main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New file', command=func)
file_menu.add_command(label='Open', command=func)
file_menu.add_separator()
file_menu.add_command(label='save', command=func)
file_menu.add_command(label='Save as', command=func)
Edit_menu = tk.Menu(main_menu, tearoff=0)
Edit_menu.add_command(label='undo', command=func)
Edit_menu.add_command(label='redo', command=func)
main_menu.add_cascade(label='file', menu=file_menu)
main_menu.add_cascade(label='edit', menu=Edit_menu)


win.config(menu=main_menu)


win.mainloop()