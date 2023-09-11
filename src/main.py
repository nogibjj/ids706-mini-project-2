import os
import pandas as pd
import matplotlib.pyplot as plt

def read_dataset(file_path: str) -> pd.DataFrame:
    
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type")
    
    return data

def generate_summary_statistics(data: pd.DataFrame) -> dict:

    if data is None or data.empty:
        raise ValueError("Data cannot be None or empty")

    summary = {
        "mean": data.mean().to_dict(),
        "median": data.median().to_dict(),
        "std_dev": data.std().to_dict()
    }

    return summary

def create_data_visualization(data: pd.DataFrame, file_path: str = 'data_visualization.png') -> None:

    if data is None or data.empty:
        raise ValueError("Data cannot be None or empty")

    data.hist()
    plt.savefig(file_path)


def save_summary_to_markdown(summary, file_path='output/summary.md'):
    with open(file_path, 'w') as f:
        for key, value in summary.items():
            f.write(f"## {key.capitalize()}\n")
            for sub_key, sub_value in value.items():
                f.write(f"- {sub_key}: {sub_value}\n")
        f.write("\n")
        
if __name__ == "__main__":
    output_dir = './output'
    os.makedirs(output_dir, exist_ok=True)
    data = read_dataset('./winequality-red.csv') 
    summary = generate_summary_statistics(data)
    create_data_visualization(data, './output/data_visualization.png')
    save_summary_to_markdown(summary, './output/summary.md')
