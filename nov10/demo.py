from bs4 import BeautifulSoup
import requests

def main():
    ev = electoralVotes()
    
    stateNames = list(ev.keys())
    stateNames.sort()
    
    for key in stateNames:
        print (key + ":", ev[key])
    
def electoralVotes():
    url = "https://www.britannica.com/topic/United-States-Electoral-College-Votes-by-State-1787124"
    source_code = requests.get(url).text
    doc = BeautifulSoup(source_code, "html.parser")
    
    trtags = doc.find_all("tr")
    
    votes = {}
    
    for tag in trtags:
        tdtags = tag.find_all("td")
        
        if len(tdtags) == 6:
            for i in range(0, 6, 2):
                votes[tdtags[i].text] = int(tdtags[i + 1].text)
                
    return votes

if __name__ == "__main__":
    main()
