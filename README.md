# WuxiaCrawler
Crawls through Wuxiaworld and converts Chapters into Mobi files for Kindle

## Usage
```python
# python Crawl.py [chapter link] [number of chapters] [chapters per file]
```
```
python Crawl.py http://www.wuxiaworld.com/martialworld-index/mw-chapter-25/ 500 50
```

### Notes
* Uses python 3.6; For 2.7, change urllib to urllib2 (need to pip install)
* Chapter link must have trailing '/'
* Must have Kindlegen installed and at the appropriate directory; set kindlegenpath in Crawl.py
* Must have beautifulsoup4 installed
```
pip install beautifulsoup4
```
