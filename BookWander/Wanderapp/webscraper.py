# Wanderapp/webscraper.py

import requests
from bs4 import BeautifulSoup

def scrape_amazon_books():
    """
    Scrape information about books from the amazonebooks.com website.

    This function sends an HTTP request to the specified URL,
    extracts information about books, and prints the title and author.

    Returns:
    None
    """
    url = 'https://www.amazonebooks.com'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Add your logic here to extract information from the website

        # Example: Print the title and author of the books
        for book_info in soup.find_all('div', class_='book-info'):
            title = book_info.find('h2', class_='book-title').text.strip()
            author = book_info.find('p', class_='book-author').text.strip()

            print(f"Title: {title}, Author: {author}")

    else:
        print(f"Error during HTTP request: {response.status_code}")

# Call the function to test
if __name__ == "__main__":
    scrape_amazon_books()
