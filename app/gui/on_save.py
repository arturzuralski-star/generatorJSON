from tkinter import filedialog


def on_save(text_widget) -> None:
    content = text_widget.get("1.0", "end").strip()
    if not content:
        return
    file_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=(("JSON", "*.json"), ("Wszystkie pliki", "*.*")),
    )
    if not file_path:
        return
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)
