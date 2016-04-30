import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages,url_link,page,class_item):

    while page <= max_pages:
        url = url_link + str(page)
        source_code = requests.get(url, allow_redirects=False)
        # just get the code, no headers or anything
        plain_text = source_code.text.encode('ascii', 'replace')
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text,'html.parser')
        for link in soup.findAll('a', {'class': class_item}):
            href = link.get('href')
            title = link.string  # just the text, not the HTML
            print(href)
            print(title)
            #get_single_item_data(href)
        page += 1




url = str(input("Enter the link appropriately leaving the page no field blank \n Example : 'https://thenewboston.com/videos.php?cat=31&video=17966 '\n \t as \n' https://thenewboston.com/videos.php?cat=31&video= '"))
s = int(input("\nEnter the page number from where the program should crawl:\t"))
n = int(input("\nEnter the page no where crawling should end:\t"))
class_item = str(input("\nEnter the class name to filter results:\t"))
trade_spider(n,url,s,class_item)

