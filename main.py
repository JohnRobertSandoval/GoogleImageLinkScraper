import requests
import json
global startIndex
global searchTerm
global c
c= 1
def searchT():
    global searchTerm
    global c
    c= 1
    searchTerm = input("Search:")
    start()

def start():
    global startIndex
    global c
    if c == 1:
        c =c + 1
        startIndex = "1"
        search()
    else:
        startIndex = int(startIndex) + 8
        startIndex = str(startIndex)
        search()

def search():
    try:
        global searchTerm
        global startIndex 
        key = '[Google Console Key]'
        cx = '[CSE ID]'
        searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + \
            searchTerm + "&start=" + startIndex + "&key=" + key + "&cx=" + cx + \
            "&searchType=image"
        r = requests.get(searchUrl)
        response = r.content.decode('utf-8')
        result = json.loads(response) 
        items = result['items']
        for i in items:
            with open("links.txt", "a+") as myfile:
                links = "'"+i['link']+"',\n"
                myfile.write(links)
                print(links)
            myfile.close()
        start()
    except KeyError:
        searchT()
searchT()



