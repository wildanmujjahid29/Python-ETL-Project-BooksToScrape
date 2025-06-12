import pandas as pd

from utils.scraper import scrape_books
from utils.transform import transform_data, transform_to_DataFrame
from utils.load import save_to_csv, save_to_mysql

def main():
    BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
    books_data = scrape_books(BASE_URL)
    df_raw = transform_to_DataFrame(books_data)
    df_raw.to_csv("data/books_kotor.csv", index=False)
    print("======================================")
    print("Berhasil mengambil data buku:", df_raw.shape[0] , "data buku")
    print(df_raw)
    print("======================================")
    print("Melakukan Transformasi data...")
    df_clean = transform_data(df_raw)
    print("Berhasil Transformasi Data")
    print(df_clean)
    print("======================================")
    print("Menyimpan Data........................")
    save_to_csv(df_clean)
    save_to_mysql(df_clean, table_name='buku_data')
    
if __name__ == "__main__":
    main()
