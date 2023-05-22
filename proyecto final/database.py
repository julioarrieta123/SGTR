import pymysql
import sqlite3


class Data:
	def __init__(self):
			self.conn = pymysql.connect(host="localhost", 
			user="root", 
			password="",
			db="sistemproa")  

			 
	def Dibujarlista(self):
		self.articulos = ttk.Treeview(self.ventana6, columns=(1, 2, 3, 4, 5, 6), show="headings", height="8")
		estilo=ttk.Style()
		estilo.theme_use("clam")
			
		estilo.configure("Treeview.Heading", background="#468189", relief="flat", foreground="white", state=DISABLED)
		self.articulos.heading(1, text="Marca")
		self.articulos.heading(2, text="Talle")
		self.articulos.heading(3, text="Estado")
		self.articulos.heading(4, text="Precio")
		self.articulos.heading(5, text="Tipo de usuario")
		self.articulos.heading(6, text="Tipo de prenda")
		self.articulos.column(4, anchor=CENTER)
		self.articulos.place(x=140, y=90)
		

	
	def returnAllElemnts(self):
		conn= sqlite3.connect('sistemproa.db')
		cursor = conn.cursor()
		cursor.excute("SELECT * FROM stock")
		rows = cursor.fetchall()
