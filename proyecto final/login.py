from cgitb import text
from select import select
from sqlite3 import Cursor
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
import estilos, idioma
import sqlite3


global guardar, var_buscar, id_seleccionado, dni_1
guardar = "Nuevo"
var_buscar = 0
#------------------------Ventana-de-Inicio----------------------------
class Loader:
	def __init__(self, master):
		self.master=master
		self.master.title("Pantalla de carga")
		self.master.geometry("300x250")
		self.master.resizable(0, 0)
		self.master.configure(bg=estilos.background)
		
		w = 350
		h = 350
		ws = self.master.winfo_screenwidth()
		hs = self.master.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
		
		self.label = tk.Label(self.master, text="Cargando...", fg="white", bg=estilos.background, font=("", 16))
		self.label.pack(pady=20)
		self.label.place(x=120,y=140)
		
		self.style = ttk.Style()
		self.style.theme_use('default')
		self.style.configure("#468189.Horizontal.TProgressbar", foreground='#468189', background='#468189')
		
		self.progressbar = tk.ttk.Progressbar(self.master, orient="horizontal", length=200, mode="indeterminate", style="#468189.Horizontal.TProgressbar")
		self.progressbar.pack(pady=10)
		self.progressbar.place(x=75,y=190)
		
		self.start()
		
	def start(self):
		self.progressbar.start(10)
		
	def stop(self):
		self.progressbar.stop()
		self.master.destroy()
		
if __name__ == "__main__":
	root=tk.Tk()
	app=Loader(root)
	root.after(2000, app.stop)
	root.mainloop()
	#-------------------------Ventana-Register----------------------------
def ventana_registrar_admin():
		
		global ventana2
		ventana2 = Tk()
		ventana2.configure(bg=estilos.background)
		#---------------------Centrar-Ventana-----------------------------
		w = 300
		h = 280
		ws = ventana2.winfo_screenwidth()
		hs = ventana2.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana2.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
		ventana2.title("Registrarse")
		#ventana2.iconbitmap("D:\\programacion IV\\proyecto final\\favicon.ico")
		ventana2.resizable(False, False)
		#---------------------------------------------------------------------
		def limpiar_caja_admin():
			usuario.set("")
			mail.set("")
			contrasena1.set("")
			contrasena2.set("")

		def registrar_admin():
			if(usuario.get() == ""):
				entry_usuario.focus()
				messagebox.showinfo("Faltan datos", "Ingrese Usuario")
				return
			elif (mail.get()==""):
				messagebox.showinfo("Faltan datos", "Ingrese Mail")
				entry_mail.focus()
				return
			elif(contrasena1.get()==""):
				messagebox.showinfo("Faltan datos", "Ingrese Contraseña")
				entry_constrasena.focus()
				return
			elif (contrasena2.get()==""):
				messagebox.showinfo("Faltan datos", "Repita Contraseña")
				entry_constrasena2.focus()
				return
			elif (contrasena1.get() != contrasena2.get()):
				messagebox.showinfo("Error","La contraseña no Coinciden")
				return

			basedatos = mydb = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
			fcursor = basedatos.cursor()

			fcursor.execute("SELECT Usuario FROM Admin1 WHERE Usuario='" + usuario.get() + "'")

			if fcursor.fetchall():
				messagebox.showinfo("Aviso", "Usuario ya Registrado")
			else:
				sql="INSERT INTO Admin1 (Usuario, Mail, Contrasena) VALUES ('{0}','{1}','{2}')".format(usuario.get(), mail.get(), contrasena1.get())
				fcursor.execute(sql)
				basedatos.commit()
				messagebox.showinfo("Registo", "Se registro el Usuario con exito")

				limpiar_caja_admin()
			basedatos.close()
		#-----------------------------------------------------------------
		Label(ventana2, text="Usuario", fg=("white"), bg=estilos.background, font=(estilos.fuenteComic,"10")).place(x=50, y=40)
		Label(ventana2, text="Mail", fg=("white"), bg=estilos.background, font=(estilos.fuenteComic,"10")).place(x=50, y=80)
		Label(ventana2, text="Contraseña", fg=("white"), bg=estilos.background, font=(estilos.fuenteComic,"10")).place(x=50, y=120)
		Label(ventana2, text="R. Contraseña", fg=("white"), bg=estilos.background, font=(estilos.fuenteComic,"10")).place(x=50, y=160)

		usuario = StringVar()
		mail = StringVar()
		contrasena1 = StringVar()
		contrasena2 = StringVar()

		entry_usuario = Entry(ventana2, textvariable=usuario)
		entry_usuario.pack()
		entry_usuario.place(x=140,y=40)

		entry_mail = Entry(ventana2, textvariable=mail)
		entry_mail.pack()
		entry_mail.place(x=140,y=80)

		entry_constrasena = Entry(ventana2, textvariable=contrasena1, show="*")
		entry_constrasena.pack()
		entry_constrasena.place(x=140,y=120)

		entry_constrasena2 = Entry(ventana2, textvariable=contrasena2, show="*")
		entry_constrasena2.pack()
		entry_constrasena2.place(x=140,y=160)

		Button(ventana2, text="Guardar", width="10", command=registrar_admin ,bg=estilos.color3,fg="white").place(x=18,y=220)
		Button(ventana2, text="Salir", width="10", command= deVentanaRegistrarAdmin_a_VentanaInicio,bg="red",fg="white").place(x=108,y=220)
		Button(ventana2, text="Cancelar", width="10", command=limpiar_caja_admin,bg=estilos.color4,fg="white").place(x=199, y=220)
		#-----------------------------------------------------------------

		mainloop()

def ventana_Login():
		global ventana3 
		ventana3 = Tk()
		ventana3.configure(bg=estilos.background)
		w = 800
		h = 349
		ws = ventana3.winfo_screenwidth()
		hs = ventana3.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana3.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
		ventana3.title("Iniciar Sesion")
		#ventana3.iconbitmap("D:\\programacion IV\\proyecto final\\favicon.ico")
		ventana3.resizable(False, False)
		#---------------------------------------------------------
		def cambiar_idioma(idioma):
			global ingles
			if idioma=="Ingles":
				pass
		#-----------------------------------------------------------------
		def login_admin():
			if(usuario3.get() == ""):
				entry_usuario3.focus()
				messagebox.showinfo("Faltan datos", "Ingrese Usuario")
				return
			elif(contrasena3.get()==""):
				messagebox.showinfo("Faltan datos", "Ingrese Contraseña")
				entry_constrasena3.focus()
				return
			
			basedatos = pmydb = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
			fcursor = basedatos.cursor()

			fcursor.execute("SELECT Usuario FROM Admin1 WHERE Usuario='" + usuario3.get() + "' and Contrasena='" + contrasena3.get() + "'")

			if fcursor.fetchall():
				deRegistro_a_escuela()
			else:
				messagebox.showinfo("Error", "Usuario y/o Contraseña Incorrecta")

			basedatos.close()
		
		def on_focus_in(event):
			if entry_usuario3.get() == default_text:
				entry_usuario3.delete(0, tk.END)
				entry_usuario3.config(show='')

		def on_focus_out(event):
			if entry_usuario3.get() == '':
				entry_usuario3.insert(0, default_text)
				entry_usuario3.config(show='')
				
		def on_focus_in_contrasena(event):
			if entry_constrasena3.get() == default_text_2:
				entry_constrasena3.delete(0, tk.END)
				entry_constrasena3.config(show='')

		def on_focus_out_contrasena(event):
			if entry_constrasena3.get() == '':
				entry_constrasena3.insert(0, default_text_2)
				entry_constrasena3.config(show='')
		
		#-----------------------------------------------------------------
		usuario3 = StringVar()
		contrasena3 = StringVar()
		
		default_text = "Ingrese Usuario"
		entry_usuario3 = Entry(ventana3, textvariable=usuario3,  width=20, font=("Comic sans", 12), bd=2, relief="flat")
		entry_usuario3.insert(0, default_text)
		entry_usuario3.configure(fg="#797979", font=("Arial Rounded", 12 )) 
		entry_usuario3.pack(pady=10)
		entry_usuario3.place(x=515, y=200)
		
		entry_usuario3.bind("<FocusIn>", on_focus_in)
		entry_usuario3.bind("<FocusOut>", on_focus_out)
		
		default_text_2="Ingrese Contraseña"
		entry_constrasena3 = Entry(ventana3, textvariable=contrasena3,show="*",  width=20, font=("Comic sans", 12), bd=2, relief="flat")
		entry_constrasena3.insert(0, default_text_2)
		entry_constrasena3.configure(fg="#797979", font=("Arial Rounded", 12 )) 
		entry_constrasena3.pack(pady=10)
		entry_constrasena3.place(x=515,y=230)
		
		entry_constrasena3.bind("<FocusIn>", on_focus_in_contrasena)
		entry_constrasena3.bind("<FocusOut>", on_focus_out_contrasena)
		
		opciones=["Español", "Ingles"]
		cmbx_idioma = ttk.Combobox(ventana3, values=opciones, state="readonly", width=8)
		cmbx_idioma.set("idioma:")
		cmbx_idioma.place(x=710, y=10)
		
		estilo = ttk.Style()
		estilo.configure('BotonRedondeado.TButton', borderwith=0, relief="flat", background='#62aea4', foreground="black", padding=6,  cursor="hand2")
		estilo.map('BotonRedondeado.TButton', background=[('active', '#2E5282')])
		
		estilo2 = ttk.Style()
		estilo2.configure('BotonRedondeado2.TButton', borderwith=0, relief="flat", background='#F34949', foreground="black", padding=6,  cursor="hand2")
		estilo2.map('BotonRedondeado2.TButton', background=[('active', '#FF0000')])

		boton_entrar= ttk.Button(ventana3, text="Entrar",command=login_admin, style='BotonRedondeado.TButton')
		boton_entrar.pack(pady=20)
		boton_entrar.place(x=515, y=280)
		
		boton_salir= ttk.Button(ventana3, text="Salir", command=salir_de_login, style='BotonRedondeado2.TButton')
		boton_salir.pack(pady=20)
		boton_salir.place(x=615, y=280)

		#----------------------------Imagen Login---------------------------------------
		
		imagen = Image.open("login_image.png")
		imagen_tk = ImageTk.PhotoImage(imagen)
		imagen_redimencionada = imagen.resize((400,350))
		imagen_tk = ImageTk.PhotoImage(imagen_redimencionada)
		label=Label(ventana3, image=imagen_tk, height="350", width="400").place(x=1, y=1)
		
		#-----------------------------imagen logo-------------------------------------------
		
		imagen2 = Image.open("logo_sgtr.png")
		imagen2_tk = ImageTk.PhotoImage(imagen2)
		imagen2_redimencionada = imagen2.resize((140,120))
		imagen2_tk = ImageTk.PhotoImage(imagen2_redimencionada)
		label2 = Label(ventana3, image=imagen2_tk, width="140", height="120", bg=estilos.background).place(x=540, y=45)
		
		#-----------------------------logo lenguaje---------------------
		
		imagen3 = Image.open("logo_lenguaje.png")
		imagen3_tk = ImageTk.PhotoImage(imagen3)
		imagen3_redimencionada = imagen3.resize((20,20))
		imagen3_tk = ImageTk.PhotoImage(imagen3_redimencionada)
		label3=Label(ventana3, image=imagen3_tk, height="20", width="20", bg=estilos.background).place(x=680, y=10)
		
		
		
		#----------------------Registrar adminastrador------------------
		imagen4 = Image.open("agregar_admin.png")
		imagen4_tk = ImageTk.PhotoImage(imagen4)
		imagen4_redimencionada = imagen4.resize((60,50))
		imagen4_tk = ImageTk.PhotoImage(imagen4_redimencionada)
		boton_admin=Button(ventana3, image=imagen4_tk, height="50", width="60", bg=estilos.background, command=deLogin_a_registrar, relief="flat", cursor="hand2").place(x=410, y=290)
		
		#---------------------------------------------------------------
		

		mainloop()
#----------------------------Ventana-Menu-----------------------------
def ventana_menu():
		global ventana4 
		ventana4 = Tk()
		ventana4.configure(bg=estilos.background)
		#---------------------Centrar-Ventana-----------------------------
		w = 650
		h = 300
		ws = ventana4.winfo_screenwidth()
		hs = ventana4.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana4.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
		ventana4.title("Inicio")
		ventana4.state("zoomed")
		#ventana4.iconbitmap("D:\\programacion IV\\proyecto final\\favicon.ico")
		ventana4.resizable(False, False)

		#-------------Main Course--------------------------------------------.

		menu = ttk.Treeview(ventana4, columns=("col1", "col2"), height="0")
		estilo=ttk.Style()
		estilo.theme_use("clam")
		
		menu.column("#0", width=80)
		menu.column("col1", width=80, anchor=CENTER)
		menu.column("col2", width=80, anchor=CENTER)
		
		estilo.configure("Treeview.Heading", background="#468189", relief="flat", foreground="white")
		menu.heading("#0", text="Clientes",command=menu_principal_a_cliente, anchor=CENTER)
		menu.heading("col1", text="Stock",command=menu_principal_a_stock, anchor=CENTER)
		menu.heading("col2", text="Vender", anchor=CENTER)
				
		menu.place(x=10, y=10)
		ventana4.mainloop()
		

def ventana_clientes():
		global ventana5 
		ventana5 = Tk()
		ventana5.configure(bg=estilos.background)
		#---------------------Centrar-Ventana-----------------------------
		w = 655
		h = 300
		ws = ventana5.winfo_screenwidth()
		hs = ventana5.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana5.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
		ventana5.title("Cliente")
		ventana5.state("zoomed")
		#ventana5.iconbitmap("D:\\programacion IV\\proyecto final\\favicon.ico")
		
		ventana5.resizable(False, False)
		
		agregar= Button(ventana5, text="Agregar Cliente", fg="white", bg=estilos.color2, command=abrir_agregar_cliente).place(x=1150, y=10)

		
		imagen = Image.open("flecha_volver.png")
		imagen_tk = ImageTk.PhotoImage(imagen)
		imagen_redimencionada = imagen.resize((50,50))
		imagen_tk = ImageTk.PhotoImage(imagen_redimencionada)
		boton = Button(ventana5, image=imagen_tk, bg=estilos.background, height="50", width="50", command=cliente_a_menu_principal, relief="flat", cursor="hand2").place(x=10, y=10)
		mainloop()

def ventana_stock():
		global ventana6
		ventana6 = Tk()
		ventana6.configure(bg=estilos.background)
		#---------------------Centrar-Ventana-----------------------------
		w = 655
		h = 300
		ws = ventana6.winfo_screenwidth()
		hs = ventana6.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana6.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
		ventana6.title("Stock")
		ventana6.state("zoomed")
		
		agregar= Button(ventana6, text="Agregar artículo", fg="white", bg=estilos.color2, command=abrir_agregar_articulo, relief="groove", cursor="hand2").place(x=1150, y=10)
		
		class App:
			def __init__(self, master):
				self.ventana6 = master
				self.Dibujarlista()
				self.returnAllElemnts()
				self.cursor()
				
			def returnAllElemnts(self):
				conn= sqlite3.connect('sistemproa.db')
				cursor = conn.cursor()
				cursor.excute("SELECT * FROM stock")
				rows = cursor.fetchall()
				
			
			def Dibujarlista(self):
				self.articulos = ttk.Treeview(self.ventana6, columns=(1, 2, 3, 4, 5, 6), show="headings", height="8")
				self.articulos.pack()
				estilo=ttk.Style()
				estilo.theme_use("clam")
				
				estilo=ttk.Style()
				estilo.theme_use("clam")
				
				estilo.configure("Treeview.Heading", background="#468189", relief="flat", foreground="white")
				self.articulos.heading(1, text="Marca")
				self.articulos.heading(2, text="Talle")
				self.articulos.heading(3, text="Estado")
				self.articulos.heading(4, text="Precio")
				self.articulos.heading(5, text="Tipo de usuario")
				self.articulos.heading(6, text="Tipo de prenda")
				self.articulos.column(4, anchor=CENTER)
					
				self.articulos.place(x=120, y=90)
						
		imagen = Image.open("flecha_volver.png")
		imagen_tk = ImageTk.PhotoImage(imagen)
		imagen_redimencionada = imagen.resize((50,50))
		imagen_tk = ImageTk.PhotoImage(imagen_redimencionada)
		boton = Button(ventana6, image=imagen_tk, bg=estilos.background, height="50", width="50", command=stock_a_menu_principal, relief="flat", cursor="hand2").place(x=10, y=10)
		
		app=App(ventana6)
		ventana6.mainloop()
def ventana_agregar_articulos():
		global ventana7
		ventana7 = Tk()
		ventana7.configure(bg=estilos.background)
		#---------------------Centrar-Ventana-----------------------------
		w = 300
		h = 300
		ws = ventana7.winfo_screenwidth()
		hs = ventana7.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana7.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
		ventana7.title("Agregar Artículos")
		#---------------------------------------------------------------
		
		def limpiar_caja_articulos():
			entry_marca.delete(0, END)
			entry_marca.delete(0, END)
			entry_talle.delete(0, END)
			entry_estado.delete(0, END)
			entry_precio.delete(0, END)
			entry_tipo_usuario.delete(0, END)
			entry_tipo_prenda.delete(0, END)
			
		def guardar_articulo():
			if entry_marca.get() == "":
				entry_marca.focus()
				messagebox.showinfo("Faltan datos", "Ingrese la marca")
				return
			elif entry_talle.get() =="":
				entry_talle.focus()
				messagebox.showinfo("Faltan datos", "Ingrese el talle")
				return
			elif cmbx_estado.get() =="Estado":
				cmbx_estado.focus()
				messagebox.showinfo("Faltan datos", "Seleccione el estado")
				return
				
			elif entry_precio.get() =="":
				entry_precio.focus()
				messagebox.showinfo("Faltan datos", "Ingrese el precio")
				return
			elif entry_tipo_usuario.get() =="":
				entry_tipo_usuario.focus()
				messagebox.showinfo("Faltan datos", "Ingrese el tipo de usuario")
				return
			elif entry_tipo_prenda.get() =="":
				entry_tipo_prenda.focus()
				messagebox.showinfo("Faltan datos", "Ingrese el tipo de prenda")
				return
				
			basedatos = mydb = pymysql.connect(host= "localhost", user="root", passwd="", db="sistemproa")
			fcursor = basedatos.cursor()

			sql="INSERT INTO articulos (marca, talle, estado, precio, tipo_usuario, tipo_prenda) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(marca.get(), talle.get(), estado.get(), precio.get(), tipo_usuario.get(), tipo_prenda.get())
			fcursor.execute(sql)
			basedatos.commit()
			messagebox.showinfo("Registro", "Se registró el articulo con exito")
			
			ventana7.destroy()
			limpiar_caja_articulos()
			basedatos.close()
		
		#----------------Labels, entry y botones-------------------------
		
		lbl_marca=Label(ventana7, text="Marca:", fg="white", bg=estilos.background).place(x=10, y=20)
		lbl_talle=Label(ventana7, text="Talle:", fg="white", bg=estilos.background).place(x=10, y=70)
		lbl_estado=Label(ventana7, text="Estado:", fg="white", bg=estilos.background).place(x=10, y=120)
		lbl_precio=Label(ventana7, text="Precio:", fg="white", bg=estilos.background).place(x=150, y=20)
		lbl_tipo_usuario=Label(ventana7, text="Tipo de usuario:", fg="white", bg=estilos.background).place(x=150, y=70)
		lbl_tipo_prenda=Label(ventana7, text="Tipo de prenda:", fg="white", bg=estilos.background).place(x=150, y=120)
		
		marca= StringVar()
		talle= StringVar()
		estado= StringVar()
		precio= StringVar()
		tipo_usuario= StringVar()
		tipo_prenda= StringVar()
		
		entry_marca= Entry(ventana7, textvariable=marca )
		entry_marca.pack()
		entry_marca.place(x=10,y=40)
		
		entry_talle= Entry(ventana7, textvariable=talle )
		entry_talle.pack()
		entry_talle.place(x=10,y=90)
		
		entry_precio= Entry(ventana7, textvariable=precio )
		entry_precio.pack()
		entry_precio.place(x=150,y=40)
		
		entry_tipo_usuario= Entry(ventana7, textvariable=tipo_usuario )
		entry_tipo_usuario.pack()
		entry_tipo_usuario.place(x=150,y=90)
		
		entry_tipo_prenda= Entry(ventana7, textvariable=tipo_prenda )
		entry_tipo_prenda.pack()
		entry_tipo_prenda.place(x=150,y=140)
		
		opciones= ["Nuevo", "Usado"]
		cmbx_estado= ttk.Combobox(ventana7, values=opciones, state="readonly", width=10)
		cmbx_estado.set("Estado:")
		cmbx_estado.place(x=10,y=140)
		
		btn_guardar= Button(ventana7, text="Guardar", bg=estilos.color3, fg="white", width=7, command=guardar_articulo,relief="groove", cursor="hand2").place(x=50,y=190)
		btn_cancelar= Button(ventana7, text="Cancelar", bg="red", fg="white", width=7, command=limpiar_caja_articulos,relief="groove", cursor="hand2").place(x=120,y=190)
		btn_salir= Button(ventana7, text="Salir", bg=estilos.color4, fg="white",width=7,command=cerrar_agregar_stock,relief="groove", cursor="hand2").place(x=190, y=190)
	
def ventana_agregar_clientes():
		global ventana8
		ventana8 = Tk()
		ventana8.configure(bg=estilos.background)
		#---------------------Centrar-Ventana-----------------------------
		w = 300
		h = 300
		ws = ventana8.winfo_screenwidth()
		hs = ventana8.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		ventana8.geometry('%dx%d+%d+%d' % (w, h, x, y))
		#-----------------------------------------------------------------
		ventana8.title("Agregar Cliente")
		
		#---------------------------------------------------------------
		Nombre=StringVar
		Apellido=StringVar
		Numero_Tel=StringVar
		Direccion=StringVar
		
		
		lbl_nombre=Label(ventana8, text="Nombre:", fg="white", bg=estilos.background).place(x=10,y=20)
		lbl_apellido=Label(ventana8, text="Apellido:", fg="white", bg=estilos.background).place(x=10,y=70)
		lbl_numero_tel=Label(ventana8, text="Número de telefono:", fg="white" , bg=estilos.background).place(x=10,y=120)
		lbl_dirección= Label(ventana8, text="Dirección:", fg="white", bg=estilos.background).place(x=10, y=170)
		
		nombre_entry = Entry(ventana8, textvariable=Nombre)
		nombre_entry.pack()
		nombre_entry.place(x=145, y=20)
		
		apellido_entry=Entry(ventana8, textvariable=Apellido)
		apellido_entry.pack()
		apellido_entry.place(x=145, y=70)
		
		numero_tel_entry=Entry(ventana8, textvariable=Numero_Tel)
		numero_tel_entry.pack()
		numero_tel_entry.place(x=145,y=120)
		
		direccion= Entry(ventana8, textvariable=Direccion)
		direccion.pack()
		direccion.place(x=145,y=170)
		
		guardad_btn= Button(ventana8, text="Guardar")
		
		
		
		ventana8.mainloop()
	
		

def deVentanaRegistrarAdmin_a_VentanaInicio():
	ventana2.destroy()
	ventana_Login()

def deLogin_a_registrar ():
	ventana3.destroy()
	ventana_registrar_admin()

def salir_de_login():
	ventana3.destroy()
	ventana_inicio()

def deRegistro_a_escuela():
	ventana3.destroy()
	ventana_menu()

def salir_de_estudiantes():
	ventana4.destroy()
	ventana_Login()



def menu_principal_a_cliente():
	ventana4.destroy()
	ventana_clientes()

def cliente_a_menu_principal():
	ventana5.destroy()
	ventana_menu()
	
def menu_principal_a_stock():
	ventana4.destroy()
	ventana_stock()
	
def stock_a_menu_principal():
	ventana6.destroy()
	ventana_menu()
	
def abrir_agregar_articulo():
	ventana_agregar_articulos()
	
def abrir_agregar_cliente():
	ventana_agregar_clientes()

def cerrar_agregar_stock():
	ventana7.destroy()
	

#-----------------------------------------------------------------------

def get_text():
    text = entry_usuario3.get()
    print("Texto ingresado:", text)
	
ventana_Login()

