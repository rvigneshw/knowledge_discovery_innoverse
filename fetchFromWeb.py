from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import os
OUTPUT_DIR="CollectedData"
# from googlesearch import search

def fetchDataForUrl(query,filenameToSave):
    ####################################
    # for url in search('"Breaking Code" WordPress blog', stop=20):
    #     print(url)
    ###################################
    #################################
    formattedQuery=query.replace(' ','+')
    req = Request('https://www.google.com/search?q={}'.format(formattedQuery), headers={'User-Agent': 'Mozilla/5.0'})    
    with urllib.request.urlopen(req) as url:
        raw = BeautifulSoup(url.read(),features="html5lib")
        soup=raw.find_all(['cite', 'h3'])
        # soup=raw.select(".r")
        htmlData=''
        for data in soup:
            htmlData=htmlData+data.text+'\n'


        soup =BeautifulSoup(htmlData,features="html5lib")

        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        text=soup.get_text()
        lines = (line.strip()+"</br>" for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        char_list = [text[j] for j in range(len(text)) if ord(text[j]) in range(65536)]
        htmltext=''
        for j in char_list:
            htmltext=htmltext+j
    with open(os.path.join(OUTPUT_DIR ,filenameToSave), 'w+',encoding="utf8") as file:
        file.write(htmltext)

def fileAndData():
    indexString='<style>table, th, td {  border: 1px solid black;  border-collapse: collapse;}</style>\
        <center> <a href="summary.html">summary</a>\
        <table style="width:70%"><tr><th>Topic</th><th>Category</th><th>Link</th></tr>'
    with open('searchQueries.txt','r') as queryList:
        for line in queryList:
            query=''.join(line.split('<>'))
            query=query.replace('\n','')
            filename=line.replace('/','')
            filename=filename.replace('\n','.html')
            indexString=indexString+'<tr><td>{0}</td><td>{1}</td> <td><a href="{2}">{3}</a></td></tr>'.format(line.split('+')[1],line.split('+')[0],filename,filename)
            fetchDataForUrl(query,filename)

        with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w+') as index:
            indexString=indexString+'<table></center>'
            index.write(indexString)
        return
# if __name__ == "__main__":
#     fileAndData()
    