import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)


dates = pd.date_range('2023-01-01', periods=100, freq='D')
regions = ['North', 'South', 'East', 'West']
products = ['Product_A', 'Product_B', 'Product_C']

data = {
    'Date': np.random.choice(dates, 500),
    'Region': np.random.choice(regions, 500),
    'Product': np.random.choice(products, 500),
    'Sales': np.random.randint(1, 100, 500),
    'Revenue': np.random.uniform(100, 1000, 500)
}


df = pd.DataFrame(data)
print(df.head())
