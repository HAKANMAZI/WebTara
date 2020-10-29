from bs4 import BeautifulSoup, SoupStrainer
import requests

class Ara():
     url = ""
     kelime =""
     page = ""    
     data = ""
     soup = ""
     url_list =[]

     def __init__(self, url, kelime):
           self.page = requests.get(url)
           self.data = self.page.text
           self.soup = BeautifulSoup(self.data,features="lxml")
           self.url = url
           self.kelime = kelime
           
            
     def mynet_ara(self):
        for a in self.soup.find_all('a'):
            try:
                link = a.get('href')
                res = requests.get(link)
                html_page = res.content
                soup = BeautifulSoup(html_page, features="lxml")
        
                for i in soup.find_all('p'):
                    if self.kelime in i.get_text():
                        self.url_list.append(link)
                        print(link)
            except:
                print("error: "+ str(link))
    
        mylist = list(set(self.url_list))
        return mylist
    
    
    
     def sondakika_ara(self):
        for a in self.soup.find_all('a'):
            link = a.get('href')[1:]
    
            url2 = self.url+link 
            res = requests.get(url2)
            html_page = res.content
            soup = BeautifulSoup(html_page, 'html.parser')
    
            for i in soup.find_all('p'):
                if self.kelime in i.get_text():
                    self.url_list.append(url2)
                    print(url2)
    
        mylist = list(set(self.url_list))
        return mylist

