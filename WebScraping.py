import bs4
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd     

link='https://www.flipkart.com/search?q=shoes&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=TRENDING&suggestionId=shoes&requestId=c1bd7653-6d99-457c-8ea0-4d81ea4911ca'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

page = requests.get(link, headers=headers)
# print(page.content)
soup = bs(page.content, 'html.parser')
# print(soup.prettify())
# name=soup.find('div', class_="Fo1I0b")
# print(name.text)
# original_price=soup.find('div', class_="kRYCnD")
# print(original_price.text)
# offered_price=soup.find('div', class_="hZ3P6w")
# print(offered_price.text)
# discount_percentage=soup.find('div', class_="HQe8jr")
# print(discount_percentage.text)

names=[]
original_prices=[]
offered_prices=[]   
discount_percentages=[]
for data in soup.find_all('div',class_="p0C73x"):
    name=data.find('div',attrs={'class':'Fo1I0b'})
    original_price=data.find('div',attrs={'class':'kRYCnD'})
    offered_price=data.find('div',attrs={'class':'hZ3P6w'})
    discount_percentage=data.find('div',attrs={'class':'HQe8jr'})
    if name and original_price and offered_price and discount_percentage:
        names.append(name.text)
        original_prices.append(original_price.text)
        offered_prices.append(offered_price.text)
        discount_percentages.append(discount_percentage.text)
# print(names)
# print(original_prices)  
# print(offered_prices)
# print(discount_percentages)

df = pd.DataFrame({'Name':names,'Original Price':original_prices,'Offered Price':offered_prices,'Discount Percentage':discount_percentages})
df.to_csv('shoes.csv', index=False, encoding='utf-8-sig')
print("CSV file saved successfully!")
