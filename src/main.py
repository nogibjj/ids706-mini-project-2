import pandas as pd
from typing import Union, Dict

def describe_data(data: Union[pd.DataFrame, Dict]) -> pd.DataFrame:
    """Returns the descriptive statistics of the dataset."""
    
    if isinstance(data, Dict):
        data = pd.DataFrame(data)
    
    return data.describe()

if __name__ == "__main__":

    sample_data = {
        "A": [1, 2, 3, 4, 5],
        "B": [5, 4, 3, 2, 1],
        "C": [2, 3, 4, 3, 2]
    }
    df = pd.DataFrame(sample_data)
    print(describe_data(df))
