import re
import urllib
from BeautifulSoup import BeautifulSoup, SoupStrainer
import os
import sys

def findpath(url):
    try:
        page = urllib.urlopen(url)
        links = ''
        for link in BeautifulSoup(page, parseOnlyThese=SoupStrainer('img')):
            if link.has_key('src'):
                match = re.search('.jpg', link['src'])
                if match:
                    links = str(link['src'])
                else:
                    match = re.search('.JPG', link['src'])
                    if match:
                        links = str(link['src'])
        
        return links
    except IOError,e:
        return 'error'

def unduhmengunduh(urls,series,maxhal):
    sx = 0
    if os.path.exists(series):
        print "folder already exist"
    else:
        os.mkdir(series)
    maxhal = int(maxhal)
    while sx < maxhal:
        sx = sx + 1
        print "downloading page "+str(sx)
        filex, exts = os.path.splitext(urls)
        filex = filex+"-page-"+str(sx)+exts
        
        print "trying download this page : "+filex
        paths = findpath(filex)
        print "got the image : "+paths
        if paths == 'error': break
        unduh = urllib.urlopen(paths) 
        basen = os.path.basename(paths)
        
        print "writing on the folder"
        filox, extos = os.path.splitext(basen)
        filename = str(sx)+extos
        output = open(series+'\\'+filename,'wb')
        output.write(unduh.read())
        output.close()

def downloadit(urls,maxseries,minseries):
    sa = int(minseries) - 1
    title, t_ext = os.path.splitext(urls)
    print "starting ......."
    maxseries = int(maxseries)
    while sa < maxseries:
        sa = sa + 1
        if os.path.exists(str(sa)):
            print "folder already exist"
        else:
            os.mkdir(str(sa))
        chapter = title+"-chapter-"+str(sa)+".html"
        print chapter
        try:
            sx = 0
            readchapter = urllib.urlopen(chapter)
            while sx < 99:
                sx = sx + 1
                xpage, xts = os.path.splitext(chapter)
                xpage = xpage+"-page-"+str(sx)+".html"
                print xpage
                try:
                    page = urllib.urlopen(xpage)
                    links = ''
                    for link in BeautifulSoup(page, parseOnlyThese=SoupStrainer('img')):
                        if link.has_key('src'):
                            match = re.search('.jpg', link['src'])
                            match1 = re.search('.JPG', link['src'])
                            if match:
                                links = str(link['src'])
                            elif match1:
                                links = str(link['src'])
                            else:
                                links = ''
        
                    if links == '':break
                    try:
                        unduh = urllib.urlopen(links) 
                        basen = os.path.basename(links)
                        print "writing on the folder"
                        filox, extos = os.path.splitext(basen)
                        filename = str(sx)+extos
                        output = open(str(sa)+'\\'+filename,'wb')
                        output.write(unduh.read())
                        output.close()
                    except IOError:
                        break  
                except IOError:
                    break
        except IOError:
            print "This chapter is not detected. Perhaps use alphanumeric instead number. Please check on the site first and use the mode one"
            continue

if __name__ == '__main__':
    #http://manga.animea.net/shoot--chapter-4-page-3.html
    modes = raw_input('> Mode Download (type: all/one/quit) : ')
    while (modes != 'quit'):
        try:
            if modes == 'all':
                url = raw_input('> Masukkan URL nya : ')
                halmin = raw_input('> Masukkan Series Start : ')
                halmax = raw_input('> Masukkan Series Finish : ')
                downloadit(url,halmax,halmin)
            else:
                url = raw_input('> Masukkan URL chapter nya : ')
                seri = raw_input('> Masukkan Serinya : ')
                halmax = raw_input('> Masukkan Halaman Max : ')
                unduhmengunduh(url,seri,halmax)
            modes = raw_input('> Mode Download (type: all/one/quit) : ')
        except:
            sys.exit(1)

