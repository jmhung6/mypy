import os
import bs4
import requests

url = "https://marketing-hsu01.web.app/fruit.html"
page = requests.get(url)
page.encoding = "utf-8"
# print(page)
soup = bs4.BeautifulSoup(page.text, "html.parser")
# print(soup.prettify)

# title_tag=soup.title

# img_tag = soup.find_all("img")
# for tag in img_tag:
#    print(tag)

img2_tag = soup.find_all("img")
# for tag in img2_tag:
#    print(tag.get("src"))

pos = url.rfind("/")
# print(pos)
web = url[0 : pos + 1]

img3_tag = soup.find_all("img")
for tag in img3_tag:
    src = tag.get("src")
    fullsrc = web + src
    print(fullsrc)
    file = src[src.rfind("/") + 1 :]
    print(file)

if not os.path.exists("download_img"):
    os.mkdir("download_img")
img = requests.get(fullsrc)

with open("download_img\\" + file, "wb") as file:
    file.write(img._content)
