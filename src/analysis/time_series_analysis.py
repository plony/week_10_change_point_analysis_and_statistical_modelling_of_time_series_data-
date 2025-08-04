import pandas as pd
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df: pd.DataFrame, title: str):
    """
    Plots the time series data.
    
    Args:
        df (pd.DataFrame): The DataFrame with time series data.
        title (str): The title of the plot.
    """
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(15, 7))
    df['Price'].plot()
    plt.title(title, fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD per barrel)', fontsize=12)
    plt.tight_layout()
    plt.show()

def check_stationarity(df: pd.DataFrame):
    """
    Performs the Augmented Dickey-Fuller test to check for stationarity.
    
    Args:
        df (pd.DataFrame): The DataFrame with the 'Price' column.
    """
    print("Running Augmented Dickey-Fuller Test...")
    result = adfuller(df['Price'].dropna())
    
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    print('Critical Values:')
    for key, value in result[4].items():
        print(f'\t{key}: {value}')
        
    if result[1] <= 0.05:
        print("\nConclusion: The p-value is small (<= 0.05), so we reject the null hypothesis.")
        print("This suggests the time series is likely stationary.")
    else:
        print("\nConclusion: The p-value is large (> 0.05), so we fail to reject the null hypothesis.")
        print("This suggests the time series has a unit root and is likely non-stationary.")