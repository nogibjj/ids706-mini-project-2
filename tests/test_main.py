import pandas as pd
from src.main import read_dataset, generate_summary_statistics

def test_read_dataset():

    data = read_dataset('test.csv')
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

    try:
        read_dataset('test.txt')
        assert False, "Expected ValueError, but got no error"
    except ValueError as e:
        assert str(e) == "Unsupported file type"

def test_generate_summary_statistics():
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    summary = generate_summary_statistics(data)
    
    assert summary['mean']['a'] == 2.0
    assert summary['median']['b'] == 5.0

    try:
        generate_summary_statistics(pd.DataFrame())
        assert False, "Expected ValueError, but got no error"
    except ValueError as e:
        assert str(e) == "Data cannot be None or empty"
