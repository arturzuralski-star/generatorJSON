from tkinter import ttk


def build_output(parent) -> dict:
    frame = ttk.LabelFrame(parent, text="Wynik JSON")
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    scrollbar = ttk.Scrollbar(frame, orient="vertical")
    text = ttk.Text(frame, height=10, wrap="none", yscrollcommand=scrollbar.set)
    scrollbar.config(command=text.yview)

    text.grid(row=0, column=0, sticky="nsew", padx=(8, 0), pady=8)
    scrollbar.grid(row=0, column=1, sticky="ns", padx=(0, 8), pady=8)

    return {"frame": frame, "text": text}
