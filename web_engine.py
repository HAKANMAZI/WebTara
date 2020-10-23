from bs4 import BeautifulSoup, SoupStrainer
import requests
import thread

url = "https://www.sondakika.com/"
kelime = "PKK"

def webara(url, kelime):
    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data)

    url_list =[]
    for link in soup.find_all('a'):
        ekle = link.get('href')[1:]

        url2 = url+ekle 
        res = requests.get(url2)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')

        for i in soup.find_all('p'):
            if kelime in i.get_text():
                url_list.append(url2)

    mylist = list(set(url_list))
    return mylist