from tkinter import *
from pytube import YouTube as yt
#Window layout
window = Tk()
window.geometry('500x300')
window.configure(bg='black')
#Does not allow the window to be resized
window.resizable(0,0) 
window.title("YouTube Video Downloader-Coding-Storm")

#Link section
link = StringVar()
Label(window, text = ''+'Paste the link :-', font = 'Tahoma 15 bold').place(x= 160 , y = 60)
link_enter = Entry(window, width = 70,textvariable = link).place(x = 32, y = 90)
def Downloader():     
    url =yt(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text = 'The video has been downloaded in the current directory', font = 'arial 15', bg = "lightgreen").place(x= 6 , y = 210)  
Button(window,text = 'Download!', font = 'Tahoma 15 bold' ,bg = 'white', padx = 2, command = Downloader).place(x=180 ,y = 150)
window.mainloop()
