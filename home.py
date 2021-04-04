"créer methode pour boucler sur toutes les categories"

import requests
from bs4 import BeautifulSoup
from category import Category

class Home:
    def __init__(self, website_url):
        self.url = website_url
        self.categories_url = list()


    def fetch_categories_url(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "lxml")
        for links in soup.findAll("a")[3:53]:
            self.categories_url.append("http://books.toscrape.com/" + links.get("href"))

    def run(self):
        for url in self.categories_url:
            """Pour chaque URL des URL de catégories"""
            category = Category(url)
            """Définition de la variable category"""
            category.handle()
            """Va chercher les Url d'une catégorie"""
            category.run()
            """Parse les informations de chaque livre de la catégorie"""









