import tkinter as tk 
from web_engine import Ara as ara
import webbrowser

root=tk.Tk() 
root.geometry("1500x600") 


kelime_sec=tk.StringVar() 

class hyperlink():
    def __init__(self,i):
        link = tk.Label(root, text=i, fg="blue", cursor="hand2")
        link.grid()
        link.bind("<Button-1>", lambda event: webbrowser.open_new(i))

    
      
OPTIONS = [
"https://www.mynet.com/",
"https://www.sondakika.com/",
"https://www.haberler.com/"
] 
variable = tk.StringVar(root)
variable.set(OPTIONS[0]) # default value
w = tk.OptionMenu(root, variable, *OPTIONS)
w.grid(row=3,column=3) 

def ok():
    link=variable.get()
    kelime=kelime_sec.get() 

    m1 = ara(link, kelime)
    links=""
    if link == "https://www.sondakika.com/": 
        links = m1.sondakika_ara()
        print(link)
    else:
        links = m1.mynet_ara()
        
    for i in links:
        a = hyperlink(i)  
      
    kelime_sec.set("") 

button = tk.Button(root, text="search", command=ok)
button.grid(row=5,column=3) 
      
kelime_sec_entry=tk.Entry(root, textvariable = kelime_sec, font = ('calibre',10,'normal')) 
kelime_sec_entry.grid(row=4,column=3) 
   


root.mainloop()
