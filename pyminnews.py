#!/usr/bin/python
# -*- coding: utf-8 -*-

from pattern.web import URLError, download
import re

news_file = "/home/david/pyminnews/news"

def main():

    title = ""
    url = ""
    regex = ""
    
    i = 0
    
    with open(news_file, 'r') as f:
        r = f.readline()
        while r:
            if i == 0:
                title = r
                i = i + 1
            elif i == 1:
                url = r
                url = url[0:len(url)-1]
                i = i + 1
            elif i == 2:
                regex = r
                i = 0
                search_regex(title, url, regex)
            r = f.readline()
        

def search_regex(title, url, regex):

    print title
    
    try:
        html = download(url, unicode=True)
    except URLError as e:
        print "Something happened... Error: " + str(e) + "\n"
        exit(0)

    results = re.findall(regex, html)

    if len(results) == 0:
        print "There are no news...\n"
    else:
        print "Go to " + url + " to see some news.\n"

if __name__ == "__main__":
    main()
