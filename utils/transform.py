import pandas as pd
import numpy as np

def transform_to_DataFrame(data):
    """
    Mengubah data yang diekstrak menjadi DataFrame pandas.
    """
    # Mengubah list of dictionaries menjadi DataFrame
    df = pd.DataFrame(data)
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    """Fungsi untuk transformasi data"""
    
    # Menghapus missing values
    df = df.dropna()
    
    # Menghapus duplikasi Data
    df = df.drop_duplicates()
    
    # Konvesi mata uang
    def convert_price(price_str):
        try:
            price = float(price_str.replace('£', '').replace(',', ''))
            return int(price * 18402.00)
        except:
            return np.nan
        
    df['Price'] = df['Price'].apply(convert_price)
    
    # Ubah rating ke angka
    def map_rating(rating_str):
        mapping = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        return mapping.get(rating_str, np.nan)

    df['Rating'] = df['Rating'].apply(map_rating)
    
    return df