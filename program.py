import tkinter as tk
from controller import*

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Download Videos Youtube')
    app = Controller(root)
    root.mainloop()