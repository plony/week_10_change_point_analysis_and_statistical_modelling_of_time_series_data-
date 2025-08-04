import pandas as pd

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    Loads the Brent oil price data from a CSV file and cleans it.
    
    Args:
        file_path (str): The path to the raw data CSV file.
    
    Returns:
        pd.DataFrame: A cleaned DataFrame with 'Date' as a datetime index
                      and 'Price' as a numeric column.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    
    df.columns = ['Date', 'Price']
    
    # Corrected line to handle mixed date formats
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='mixed')
    
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    
    df.dropna(subset=['Date', 'Price'], inplace=True)
    
    df.set_index('Date', inplace=True)
    
    df.sort_index(inplace=True)
    
    print("Data loaded and cleaned successfully.")
    print(df.head())
    print("\nDataFrame Info:")
    df.info()
    
    return df

if __name__ == '__main__':
    file_path = "../data/raw/BrentOilPrices.csv"
    brent_prices_df = load_and_clean_data(file_path)
    if brent_prices_df is not None:
        output_path = "../data/processed/brent_prices_cleaned.csv"
        brent_prices_df.to_csv(output_path)
        print(f"\nCleaned data saved to {output_path}")