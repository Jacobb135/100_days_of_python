from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')

titles = soup.find_all(name="span", class_="titleline")

title_list = []
link_list = []

for title in titles:
    title_list.append(title.text)
    anchor = title.a
    link_list.append(anchor.get("href"))

upvotes = soup.find_all(class_="score")
upvote_list = [int(upvote.text.split()[0]) for upvote in upvotes]

print(title_list)
print(link_list)
print(upvote_list)

most_upvotes = max(upvote_list)
index = upvote_list.index(most_upvotes)
print(title_list[index])
print(link_list[index])
print(most_upvotes)

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# # print(soup.p)
#
# # all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.text)
#
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# heading = soup.select(".heading")
# print(heading)

