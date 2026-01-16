import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from colorama import Fore, Back, Style

# Create a session
session = requests.Session()

# Define a retry strategy
retry_strategy = Retry(
    total=5,  # Total number of retries
    backoff_factor=1,  # Waits 1 second between retries, then 2s, 4s, 8s...
    status_forcelist=[429, 500, 502, 503, 504],  # Status codes to retry on
    method_whitelist=["HEAD", "GET", "OPTIONS"]  # Methods to retry
)

url = "http://192.168.56.103/.hidden/"
i = 0

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

def get_hidden_file(path):
    global url
    url += path
    response =  session.get(url)
    print("current link:", url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all("a")
    for x in range(len(links)):
        global i
        i = i + 1
        href = links[x].get("href")
        if(href == '../' ):
            continue

        if(href == 'README'):
            response =  session.get(url + "README")
            text = response.text
            if "flag" in text:
                print(Fore.GREEN, text, "in path", url)
                exit(0)
            else:
                url = url.replace(path, '')
                return
        get_hidden_file(href)

        

get_hidden_file("")
