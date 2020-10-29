import tkinter as tk 
import web_engine as ara   
import webbrowser

root=tk.Tk() 
root.geometry("1500x600") 

link_var=tk.StringVar() 
kelime_var=tk.StringVar() 

class hyperlink():
    def __init__(self,i):
        link = tk.Label(root, text=i, fg="blue", cursor="hand2")
        link.grid()
        link.bind("<Button-1>", lambda event: webbrowser.open_new(i))

def submit(): 
    link=link_entry.get() 
    kelime=kelime_var.get() 

    links = ara.webara(link, kelime)
    for i in links:
        a = hyperlink(i)  
      
    link_var.set("") 
    kelime_var.set("") 
      
      
# creating a label for  
# name using widget Label 
link_label = tk.Label(root, text = 'Links: ', font=('calibre', 10, 'bold')) 
# name using widget Entry 
link_entry = tk.Entry(root, textvariable = link_var,font=('calibre',10,'normal')) 
   
# creating a label for password 
kelime_label = tk.Label(root,text = 'Aradığın Kelime',font = ('calibre',10,'bold')) 
# creating a entry for password 
kelime_entry=tk.Entry(root, textvariable = kelime_var, font = ('calibre',10,'normal')) 
   
# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(root,text = 'Keşfet', command = submit) 
   

link_label.grid(row=0,column=0) 
link_entry.grid(row=0,column=1) 
kelime_label.grid(row=1,column=0) 
kelime_entry.grid(row=1,column=1) 
sub_btn.grid(row=2,column=1) 
   
# performing an infinite loop  
# for the window to display 
root.mainloop()
