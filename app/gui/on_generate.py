from .collect_data import collect_data
from .update_output import update_output


def on_generate(entries: dict, text_widget) -> None:
    data = collect_data(entries)
    update_output(text_widget, data)
