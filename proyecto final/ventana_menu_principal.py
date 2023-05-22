from cgitb import text
from select import select
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image 
import pymysql 
import estilos

def ventana_menu():
		global ventana4 
		ventana4 = Tk()
		ventana4.configure(bg=estilos.background)
		#---------------------Centrar-Ventana-----------------------------
		w = 655
		h = 300
		ws = ventana4.winfo_screenwidth()
		hs = ventana4.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana4.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
		ventana4.title("Inicio")
		ventana4.state("zoomed")
		
		#-------------Main Course--------------------------------------------
		Button(ventana4, text="Clientes", width="10", bg=estilos.color_bu, fg="white").place(x=10, y=20)		
		mainloop()
