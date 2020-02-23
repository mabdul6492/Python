from requests_html import HTMLSession
import csv

csv_file = open('imdb.csv', 'w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['Title', 'Runtime', 'Director', 'Plot'])
session = HTMLSession()
source = session.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth').html
body = source.find("div.list.detail.sub-list")[0]
movies = body.find('.nm-title-overview-widget-layout')

movie_info = []

for movie in movies:
    title = movie.find('h4 a')[0].text
    runtime = movie.find('td p time')[0].text
    directors = movie.find('div span a')
    director = [director.text for director in directors]
    plot = movie.find('.outline')[0].text
    stars = movie.find()
    movie_info.append((title, runtime, director, plot))
    csv_writer.writerow([title, runtime, director, plot])
#
# for movie in movie_info:
#     print(f"Title:{movie[0]} \n"
#           f"Duration: {movie[1]} \n"
#           f"Directors:{movie[2]} \n"
#           f"Plot:{movie[3]} \n")
