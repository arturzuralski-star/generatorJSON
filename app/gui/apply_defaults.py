from .default_data import default_data


def apply_defaults(entries: dict) -> None:
    data = default_data()
    for key, entry in entries.items():
        if key in data:
            entry.delete(0, "end")
            entry.insert(0, data[key])
