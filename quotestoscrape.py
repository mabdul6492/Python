from requests_html import HTMLSession
from bs4 import BeautifulSoup
import csv

urls = []
count = 1
csv_file = open('quotes.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['Quotes', 'Author', 'Tags'])

for i in range(1, 11):
    urls.append(f'http://quotes.toscrape.com/page/{i}/')

for url in urls:
    session = HTMLSession()
    responce = session.get(url).html
    source = responce.html

    soup = BeautifulSoup(source, 'lxml')
    box = soup.find_all('div', class_='quote')
    all_quotes = []

    for quotes in box:
        quote = quotes.find('span', class_='text').text
        author = quotes.find('small', class_='author').text
        tags = quotes.select('div.tags a')
        tag = [tat.text for tat in tags]
        all_quotes.append((quote, author, tag))
        csv_writer.writerow([quote, author, tag])

csv_file.close()

    # for all_quote in all_quotes:
    #     print('Count: {} \n Quote: {} \n Author: {} \n Tags: {} \n\n'
    #           .format(count, *all_quote))
    #     count += 1
