from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()
# pass the soup
soup = BeautifulSoup(content, "html.parser")
print(soup.title)
print(soup.title.string)
# it is used to indenting the the whole program
print(soup.prettify())
# in this tag is used to print only anchor tag
print(soup.a)
# in this tag is used to print all anchor tag
all_anchor_tag = soup.find_all(name="a")
print(all_anchor_tag)
# print all anchor tag
soup.find_all("a")
# print anchor link in paragraph inside anchor
company_url = soup.select_one(selector= "p a")
# all the link print into text
for tag in all_anchor_tag:
    print(tag.getText()
# to print all the links only
    print(tag.get("href"))
# to print only one heading
heading = soup.find(name="h", id="name")
print(heading)
# to print only all heading
heading = soup.find_all(name="h3", class_="heading")
# to print one whole class_
soup.select(".heading")