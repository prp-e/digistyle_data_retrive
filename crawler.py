from bs4 import BeautifulSoup
import requests
import time

products = []
for i in range(10):
    base_url = f"https://www.digistyle.com/plp/plp_29733814/?pageno={i + 1}"
    res = requests.get(base_url)

    crawled_data = BeautifulSoup(res.text, "html.parser")
    data = crawled_data.find_all("div", {"class": "cp-card cp-card--product-card js-cro-product"})

    for datum in data:
        picture = datum.find("img", {"class": "c-product-card__image"})["src"]
        url = datum.find("a", {"c-product-card__image-container ga-product-impression"})["href"]
        product = {
            "picture": picture,
            "url": f'https://www.digistyle.com{url}'
        }
        products.append(product)
    
    time.sleep(10)

print(products)