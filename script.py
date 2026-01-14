import requests
from bs4 import BeautifulSoup
url = "http://192.168.56.103/.hidden/"

def url_join(path):
    new_url = url + path
    return new_url

def get_hidden_file():
    # print("Visite de", url)

    response =  requests.get(url)
    # print("response:", response)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all("a")
    for link in links:
        if(link.get("href") == '../'):
            continue

        if(link.get("href") == 'README'):
            new_url = url_join("README")
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.find_all("p")
            if "flag" in text:
                print("flag trouve:", flag)
                return
        
    # print("Link:", link.get("href"), "Text:", link.string)
    get_hidden_file()



get_hidden_file()