# import pdfkit

from bs4 import BeautifulSoup
import urllib.request

import subprocess
import os
import sys

url = sys.argv[1]
print(url.split('/'))
titleChapter = url.split('/')[-2].split('-')

title = "".join(titleChapter[:-1]) # title of novel
firstChapterNum = int(titleChapter[-1])  #chapter number

totalChapters = int(sys.argv[2]) # total chapters to download
perFile = int(sys.argv[3]) # how many chapters per file

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
    i = 0
    
    for i in range(totalChapters//perFile):
        
        j = 0
        
        startChapterNum = i+j+firstChapterNum
        endChapterNum = startChapterNum + perFile
        
        filename = title + "-" + str(startChapterNum) + "-" + str(endChapterNum) + ".html"
        
        outfile = open(filename, "w") # itermediary html file
        
        # opening tags
        chapters = '''
            <html xlmns="http://www.w3.org/1999/xhtml" lang="en-US">
            <head>
            <meta http-equiv="content-type" content="text/html; charset=UTF-8">
            </head>
            <body>
            '''

        for j in range(perFile):
            # get text for a chapter
            html = getChapterHtml(article)
            
            # concat chapters
            
            chapters += str(html)
            
            # go to next link
            link = getNextLink(article)
            article = makeSoup(link).find("article")
            print (link)
        
        chapters += "</body></html>" # closing tags
        outfile.write(chapters)
        
        outfile.close() # close the file
        
        # kindlegen - create mobi file from html
        subprocess.Popen(["/Users/HLS/code/KindleGen/kindlegen", filename])