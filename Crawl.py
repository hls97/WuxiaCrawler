import pdfkit

from bs4 import BeautifulSoup
import urllib.request

import os

url = "http://www.wuxiaworld.com/martialworld-index/mw-chapter-722/"

def makePDFWriter(path):
    return PdfFileWriter()



def makeSoup(url):
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    f = urllib.request.urlopen( req )
    raw_html = f.read()
    return BeautifulSoup(raw_html, "html.parser")



def getChapter(soup):
    text = article.find("div", {"itemprop": "articleBody"})
    lines = text.find_all("p")[1:]

    title = lines[0].string
    lines = lines[1:-1]
    page = title

    for line in lines:
        if line.string:
            page += line.string + "\n"

    return page

def getChapterHtml(soup):
    text = article.find("div", {"itemprop": "articleBody"})
    return text
def getNextLink(soup):
    text = article.find("div", {"itemprop": "articleBody"})
    a = text.find_all("a")[1]
    return a['href']

# path = os.path.join( "C:", "Program Files", "wkhtmltopdf", "bin", "wkhtmltopdf")
# config = pdfkit.configuration(wkhtmltopdf="./wkhtmltopdf")

soup = makeSoup(url)

article = soup.find("article")
options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'dpi': 300,
    "minimum-font-size": '20',
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
}

if not article:
    print ("Can't find article")
else:

    for i in range(30):
        # # create pdf writer
        # writer = PdfFileWriter()
        # outfile = open("test" + str(i) + ".pdf", "w")
        chapters = ""

        for j in range(10):
            # get text for a chapter
            chapter = getChapterHtml(article)

            # concat chapters

            chapters += chapter.prettify()

            # go to next link
            link = getNextLink(article)
            article = makeSoup(link).find("article")
            print (link)

        pdfkit.from_string(chapters, "Chapter-" + str(i) + ".pdf", options=options)
