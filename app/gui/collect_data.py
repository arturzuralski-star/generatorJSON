
def collect_data(entries: dict) -> dict:
    data = {}
    for key, entry in entries.items():
        value = entry.get().strip()
        if key == "age":
            data[key] = int(value) if value.isdigit() else value
        else:
            data[key] = value
    return data
