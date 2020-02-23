from requests_html import HTMLSession
from bs4 import BeautifulSoup
import csv

csv_file = open('box_office.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['Title', 'Weekends', 'Gross', 'Weeks'])

session = HTMLSession()
responce = session.get('https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht').html
source = responce.html

soupe = BeautifulSoup(source, 'lxml')
box = soupe.find('tbody')
rows = box.find_all('tr')
all_movies = []

for movies in rows:
    title = movies.find('td', class_='titleColumn').text.replace('\n', '')
    weekends = movies.find('td', class_='ratingColumn').text.strip()
    gross = movies.find('span', class_='secondaryInfo').text
    weeks = movies.find('td', class_='weeksColumn').text
    all_movies.append((title, weekends, gross, weeks))
    csv_writer.writerow([title, weekends, gross, weeks])

print(all_movies)

