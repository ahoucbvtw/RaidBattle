import tkinter as tk
import PIL.Image
import PIL.ImageTk


window = tk.Tk()

#建立主視窗
class MainWindow(object):
	def __init__(self, master):
		self.window = master
		self.window.title('zzz V1.0') #視窗名稱
		self.window.config(background='#f0f0f0')#更該視窗背景顏色
		self.window.geometry("590x570+300+50") #視窗解析度 (x*y+視窗欲固定的畫面位置X+視窗欲固定的畫面位置Y)
		self.window.resizable(0,0)#不可以更改大⼩

# window.title(12) #視窗名稱
# window.geometry("590x570+300+50") #視窗解析度 (x*y+視窗欲固定的畫面位置X+視窗欲固定的畫面位置Y)
# window.resizable(0,0) #不可以更改大⼩
# window.config(background='#f0f0f0') #更該視窗背景顏色
MainWindow(window)

make_frame = tk.LabelFrame(window, width=100, height=100) 
make_frame.place(x = 40, y = 7) 



# now create the ImageTk PhotoImage: 
image = PIL.Image.open("4.png")
img = PIL.ImageTk.PhotoImage(image) 
in_frame = tk.Label(make_frame, image = img) 
in_frame.pack() 

window.mainloop() 