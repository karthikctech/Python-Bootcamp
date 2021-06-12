import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
       article_text = article_tag.getText()
       article_texts.append(article_text)
       article_link = article_tag.get("href")
       article_links.append(article_link)
article_upvotes =[score.getText() for score in  soup.find_all(name="span", class_="score")]
largest_points = max(article_upvotes)
largest_index = article_upvotes.index(largest_points)
print(article_texts[largest_index])
print(article_links[largest_index])





# print(article_texts)
# print(article_links)
# print(article_upvotes)