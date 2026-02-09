import json


def update_output(text_widget, data: dict) -> None:
    text_widget.delete("1.0", "end")
    text_widget.insert("1.0", json.dumps(data, ensure_ascii=False, indent=2))
