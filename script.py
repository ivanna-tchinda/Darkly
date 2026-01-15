import requests
from bs4 import BeautifulSoup
url = "http://192.168.56.103/.hidden/"
i = 0

def url_join(path):
    new_url = url + path
    return new_url

def get_hidden_file(new_url, path):

    new_url += path
    response =  requests.get(new_url)
    print("get", new_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all("a")
    # print("get all links", links)
    for x in range(len(links)):
        global i
        i = i + 1
        print("into", links[x].get("href"), i)
        if(links[x].get("href") == '../' ):
            continue

        if(links[x].get("href") == 'README'):
            new_url += "README"
            response =  requests.get(new_url)
            text = response.text
            # print(text)
            if "flag" in text:
                print("flag trouve:", flag)
                return
            else:
                return
        # print("entering a new file")
        get_hidden_file(new_url, links[x].get("href"))

        

get_hidden_file(url, "")
