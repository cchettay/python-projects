import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("span", class_="titleline")

print("===== TOP TECH NEWS =====\n")

for i in range(len(headlines)):
    print(i + 1, ".", headlines[i].text)
