from bs4 import BeautifulSoup
import requests

base_url = "https://www.digistyle.com/plp/plp_29733814/?pageno=4"
res = requests.get(base_url)

print(res.text)