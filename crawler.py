from bs4 import BeautifulSoup
import requests

base_url = "https://www.digistyle.com/plp/plp_29733814/?pageno=4"
res = requests.get(base_url)

crawled_data = BeautifulSoup(res.text, "html.parser")
data = crawled_data.find_all("div", {"class": "cp-card cp-card--product-card js-cro-product"})

print(data)