from tkinter import ttk

from gui.apply_defaults import apply_defaults
from gui.build_form import build_form
from gui.build_output import build_output
from gui.build_root import build_root
from gui.on_generate import on_generate
from gui.on_save import on_save


def main() -> None:
    root = build_root()

    container = ttk.Frame(root, padding=12)
    container.pack(fill="both", expand=True)
    container.columnconfigure(0, weight=1)
    container.rowconfigure(1, weight=1)

    header = ttk.Label(container, text="Generator JSON", font=("Arial", 16, "bold"))
    header.grid(row=0, column=0, sticky="w", pady=(0, 12))

    form_info = build_form(container)
    form_frame = form_info["frame"]
    entries = form_info["entries"]
    form_frame.grid(row=1, column=0, sticky="nsew")

    output_info = build_output(container)
    output_frame = output_info["frame"]
    output_text = output_info["text"]
    output_frame.grid(row=2, column=0, sticky="nsew", pady=(12, 0))

    actions = ttk.Frame(container)
    actions.grid(row=3, column=0, sticky="e", pady=(12, 0))

    ttk.Button(actions, text="Generuj", command=lambda: on_generate(entries, output_text)).grid(
        row=0, column=0, padx=6
    )
    ttk.Button(actions, text="Zapisz", command=lambda: on_save(output_text)).grid(
        row=0, column=1, padx=6
    )

    apply_defaults(entries)

    root.mainloop()


if __name__ == "__main__":
    main()
