#import
from cProfile import label
import tkinter as tk
from pytube import YouTube
import os

#介面
win = tk.Tk()
win.geometry("560x280")
win.title("Youtube影片下載器")
getvideo = "360p"
videorb = tk.StringVar()
url = tk.StringVar()
path = tk.StringVar()


#輸入網址
label1 = tk.Label(win, text= "Youtube網址：")
label1.place(x = 123, y = 30)
entryUrl = tk.Entry(win, textvariable = url)
entryUrl.config(width = 20)
entryUrl.place(x = 220, y = 30)

#檔案位置
label2 = tk.Label(win, text = "存檔位置（預設為『下載』資料夾）")
label2.place(x = 10, y = 70)
entryPath = tk.Entry(win, textvariable = path)
entryPath.config(width = 20)
entryPath.place(x = 220, y = 70)

#command
def clickDown():
    global getvideo, strftype, listradeo
    labelMsg.config(text = "")
    if(url.get() == ""):
        labelMsg.config(text = "網址欄位為必填！")
        return

    if(path.get() == ""):
        pathdir = "download"
    else:
        pathdir = path.get()
        pathdir = pathdir.replace("\\","\\\\")

    try:
        yt = YouTube(url.get())
        yt.streams.filter(subtype = 'mp4', res = getvideo, progressive = True).first().download(pathdir)

        labelMsg.config(text = "下載完成！")

    except:
        labelMsg.config(text = "影片無法下載！")

def rbVideo():
    global getvideo
    labelMsg.config(text = "")
    getvideo = videorb.get()

#選取格式
rb1 = tk.Radiobutton(win, text = '360p, mp4', variable = videorb, value = '360p', command = rbVideo)
rb1.place(x = 220, y = 110)
rb1.select() #default
rb2 = tk.Radiobutton(win, text = "720p, mp4", variable = videorb, value = "720p", command = rbVideo)
rb2.place(x = 220, y = 130)

#按鈕
btnDown = tk.Button(win, text = "開始下載", command = clickDown)
btnDown.place(x = 220, y = 180)

#提示訊息
labelMsg = tk.Label(win, text = "", fg = "red")
labelMsg.place(x = 220, y = 220)

win.mainloop()