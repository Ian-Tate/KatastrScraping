from bs4 import BeautifulSoup
import requests

r = requests.get("http://nahlizenidokn.cuzk.cz/ZobrazObjekt.aspx?encrypted=pZP2c_C-4Zwi-o9i4RUYiWYST9VIFD3AGyMPkvcsXxpwZMzKzDqyojam9w2VguS1eGT-fFK06FDDdBL8vMeC6iB-8TWjftGkkMFnZaOZqFcwz7svERpbYQ==")
print(r)

soup = BeautifulSoup(r.text, "html.parser")


#print(soup.prettify())
print("************************** ZDE *****************************")
table = soup.findAll(class_="zarovnat stinuj ") #MÁM TĚ !!! TOHLE VYPÍŠE TU SPRÁVNOU TABULKU
print(table)






