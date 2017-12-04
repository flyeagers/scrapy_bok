import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    #
    url = 'http://www.piaotian.com/html/0/738/360430.html'
    head = {}
    #
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    #req = requests.Request(url, headers=head)
    #params = {'page': 1}
    #response = urllib.urlopen(req)
    response = requests.get(url, params=head)
    #response = requests.urlopen(req)
    #html = response.read()
    soup = BeautifulSoup(response.text, "html.parser")  #
    #
    #soup = BeautifulSoup(html, 'lxml')
    #
    soup_text = soup.find('br')
    #
    print(soup_text.text)