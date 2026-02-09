from tkinter import ttk


FIELDS = (
    ("name", "Imię"),
    ("age", "Wiek"),
    ("email", "Email"),
    ("city", "Miasto"),
)


def build_form(parent) -> dict:
    frame = ttk.LabelFrame(parent, text="Dane wejściowe")
    frame.columnconfigure(1, weight=1)
    entries = {}
    for row, (key, label) in enumerate(FIELDS):
        ttk.Label(frame, text=label).grid(row=row, column=0, sticky="w", padx=8, pady=6)
        entry = ttk.Entry(frame)
        entry.grid(row=row, column=1, sticky="ew", padx=8, pady=6)
        entries[key] = entry
    return {"frame": frame, "entries": entries}
