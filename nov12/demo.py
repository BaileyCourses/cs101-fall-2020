from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def showLinks(url):

    html = requests.get(url).text
    doc = BeautifulSoup(html, "html.parser")

    links = doc.find_all("a")

    for link in links:
        href = link.get("href")
        
        if href.startswith("/wiki/"):
            href = urljoin("https://en.wikipedia.org", href)
            
        print(href)

def wikipedia(startingUrl, numPages):
    
    url = startingUrl
    
    for i in range(numPages):
        html = requests.get(url).text
        doc = BeautifulSoup(html, "html.parser")
        
        paras = doc.find_all("p")
        
        for para in paras:
            firstLink = para.find("a")
            
            if firstLink is not None:
                break
            
        
        # ensure that firstPara has a link
        
#        firstLink = firstPara.find("a")
        newUrl = firstLink.get("href")
        
        if newUrl.startswith("/wiki/"):
            newUrl = urljoin("https://en.wikipedia.org", newUrl)
            

        print(newUrl)
        url = newUrl

    

def main():
#    showLinks("https://en.wikipedia.org/wiki/Hamilton_College")
    wikipedia("https://en.wikipedia.org/wiki/Hamilton_College", 100)
    
#    print("Welcome!")

if __name__ == "__main__":
    main()
