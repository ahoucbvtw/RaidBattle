import tkinter as tk
import tkinter.font as tkfont
import PIL.Image
import PIL.ImageTk

window = tk.Tk()

#建立主視窗
class MainWindow(object):
	def __init__(self, master):
		self.window = master
		self.window.title('RaidBattle V1.0') #視窗名稱
		self.window.config(background='#f0f0f0')#更該視窗背景顏色
		self.window.geometry("590x570+300+50") #視窗解析度 (x*y+視窗欲固定的畫面位置X+視窗欲固定的畫面位置Y)
		self.window.resizable(0,0)#不可以更改大⼩

	def gotoSub(self):
			self.goSub = goSub

	#建立按鈕實體物件
	class Button(object):
		def __init__(self, ButtonName, height, width, x, y):
			self.ButtonName = ButtonName
			self.height = height
			self.width = width
			self.x = x
			self.y = y

			Font = tkfont.Font(family='新細明體', size=10, weight="bold")
			BN = tk.Button(window,text = self.ButtonName,font=Font)
			BN.config(bg= "skyblue")
			BN.config(width = self.width,height = self.height)
			# BN.config(command = self.gotoSub)
			BN.place(x = self.x, y = self.y)



#建立主視窗下的頁面
class Main(object):
	def __init__(self):
		image = PIL.Image.open("hole.png")
		photo = PIL.ImageTk.PhotoImage(image)

		label = tk.Label(window, image=photo)
		label.image = photo  # keep a reference!
		label.place(x = 15, y = 0)

		a = MainWindow.Button("絢麗草原",1,10,165,537)
		b = MainWindow.Button("沐光森林",1,10,72,522)
		c = MainWindow.Button("牙牙湖之眼",1,10,6,462)
		d = MainWindow.Button("牙牙湖東岸",1,10,8,418)
		e = MainWindow.Button("瞭望塔舊址",1,10,40,386)
		f = MainWindow.Button("牙牙湖西岸",1,10,55,358)
		g = MainWindow.Button("沙塵窪地",1,10,167,150)
		h = MainWindow.Button("巨人帽岩",1,10,140,124)
		i = MainWindow.Button("逆鱗湖",1,10,155,25)
		j = MainWindow.Button("拳關丘陵",1,10,435,28)
		k = MainWindow.Button("巨人鏡池",1,10,486,73)
		l = MainWindow.Button("巨石原野",1,10,440,185)
		m = MainWindow.Button("橋間空地",1,10,400,256)
		n = MainWindow.Button("機擎河岸",1,10,373,322)
		o = MainWindow.Button("美納斯湖北岸",1,10,435,382)
		p = MainWindow.Button("巨人凳岩",1,10,437,420)
		q = MainWindow.Button("美納斯湖南岸",1,10,386,520)

MainWindow(window)
Main()

window.mainloop() #確立視窗一直長在
