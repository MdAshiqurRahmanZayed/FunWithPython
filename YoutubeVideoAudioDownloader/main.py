from tkinter import *                   
from tkinter import messagebox as mb  
from tkinter import filedialog as fd  
from pytube import YouTube           
import os
def browse_folder():  
     download_path = fd.askdirectory(initialdir = "D:\Downloads", title = "Select the folder to save the video")  
     download_dir.set(download_path)  
     
def download_video():  
     youtube_url = video_url.get()  
     download_folder = download_dir.get()  
     
     if(youtube_url != "" and download_folder != ""):  
          video = YouTube(youtube_url)        

          video_stream = video.streams.filter(file_extension = "mp4", progressive = True, res = "720p", type = "video").get_by_itag(22)  
     
          video_stream.download(download_folder)  
     
          mb.showinfo("Download Complete", "Selected Video is downloaded\nand saved successfully in " + download_folder)  
     
     else:  
          mb.showerror("Can't Download!!! Empty Fields", "Fields are empty!")  

def download_audio():  
     youtube_url = video_url.get()  
     download_folder = download_dir.get()  
     
     if(youtube_url != "" and download_folder != ""):  
          audio = YouTube(youtube_url).streams.get_audio_only()
          audio_download = audio.download(download_folder)
          base = os.path.splitext(audio_download)
          new_file = base + '.mp3'
          os.rename(audio_download, new_file)

     
          mb.showinfo("Download Complete", "Selected Video is downloaded\nand saved successfully in " + download_folder)  
     
     else:  
          mb.showerror("Can't Download!!! Empty Fields", "Fields are empty!")  

def reset():  

     video_url.set("")  
     download_dir.set("")  
 
     url_field.focus_set()  
     
def exit():  
     gui_root.destroy()  
     
# ------------------------- main function -------------------------  
     
if __name__ == "__main__":  
     gui_root = Tk()  
     
     gui_root.title("YouTube Downloader")  
     
     gui_root.geometry("800x600")  
     
     gui_root.resizable(0, 0)  
     
     gui_root.config(bg = "#3b3e50")  
     
     header_frame = Frame(gui_root, bg = "#3b3e50")  
     entry_frame = Frame(gui_root, bg = "#3b3e50")  
     button_frame = Frame(gui_root, bg = "#3b3e50")  
     
     header_frame.pack()  
     entry_frame.pack()  
     button_frame.pack()  
     
     # ------------------------- the header_frame frame -------------------------  
     

     header_label = Label(  
          header_frame,  
          text = "YouTube Video Downloader",  
          font = 'arial 30 bold',  
          bg = "#3b3e50",
          fg="White",  
          anchor = SE ,
          )  
     
     header_label.grid(row = 0, column = 1, padx = 10, pady = 10)  
     
     # ------------------------- the entry_frame frame -------------------------  
     
     url_label = Label(  
          entry_frame,  
          text = "Video URL:",  
          font = 'arial 20 bold',   
          bg = "#3b3e50",
          fg="White",
          anchor = SE  
          )  
     des_label = Label(  
          entry_frame,  
          text = "Destination:",  
         font = 'arial 20 bold',   
          bg = "#3b3e50",
          fg="White",  
          anchor = SE  
          )  
     
     url_label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)  
     des_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)  
     
     video_url = StringVar()  
     download_dir = StringVar()  
     
     url_field = Entry(  
          entry_frame,  
          textvariable = video_url,  
          width = 35,  
          font = 'arial 20 bold',  
          bg = "lightgreen",  
          fg = "#000000",  
          relief = GROOVE  
          )  
     des_field = Entry(  
          entry_frame,  
          textvariable = download_dir,  
          width = 26,  
          font = 'arial 20 bold',   
          bg = "#FFFFFF",  
          fg = "#000000",  
          relief = GROOVE  
          )  
     
     url_field.grid(row = 0, column = 1, padx = 5, pady = 5, columnspan = 2)  
     des_field.grid(row = 1, column = 1, padx = 5, pady = 5)  
     
     browse_button = Button(  
          entry_frame,  
          text = "Browse",  
          width = 7,  
          font = 'arial 20 bold',  
          bg = "#FF9200",  
          fg = "#FFFFFF",  
          activebackground = "#FFE0B7",  
          activeforeground = "#000000",  
          relief = GROOVE,  
          command = browse_folder  
          )  
     
     browse_button.grid(row = 1, column = 2, padx = 5, pady = 5)  
     
     # ------------------------- the button_frame frame -------------------------  
     
     download_button = Button(  
          button_frame,  
          text = "Download",  
          width = 12,  
          font = 'arial 20 bold',  
          bg = "#15EF5F",  
          fg = "#FFFFFF",  
          activebackground = "#97F9B8",  
          activeforeground = "#000000",  
          relief = GROOVE,  
          command = download_video  
          )  
     download_audio_button = Button(  
          button_frame,  
          text = "Download Audio",  
          width = 15,  
          font = 'arial 20 bold',  
          bg = "#15EF5F",  
          fg = "#FFFFFF",  
          activebackground = "#97F9B8",  
          activeforeground = "#000000",  
          relief = GROOVE,  
          command = download_audio  
          )
     reset_button = Button(  
          button_frame,  
          text = "Clear",  
          width = 12,  
          font = 'arial 20 bold',  
          bg = "#23B1E6",  
          fg = "#FFFFFF",  
          activebackground = "#C3E6EF",  
          activeforeground = "#000000",  
          relief = GROOVE,  
          command = reset  
          )  
     close_button = Button(  
          button_frame,  
          text = "Exit",  
          width = 12,  
          font = 'arial 20 bold',  
          bg = "#F64247",  
          fg = "#FFFFFF",  
          activebackground = "#F7A2A5",  
          activeforeground = "#000000",  
          relief = GROOVE,  
          command = exit  
          )  
     
     download_button.grid(row = 0, column = 0, padx = 5, pady = 10)  
     reset_button.grid(row = 0, column = 1, padx = 5, pady = 10)  
     close_button.grid(row = 0, column = 2, padx = 5, pady = 10)  
     download_audio_button.grid(row = 1, column = 0, padx = 5, pady = 10)  
     
     gui_root.mainloop()  