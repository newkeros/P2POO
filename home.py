"créer methode pour boucler sur toutes les categories"

import requests
from bs4 import BeautifulSoup
from book import Book
from category import Category

class Home:
    def __init__(self, url):
        self.url = url
        self.categories_url = list()


    def categories_url(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "lxml")
        for links in soup.findAll("a")[3:53]:
            self.categories_url.append("http://books.toscrape.com/" + links.get("href"))

    def run(self):
        for url in self.categories_url:
            category = Category(url)
            book = Book(url)
            category.handle()
            book.handle_book()
            book.print_book()


home_url = Home("http://books.toscrape.com/")
home_url.run()





