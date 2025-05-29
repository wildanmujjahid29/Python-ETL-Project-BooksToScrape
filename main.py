from utils.scraper import scrape_books 
import pandas as pd

def main():
    BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
    books_data = scrape_books(BASE_URL)
    df = pd.DataFrame(books_data)
    df.to_csv("data/books_kotor.csv", index=False)
    print("======================================")
    print("Berhasil mengambil data buku:", df.shape[0] , "data buku")
    print(df)
    print("======================================")
    print("Melakukan Transformasi data...")

if __name__ == "__main__":
    main()
