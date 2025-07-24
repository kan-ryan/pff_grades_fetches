import csv


def export_to_csv(data, filename):
    if not data:
        print("No data to export.")
        return

    # Compute union of all keys across all dicts
    all_keys = set()
    for row in data:
        all_keys.update(row.keys())
    fieldnames = sorted(all_keys)  # consistent column order

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
