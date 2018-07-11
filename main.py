import Scraper
import requests
import webbrowser
from bs4 import BeautifulSoup

url = "http://nahlizenidokn.cuzk.cz/VyberLV.aspx"
url1 = "http://nahlizenidokn.cuzk.cz/ZobrazObjekt.aspx?encrypted=TpAPYChmh9dJYLP1ld3eLnekI72grEUiRKbm4ltAxuR6Dc7OFq_BhT9_uz1MAXZ3wmCXL-P46sXgAN1tu3jE8YBxpn6sMEQOOKI3rlfX5OQOWNamowDing=="

payloadOne = {'ctl00$bodyPlaceHolder$vyberObecKU$vyberKU$txtKU': 600016}
payloadTwo = {'ctl00$bodyPlaceHolder$txtLV': 1}
s = requests.Session()
r = s.post(url, params=payloadOne)
print(r.status_code)

ra = s.post(url, params=payloadTwo)
print(ra.status_code)



table = Scraper.scrap_seznam_nemovitosti(url1)
print(table)
