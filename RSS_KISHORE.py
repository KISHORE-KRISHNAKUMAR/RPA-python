import feedparser
def titles(a):
    b = a.entries
    for i in range(5):
        print(b[i]['title'])
        print('\n')
urls= [ 'https://www.thehindu.com/sci-tech/science/feeder/default.rss' ,
          'https://www.thehindu.com/business/Economy/feeder/default.rss',
          'https://www.thehindu.com/news/international/feeder/default.rss',
          'https://www.thehindu.com/business/markets/feeder/default.rss']
for i in urls:
    d = feedparser.parse(i)
    print(d['feed']['title'] , ':')
    titles(d)
    print()
