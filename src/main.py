import pandas as pd
import matplotlib.pyplot as plt

def read_dataset(file_path):
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type")
    
    return data

def generate_summary_statistics(data):
    mean = data.mean()
    median = data.median()
    std_dev = data.std()

    with open('summary_report.md', 'w') as f:
        f.write(f"# Summary Report\n")
        f.write(f"## Mean\n{mean}\n")
        f.write(f"## Median\n{median}\n")
        f.write(f"## Standard Deviation\n{std_dev}\n")

def create_data_visualization(data):
    data.hist()
    plt.savefig('data_visualization.png')
