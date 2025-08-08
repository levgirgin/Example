import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
def division(a, b):
        return a/b

def addition(a, b):
        return a + b