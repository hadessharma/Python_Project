from bs4 import BeautifulSoup
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

args = {
    "veryify": False
}
response = requests.get(url="https://news.ycombinator.com/newest", params=args)


soup = BeautifulSoup(response.text, "html.parser")
filter = soup.select(selector=".titleline")

for title in filter:
    print(title.text)
