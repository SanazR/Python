import pandas as pd
import requests
from bs4 import BeautifulSoup

page= requests.get ('https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.YWVra9pByUk')

soup= BeautifulSoup(page.content,'html.parser')

#print(soup)
#Find all 'a' tags
#print(soup.find_all('a'))

week=soup.find(id='seven-day-forecast-body')
#print (week)

items= week.find_all(class_='tombstone-container')
#print(items[0])
#print()
#print(items[1])

print(items[1].find(class_='period-name').get_text())
print(items[1].find(class_='short-desc').get_text())
print(items[1].find(class_='temp').get_text())
print()

period_names=[item.find(class_='period-name').get_text() for item in items]

short_description=[item.find(class_='short-desc').get_text() for item in items]

temperature=[item.find(class_='temp').get_text() for item in items]

print(period_names)
print()
print(short_description)
print()
print(temperature)
print()

weather_stuff= pd.DataFrame(
  {'period': period_names,
  'short-desc': short_description,
  "temp": temperature
    
  }
)


print(weather_stuff)
weather_stuff.to_csv('weather.csv')

