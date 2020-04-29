from tkinter import *
import tkinter.font as tkfont
from  tkinter  import ttk
import PIL.Image
import PIL.ImageTk
import sqlite3 as lite
import sys, os


#建立連線自身資料庫(return不能使用在__init__裡)
class database(object):
	def __init__(self, Table,Searchdata):
		self.Table = Table
		self.Searchdata = Searchdata

	def connect(self):
		con = lite.connect('RaidBattle.db')
		with con:
			cur = con.cursor()

			if self.Table == str("Map") :
				cursor = cur.execute("SELECT *from Map")
				for row in cursor:
					if row[1] == self.Searchdata:
						a = row[2]
						return a


			elif self.Table == str("Sword") :
				cursor = cur.execute("SELECT *from Sword")
				for row in cursor:
					if row[1] == self.Searchdata:
						a = row[2]
						return a
			else:
				cursor = cur.execute("SELECT *from Shield")
				for row in cursor:
					if row[1] == self.Searchdata:
						a = row[2]
						return a

#建立Sub主視窗
class Sub(object):

	def gotoMain(self):
		print("返回主頁面")
		self.goMain()

#建立主視窗
	def __init__(self, goMain, MapName):

		def resource_path(relative_path):
		#Get absolute path to resource, works for dev and for PyInstaller
			try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
				base_path = sys._MEIPASS
			except Exception:
				base_path = os.path.abspath(".")
			return os.path.join(base_path, relative_path)

		icon = resource_path("icon.ico")
		self.window = goMain
		self.window = Tk()
		self.window.iconbitmap(icon)
		self.MapName = MapName
		self.window.title(self.MapName) #視窗名稱
		self.window.config(background='#f0f0f0')#更該視窗背景顏色
		self.window.geometry("590x580+500+180") #視窗解析度 (x*y+視窗欲固定的畫面位置X+視窗欲固定的畫面位置Y)
		self.window.resizable(0,0)#不可以更改大⼩

		#起動搜詢資料庫的實體物件
		maplist = database("Map",self.MapName)

		#定義遊戲版本選擇按鈕的觸發事件
		def show(*args):
			#一定要遊戲版本、洞口顏色、洞口號碼都選擇(字串中要有值)才會執行下列搜尋資料庫動作
			if gameversion.get() != str() and holeColor.get() != str() and holeNumlist.get() != str():
				aa = holeNumlist.get() + holeColor.get()
				monlistValue = database(gameversion.get(),aa)
				monlist.delete(0,END) #清空Pokemon List列表
				monlistdabase = monlistValue.connect() #將資料庫中Pokemon資料代出
				ccc = monlistdabase.split("#") #將Pokemon資料以#來區隔(splite)成字串陣列
				print(ccc)
				for item in ccc: #將Pokemon字串陣列一一代入Pokemon List
					monlist.insert("end", item)

				#將Lable改成使用圖像方式匯入顯示選擇會出現的寶可夢圖片
				PNGMon = resource_path( gameversion.get() + aa +".png" )
				image1 = PIL.Image.open(PNGMon)
				img1 = PIL.ImageTk.PhotoImage(image1)
				label = Label(self.window, image = img1)
				label.image = img1
				label.place(x = 195, y = 518)


#建立一圖片在LableFrame底下
		Font = tkfont.Font(family='新細明體', size=10, weight="bold")
		FontMon = tkfont.Font(family='新細明體', size=11)

		frame1 = Frame(self.window,height=250, bd=3, relief="sunken")
		frame1.pack(fill="x", padx=5, pady=5)

		#將Lable改成使用圖像方式匯入顯示選擇區域地圖

		mappng = resource_path( self.MapName + ".png")
		image = PIL.Image.open(mappng)
		img = PIL.ImageTk.PhotoImage(image)
		label = Label(frame1, image = img)
		label.image = img
		label.pack()

#製作遊戲版本單選Radiobutton
		labelFrame1 = LabelFrame(self.window, text = "遊戲版本", font=Font,padx = 5, pady = 5)
		labelFrame1.place(x = 48, y = 335)

		gameversion = StringVar()  #此變數的預設輸入為字串
		sword = Radiobutton(labelFrame1, text = "劍", variable= gameversion, value = "Sword", font=Font, indicatoron=False, command = show, bg= "#b5e1f3")
		shield = Radiobutton(labelFrame1, text = "盾", variable= gameversion, value = "Shield", font=Font, indicatoron=False, command = show ,bg= "#b5e1f3")
		sword.pack()
		shield.pack()


#製作巢穴光柱單選Radiobutton
		labelFrame2 = LabelFrame(self.window, text = "巢穴光柱", font=Font,padx = 5, pady = 5)
		labelFrame2.place(x = 155 , y = 335)

		holeColor = StringVar()
		red = Radiobutton(labelFrame2, text = "紅色光柱", variable= holeColor, value = "R", font=Font, indicatoron=False, command = show, bg= "#b5e1f3")
		purple = Radiobutton(labelFrame2, text = "紫色光柱", variable= holeColor, value = "P", font=Font, indicatoron=False, command = show, bg= "#b5e1f3")
		red.pack()
		purple.pack()



#建立Frame把巢穴標號的Label和Combobox下拉選單一起放入底下方便後續一起調整位置
		frame4 = Frame(self.window,padx = 5, pady = 10)
		frame4.place(x = 55 , y = 410)

#製作巢穴編號Combobox下拉選單
		labelholeNum = Label(frame4, text = "巢穴編號", font=Font) 
		labelholeNum.pack()

		holeNum_Var = StringVar()
		holeNumlist = ttk.Combobox(frame4,textvariable = holeNum_Var, font = "微軟正黑體 13 normal",width = 13)
		holeNumlist["values"] = maplist.connect()
		holeNumlist.current(0)
		holeNumlist.configure(state = "readonly") #不能在選單內輸入文字
		holeNumlist.bind("<<ComboboxSelected>>",show)  #繫結事件,(下拉列表框被選中時，繫結go()函式)  
		holeNumlist.pack()

#製作返回主頁面的按鈕
		BackBN = Button(self.window, text = "返回", font=Font)
		BackBN.config(bg= "skyblue")
		BackBN.config(width = 10,height = 1)
		BackBN.config(command = self.gotoMain)
		BackBN.place(x = 93 , y = 487)
		

#製作右側顯示文字框架
		labelMonlist = Label(self.window, text = "出現寶可夢", font=Font) 
		labelMonlist.place(x = 407, y = 300)

		monlist = Listbox(self.window)
		monlist.config(height = 12, width = 41, font = FontMon, exportselection = False, borderwidth = 3, selectmode = "single",bg= "#b5e1f3")
		monlist.place(x = 290, y = 318)



		self.window.mainloop()


if __name__ == '__main__':

	window = Tk()
	Sub()
	window.mainloop() 