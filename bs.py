from bs4 import BeautifulSoup
import requests

url = 'https://lotus.vn/lachanviruscorona'
page = requests.get(url, verify=False)
soup = BeautifulSoup(page.text, 'html.parser')

journey = soup.find_all("div", class_='statistic_number red')
print(journey)
#print("H3 = ",journey[0].find("h3").text)


'''
url = 'https://lotus.vn/lachanviruscorona'
page = requests.get(url, verify=False)
soup = BeautifulSoup(page.text, 'html.parser')
journey = soup.find_all("div", class_='statistic_number red')

print(journey)
'''