from bs4 import BeautifulSoup
import requests


def scrap_seznam_nemovitosti(self):
    r = requests.get(self)
    print(r)
    soup = BeautifulSoup(r.text, "html.parser")
    #print("************************** ZDE *****************************")
    table = soup.findAll(class_="zarovnat stinuj ")  # MÁM TĚ !!! TOHLE VYPÍŠE TU SPRÁVNOU TABULKU
    #print(table)
    return table
