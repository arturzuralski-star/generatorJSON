import tkinter as tk


def build_root(title: str = "Generator JSON") -> tk.Tk:
    root = tk.Tk()
    root.title(title)
    root.geometry("700x450")
    root.minsize(600, 400)
    return root
