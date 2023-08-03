'''
! pip install feedparser
'''

import feedparser
d = feedparser.parse('http://www.reddit.com/r/python/.rss')

# print the title of the feed
print(d['feed']['title'])

# print the link
print(d['feed']['link'])

# print the number of links
print(len(d['entries']))

# print the entry information
print(d.entries[0]['link'])

for post in d.entries:
    print(post.title + ": "+post.link)
