from tkinter import *
import pytube

#functions
def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download(r"C:\YouTube Videos Downloaded")
        notif.config(fg="green", text="Download successfull! Congratulations")
    except Exception as e:
        print(e)
        notif.config(fg="red", text="Video could not be downloaded")




#Main Screen
master = Tk()
master.title("Youtube Downloader")


#Labels
Label(master, text="Youtube Video Converter", fg="red", font=("Calibri", 15)).grid(sticky=N, padx=100, row=0)
Label(master, text="Please enter the link to your video below : ",font=("Calibri", 12)).grid(sticky=N, row=1, pady=15)
notif = Label(master, font=("Calibri", 12))
notif.grid(sticky=N,pady=1,row=4)

#variables
url = StringVar()

#Entry
Entry(master,width=50,textvariable=url).grid(sticky=N,row=2)

#Button
Button(master, width=20, text="Download", font=("Calibri",12),command=download).grid(sticky=N,row=3,pady=15)


master.mainloop()
