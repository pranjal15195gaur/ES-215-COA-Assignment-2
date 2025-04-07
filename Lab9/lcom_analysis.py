import csv
from tabulate import tabulate

def fetch_high_lcom_classes(csv_path, threshold=10.0):
    """Extracts classes with high LCOM values from the CSV file."""
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [
            (
                row["Type Name"],
                *map(float, (row["LCOM1"], row["LCOM2"], row["LCOM3"], row["LCOM4"], row["LCOM5"])),
                row["YALCOM"],
                sum(map(float, (row["LCOM1"], row["LCOM2"], row["LCOM3"], row["LCOM4"], row["LCOM5"]))) / 5
            )
            for row in reader if sum(map(float, (row["LCOM1"], row["LCOM2"], row["LCOM3"], row["LCOM4"], row["LCOM5"]))) / 5 > threshold
        ]

def display_analysis(high_lcom_classes):
    """Displays analysis results and recommendations."""
    print("LCOM Cohesion Analysis Report\n")
    print("Classes with high LCOM values exhibit weak cohesion, implying a potential violation of the Single Responsibility Principle.")
    print("Consider refactoring these classes to enhance modularity and maintainability.\n")

    headers = ["Class Name", "LCOM1", "LCOM2", "LCOM3", "LCOM4", "LCOM5", "YALCOM", "(Avg)"]
    table_data = [
        [cls, f"{l1:.2f}", f"{l2:.2f}", f"{l3:.2f}", f"{l4:.2f}", f"{l5:.2f}", yalcom, f"({avg:.2f})"]
        for cls, l1, l2, l3, l4, l5, yalcom, avg in high_lcom_classes
    ]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    print("\nAffected Classes:")
    for cls, *_ in high_lcom_classes:
        print(f"- {cls}")

def main():
    csv_path = "output/TypeMetrics.csv"
    high_lcom_classes = fetch_high_lcom_classes(csv_path)
    if high_lcom_classes:
        display_analysis(high_lcom_classes)
    else:
        print("No classes exceed the specified LCOM threshold.")

if __name__ == "__main__":
    main()

