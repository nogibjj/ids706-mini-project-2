import pandas as pd
from src.main import describe_data

def test_describe_data():
    data = {
        "A": [1, 2, 3],
        "B": [3, 2, 1]
    }
    df = pd.DataFrame(data)
    
    result = describe_data(df)
    
    assert result.loc['mean', 'A'] == 2.0
    assert result.loc['mean', 'B'] == 2.0
    assert result.loc['min', 'A'] == 1.0
    assert result.loc['min', 'B'] == 1.0
