from requests import request
from bs4 import BeautifulSoup


class Book:
    def __init__(self, url):
        self.url = url
        self.image_url = ""
        self.review_rating = ""
        self.category = ""
        self.number_available = ""
        self.price_without_tax = ""
        self.price_including_tax = ""
        self.description = ""
        self.upc = ""
        self.title = ""

    def handle_book(self):
        response = request.get(self.url)
        if response.ok:
            response.encoding = "utf-8"
            self.soup = BeautifulSoup(response.text, "lxml")

            self.image_url = self.get_image_url()
            self.review_rating = self.get_review_rating()
            self.category = self.get_category()
            self.number_available = self.get_number_available()
            self.price_without_tax = self.get_price_excluding_tax()
            self.price_including_tax = self.get_price_including_tax()
            self.description = self.get_product_description()
            self.upc = self.get_upc()
            self.title = self.get_title()


    def get_title(self):
        title_scrapping = self.soup.find("div", class_="col-sm-6 product_main").h1.text
        return title_scrapping

    def get_upc(self):
        tr = self.soup.select("tr")
        return tr[0].td.text

    def get_product_description(self):
        description = self.soup.select("p")
        return description[3].text

    def get_price_including_tax(self):
        price_without_tax = self.soup.select("tr")
        return price_without_tax[3].td.text

    def get_price_excluding_tax(self):
        price_without_tax = self.soup.select("tr")
        return price_without_tax[2].td.text

    def get_number_available(self):
        number_available = self.soup.select("p")
        return number_available[1].text.strip().strip(" Instock)available(")

    def get_category(self):
        category = self.soup.ul.find_all("a")[-1].text
        return category

    def get_review_rating(self):
        review_rating = self.soup.find_all("p")[2]
        return review_rating.get("class")[-1]

    def get_image_url(self):
        image_url = self.soup.find_all("img")[0]
        return image_url.get("src").replace("../../", "http://books.toscrape.com/")

    def print_book(self):
        print(f" Title : {self.title}\n UPC : {self.upc}\n Product description : {self.description}\n"
              f" Price including tax : {self.price_including_tax}\n Price excluding tax : {self.price_without_tax}\n "
              f"Number available : {self.number_available}\n Category : {self.category}\n Review rating : "
              f"{self.review_rating}\n Image URL : {self.image_url}\n ")


book1 = Book("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")

book1.print_book()
