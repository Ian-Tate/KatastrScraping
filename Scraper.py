from bs4 import BeautifulSoup
import requests

def fill_first_form(self, insert):
    payload = {'ctl00$bodyPlaceHolder$vyberObecKU$vyberKU$txtKU': insert}
    r = requests.get(self, params=payload)
    print (r.status_code)
    #with open("requests_results.html", "wb") as f:
    #    f.write(r.content)
    return r


def scrap_seznam_nemovitosti(self):
    r = requests.get(self)
    print(r)
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.findAll(class_="zarovnat stinuj ")  # MÁM TĚ !!! TOHLE VYPÍŠE TU SPRÁVNOU TABULKU
    #print(table)
    return table


