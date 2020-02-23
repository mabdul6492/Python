from requests_html import HTMLSession
from bs4 import BeautifulSoup
import csv

csv_file = open('books.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['Title', 'Price', 'ImageUrl'])
urls = []
count = 1

for i in range(1, 51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{i}.html')

for url in urls:
    session = HTMLSession()
    response = session.get(url).html
    source = response.html

    soup = BeautifulSoup(source, 'lxml')
    box = soup.find('ol')

    all_books = []
    books = box.find_all('li')

    for book in books:
        title = book.select('h3 a')[0]['title']
        price = book.find('p', class_='price_color').text
        image = book.find('img')['src']
        all_books.append((title, price, url+image))
        csv_writer.writerow([title, price, url+image])
        print(count, end=" ")
        count = count + 1

    # for book in all_books:
    #     print('Title: {} \n Price: {} \n image: {} \n'
    #           .format(*book))

csv_file.close()
