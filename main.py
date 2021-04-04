from home import Home

if __name__ == "__main__":
    website_url = Home("http://books.toscrape.com/")
    website_url.fetch_categories_url()
    website_url.run()
