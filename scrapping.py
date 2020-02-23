from requests_html import HTMLSession

session = HTMLSession()
source = session.get('http://172.16.104.50').html
# print(response.html)

source.render()
blocks = source.find('#test, .article')
print(blocks)
headlines = []
summaries = []

for block in blocks:
    headline = block.find('h2')[0]
    summary = block.find('p')[0]
    headlines.append(headline.text)
    summaries.append(summary.text)

print(headlines)
print(summaries)
