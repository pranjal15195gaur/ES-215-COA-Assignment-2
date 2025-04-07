import pandas as pd

def load_lcom_data(csv_path):
    """
    Load the LCOM CSV data.
    Expected columns: "Project Name", "Package Name", "Type Name",
                      "LCOM1", "LCOM2", "LCOM3", "LCOM4", "LCOM5", "YALCOM"
    """
    df = pd.read_csv(csv_path)
    return df

def print_top_high_lcom(df, metric="LCOM1", threshold=0.8, top_n=5):
    """
    Sort the dataframe by the specified LCOM metric (in descending order),
    then filter classes with LCOM > threshold and print the top_n classes.
    """
    # Filter by threshold, then sort descending by the metric.
    filtered = df[df[metric] > threshold].sort_values(by=metric, ascending=False)
    top_classes = filtered.head(top_n)
    
    if top_classes.empty:
        print(f"No classes found with {metric} > {threshold}.")
    else:
        print(f"Top {top_n} classes with high {metric} values (>{threshold}):")
        print(top_classes[["Project Name", "Package Name", "Type Name", metric]].to_string(index=False))

def main():
    csv_path = "output/TypeMetrics.csv"  # Ensure the CSV file is in your current directory.
    
    # Load the LCOM metrics data.
    lcom_data = load_lcom_data(csv_path)
    
    # Print top 5 classes sorted by LCOM1 with values greater than 0.8.
    print_top_high_lcom(lcom_data, metric="LCOM1", threshold=0.8, top_n=5)

if __name__ == "__main__":
    main()
