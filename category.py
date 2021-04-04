import requests
from bs4 import BeautifulSoup
from book import Book

class Category:
    def __init__(self, url):
        self.url = url
        self.book_urls = list()



    def handle(self):
        base_url = self.url[:-10]
        next_flag = True
        i = 1
        while next_flag:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, "lxml")
            for link in soup.find_all("h3"):
                self.book_urls.append(
                    link.a.attrs["href"].replace(
                        "../../../", "http://books.toscrape.com/catalogue/"
                    )
                )
            next_flag = soup.find("li", {"class": "next"}) is not None
            i += 1
            self.url = base_url + "page-" + str(i) + ".html"

    def run(self):
        for url in self.book_urls:
            book = Book(url)
            book.handle_book()
            book.print_book()


historical_fiction = Category("https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html")
historical_fiction.handle()
historical_fiction.run()

"""récuperer tous les liens mettre dans une instance de listemethode run boucle sur tous les livres, créer book handle et print book"
handle qui recupere tous les liens des categories"""


"""créer methode create book qui aura pour role de creer toute les instances de book que je vais pouvoir mettre dans une une 
ou dans chaque cas j'aurais une instance de book (créer liste book dans le init) et autre run qui suit
(liste d'instances)"""