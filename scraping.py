from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = "https://shop.coles.com.au/a/national/specials/search/coles-weekly-specials?pid=pr_Tile_SpecialsTab_Campaigns_Coles-Weekly-Specials"
driver = webdriver.Safari()
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content)

products = []
prices = []
savings = []

# get products name
for a in soup.find_all('span', {'class' : 'product-name'}):
    products.append(a.text)
# get prices info
for a in soup.find_all('span', {'class' : 'product-pricing-info'}):
    dollar = a.find('span', {'class' : 'dollar-value'})
    cent = a.find('span',  {'class' : 'cent-value'})
    price = dollar.text + cent.text
    prices.append(price)
# get the saving info
for a in soup.find_all('span', {'class' : 'product-save-value'}):
    savings.append(a.text)

# export data to a csv file
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Savings': savings})
df.to_csv('/Users/june/Desktop/coles-weekly-specials.csv', index = False, encoding='utf-8')

driver.close()

