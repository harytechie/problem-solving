import pandas as pd
import matplotlib.pyplot as plt

# Safe Windows path using raw string
file_path = r"D:\py class\data visualization\addresses.csv"

try:
    # 1. Load the CSV file
    df = pd.read_csv(file_path)
    
    # Clean up column names (removes hidden spaces or mismatched casing)
    df.columns = df.columns.str.strip()
    
    print("\n--- SUCCESSFULLY FOUND COLUMNS ---")
    print(list(df.columns))
    print("------------------------------------\n")

    # 2. Check for common 'addresses.csv' formats and plot dynamically
    plt.figure(figsize=(10, 5))
    
    # Scenario A: If it's a standard address file with a State or City distribution
    if 'State' in df.columns:
        df['State'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Distribution of Addresses by State')
        plt.xlabel('State')
        plt.ylabel('Count')
        
    elif 'City' in df.columns:
        df['City'].value_counts().plot(kind='bar', color='salmon', edgecolor='black')
        plt.title('Distribution of Addresses by City')
        plt.xlabel('City')
        plt.ylabel('Count')
        
    # Scenario B: If your file still uses custom numerical fields but has different names
    else:
        # Fallback: Just plot the first available column against the second column
        x_col = df.columns[0]
        y_col = df.columns[1]
        plt.plot(df[x_col], df[y_col], marker='o', color='purple')
        plt.title(f'{y_col} vs {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # 3. Force open the chart window
    print("Opening chart window...")
    plt.show()

except FileNotFoundError:
    print(f"Error: Could not find the file at: {file_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
