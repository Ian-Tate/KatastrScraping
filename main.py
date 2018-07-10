import Scraper

url = "http://nahlizenidokn.cuzk.cz/ZobrazObjekt.aspx?encrypted=TpAPYChmh9dJYLP1ld3eLnekI72grEUiRKbm4ltAxuR6Dc7OFq_BhT9_uz1MAXZ3wmCXL-P46sXgAN1tu3jE8YBxpn6sMEQOOKI3rlfX5OQOWNamowDing=="

table = Scraper.scrap_seznam_nemovitosti(url)
print(table)
