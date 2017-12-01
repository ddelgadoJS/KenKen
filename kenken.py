 #José Daniel Delgado Segura
#2015001500
#21-05-2015
#Programa 2 - Pasatiempo Aritmético KenKen

#————————————————————————————————————————————————————————————————————————centrar————————————————————————————————————————————————————————————————————————#
def centrar(ventana): #Centra la ventana que se abre. Todas las WIN la utilizan. Tomada de internet.
	ventana.update_idletasks()
	w=ventana.winfo_width()
	h=ventana.winfo_height()
	extraW=ventana.winfo_screenwidth()-w
	extraH=ventana.winfo_screenheight()-h
	ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))
#——————————————————————————————————————————————————————————————————————Fin centrar——————————————————————————————————————————————————————————————————————#
#——————————————————————————————————————————————————————————————————————Ventana Jugar————————————————————————————————————————————————————————————————————#
def FN_WIN_jugar ():
	s = 0
	m = 0
	h = 0
	
	WIN_menú.withdraw()
	WIN_configurar.withdraw()
	WIN_validar_completo.withdraw()

	global WIN_jugar
	global LBL_segundos
	global BTN_pausa
	global BTN_iniciar
	global BTN_menú_jugar
	global BTN_validar
	global BTN_reiniciar
	global BTN_terminar
	global TXT_nombre
	global nombre
	global default_horas
	global default_minutos
	global default_segundos

	WIN_jugar = Toplevel()
	LBL_segundos = Label
	BTN_menú_jugar = BTN_pausa = BTN_iniciar = BTN_validar = BTN_reiniciar = BTN_terminar = Button
	TXT_nombre = Entry
	nombre = StringVar()
	nombre.set("Nombre")

	WIN_jugar.protocol("WM_DELETE_WINDOW", lambda : WIN_jugar.destroy())
	
	WIN_jugar.geometry("1000x600")
	WIN_jugar.title("Juego KENKEN")
	WIN_jugar.resizable(width = FALSE, height = FALSE)
	centrar (WIN_jugar)

	cuadrícula()

	TXT_nombre = Entry(WIN_jugar, textvariable = nombre, width = 20, font = ("Helvetica Neue", 15, "bold"))
	TXT_nombre.place(x = 760, y = 120)

	LBL_título = Label(WIN_jugar, text = "KenKen",font = ("Helvetica Neue", 20, "bold")).place(x = 320, y = 10)
	LBL_horas = Label(WIN_jugar, text = "Horas", font = ("Helvetica Neue", 13)).place(x = 768, y = 20)
	LBL_minutos = Label(WIN_jugar, text = "Minutos", font = ("Helvetica Neue", 13)).place(x = 825, y = 20)
	LBL_segundos = Label(WIN_jugar, text = "Segundos", font = ("Helvetica Neue", 13)).place(x = 891, y = 20)

	LBL_iniciar = Label(WIN_jugar, text = "Iniciar", font = ("Helvetica Neue", 13, "bold")).place(x = 782, y = 233)
	LBL_terminar = Label(WIN_jugar, text = "Terminar", font = ("Helvetica Neue", 13, "bold")).place(x = 880, y = 233)
	LBL_otro = Label(WIN_jugar, text = "Otro", font = ("Helvetica Neue", 13, "bold")).place(x = 787, y = 343)
	LBL_reiniciar = Label(WIN_jugar, text = "Reiniciar", font = ("Helvetica Neue", 13, "bold")).place(x = 886, y = 343)
	LBL_validar = Label(WIN_jugar, text = "Validar", font = ("Helvetica Neue", 13, "bold"))
	LBL_validar.place(x = 780, y = 453)
	LBL_top10 = Label(WIN_jugar, text = "Top 10", font = ("Helvetica Neue", 13, "bold"))
	LBL_top10.place(x = 889, y = 453)
	LBL_menú = Label(WIN_jugar, text = "Menú", font = ("Helvetica Neue", 13, "bold"))
	LBL_menú.place(x = 842, y = 571)

	BTN_iniciar = Button(WIN_jugar, image = IMG_BTN_WIN_jugar_iniciar, height = 65, width = 65, borderwidth = 0, command = FN_iniciar)
	BTN_iniciar.place (x = 775, y = 165)
	BTN_terminar = Button(WIN_jugar, image = IMG_BTN_WIN_jugar_terminar, height = 65, width = 65, borderwidth = 0, command = FN_terminar)
	BTN_terminar.place (x = 885, y = 165)
	BTN_otro = Button(WIN_jugar, image = IMG_BTN_WIN_jugar_otro, height = 65, width = 65, borderwidth = 0, command = lambda : FN_otro("otro"))
	BTN_otro.place (x = 775, y = 275)
	BTN_reiniciar = Button(WIN_jugar, image = IMG_BTN_WIN_jugar_reiniciar, height = 65, width = 65, borderwidth = 0, command = FN_reiniciar)
	BTN_reiniciar.place (x = 885, y = 275)
	BTN_validar = Button(WIN_jugar, image = IMG_BTN_WIN_jugar_validar, height = 65, width = 65, borderwidth = 0, command = FN_validar)
	BTN_validar.place (x = 775, y = 385)
	BTN_top10 = Button(WIN_jugar, image = IMG_BTN_WIN_jugar_top10, height = 65, width = 65, borderwidth = 0, command = WIN_top10)
	BTN_top10.place (x = 885, y = 385)
	BTN_menú_jugar = Button(WIN_jugar, image = IMG_BTN_menú, height = 65, width = 65, borderwidth = 0, command = menú_volver)
	BTN_menú_jugar.place (x = 832, y = 495)

	if validar_completo_respuesta.get() == 1:
		BTN_validar_completo = Button(WIN_jugar, image = IMG_BTN_WIN_validar_completo, height = 65, width = 65, borderwidth = 0, command = FN_validar_completo)
		BTN_validar_completo.place (x = 885, y = 385)

		BTN_menú_jugar.place (x = 775, y = 495)
		BTN_top10.place (x = 885, y = 495)

		LBL_validar_completo = Label(WIN_jugar, text = "Validar\ncompleto", font = ("Helvetica Neue", 13, "bold"))
		LBL_validar_completo.place(x = 882, y = 453)
		LBL_validar.place(x = 780, y = 453)
		LBL_top10.place(x = 889, y = 562)
		LBL_menú.place(x = 785, y = 562)

	if int(reloj_selec.get()) == 0:
		LBL_horas = Label(WIN_jugar, text = "Horas", font = ("Helvetica Neue", 13)).place(x = 768, y = 20)
		LBL_minutos = Label(WIN_jugar, text = "Minutos", font = ("Helvetica Neue", 13)).place(x = 825, y = 20)
		LBL_segundos = Label(WIN_jugar, text = "Segundos", font = ("Helvetica Neue", 13)).place(x = 891, y = 20)
		time.sleep(0.40)
		LBL_clock = Label(WIN_jugar, text = " "+"0"+str(h) + "       " + "0"+str(m) + "        " + "0"+str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)

		BTN_pausa = Button(WIN_jugar, height = 1, width = 5, text = "Pausa", borderwidth = 1, font = ("Helvetica Neue", 16), command = FN_pausa, state = DISABLED)
		BTN_pausa.place (x = 830, y = 75)
	
	elif int(reloj_selec.get()) == 2:
		h = int(default_horas.get())
		m = int(default_minutos.get())
		s = int(default_segundos.get())

		default_horas.set(h)
		default_minutos.set(m)
		default_segundos.set(s)

		SPNBX_horas = Spinbox(WIN_jugar, width = 2, font = ("Helvetica Neue", 12), from_ = 0, to = 3, textvariable = default_horas, wrap = True).place(x = 775, y = 44)
		SPNBX_minutos = Spinbox(WIN_jugar, width = 2, font = ("Helvetica Neue", 12), from_ = 0, to = 59, textvariable = default_minutos, wrap = True).place(x = 840, y = 44)
		SPNBX_segundos = Spinbox(WIN_jugar, width = 2, font = ("Helvetica Neue", 12), from_ = 0, to = 59, textvariable = default_segundos, wrap = True).place(x = 915, y = 44)
		BTN_pausa = Button(WIN_jugar, height = 1, width = 5, text = "Pausa", borderwidth = 1, font = ("Helvetica Neue", 16), command = FN_pausa, state = DISABLED)
		BTN_pausa.place (x = 830, y = 75)
#———————————————————————————————————————————————————————————————Clock——————————————————————————————————————————————————————————————#
def FN_THRDs ():
	terminar = False
	THRD_FN_WIN_jugar = Thread (target = FN_WIN_jugar, args = ())
	THRD_FN_WIN_jugar.start()
	
def FN_iniciar ():
	global iniciado 
	iniciado = True
	global terminar
	terminar = False
	BTN_menú_jugar.config(state = DISABLED)
	if nombre.get() == "Nombre" or len(nombre.get()) < 3 or len(nombre.get()) > 30:
		messagebox.showerror("Error en el nombre", "Debe ingresar un nombre correcto antes de iniciar (3 a 40 caracteres).")
		return

	BTN_pausa.config (state = NORMAL)
	BTN_iniciar.config(state = DISABLED)
	TXT_nombre.config(state = DISABLED)
	sel = nivel_selec.get()

	if sel == 33:
		lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45]
		for i in lista_btn:
			i.config(state = NORMAL)
	elif sel == 44:
		lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_btn:
			i.config(state = NORMAL)
	elif sel == 55:
		lista_btn = [BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_btn:
			i.config(state = NORMAL)
	elif sel == 0:
		lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_btn:
			i.config(state = NORMAL)
	elif sel == 77:
		lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_btn:
			i.config(state = NORMAL)
	elif sel == 88:
		lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_btn:
			i.config(state = NORMAL)
	elif sel == 99:
		lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
		for i in lista_btn:
			i.config(state = NORMAL)

	if int(reloj_selec.get()) == 0:
		THRD_clock = Thread (target = clock, args = ())
		THRD_clock.start()

	elif int(reloj_selec.get()) == 2:
		THRD_FN_timer = Thread(target = FN_timer, args = ())
		THRD_FN_timer.start()

def FN_pausa ():
	global pausa

	if pausa == False:
		pausa = True
	else:
		pausa = False

def clock(): 
	global h
	global m	
	global s

	global clock_estado
	clock_estado = True

	if default_horas.get() == "":
		h = 0
	if default_minutos.get() == "":
		m = 0
	if default_segundos.get() == "":
		s = 0
	else:
		h = int(default_horas.get())
		m = int(default_minutos.get())
		s = int(default_segundos.get())
	
	while h <= 23:
		if terminar == True:
			LBL_clock = Label(WIN_jugar, text = " "+"0"+ "0" + "       " + "0"+ "0" + "        " + "0"+ "0" +" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			return
		if pausa == False: #Comprueba que no haya una señal de pausa. Si es False no lo hay.
			time.sleep(0.99)
			s += 1
			if m == 59 and s == 60:
				h += 1
				m = 0
				s = 0
			elif s == 60:
				m += 1
				s = 0
			if s < 10 and m < 10 and h < 10:
				LBL_segundos = Label(WIN_jugar, text = " "+"0"+str(h) + "       " + "0"+str(m) + "        " + "0"+str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			elif s >= 10 and m < 10 and h < 10:
				LBL_segundos = Label(WIN_jugar, text = " "+"0"+str(h) + "       " + "0"+str(m) + "        " + str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			elif s >= 10 and m >= 10 and h < 10:
				LBL_segundos = Label(WIN_jugar, text = " "+"0"+str(h) + "       " + str(m) + "        " + str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			elif s < 10 and m < 10 and h >= 10:
				LBL_segundos = Label(WIN_jugar, text = " "+str(h) + "       " + "0"+str(m) + "        " + "0"+str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			elif s < 10 and m >= 10 and h >= 10:
				LBL_segundos = Label(WIN_jugar, text = " "+str(h) + "       " + str(m) + "        " + "0"+str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			elif s < 10 and m >= 10 and h < 10:
				LBL_segundos = Label(WIN_jugar, text = " "+"0"+str(h) + "       " + str(m) + "        " + "0"+str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			else:
				LBL_segundos = Label(WIN_jugar, text = " "+str(h) + "       " + str(m) + "        " + str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
		if h == 23 and m == 59 and s == 59:
			break
	messagebox.showinfo("Fin","Fin del juego, límite de reloj alcanzado.")
#—————————————————————————————————————————————————————————————Fin Clock————————————————————————————————————————————————————————————#
#————————————————————————————————————————————————————————————Cuadrícula————————————————————————————————————————————————————————————#
def cuadrícula():
	sel = nivel_selec.get()
	global BTN_00
	global BTN_01
	global BTN_02
	global BTN_03
	global BTN_04
	global BTN_05
	global BTN_06
	global BTN_07
	global BTN_08
	global BTN_10
	global BTN_11
	global BTN_12
	global BTN_13
	global BTN_14
	global BTN_15
	global BTN_16
	global BTN_17
	global BTN_18
	global BTN_20
	global BTN_21
	global BTN_22
	global BTN_23
	global BTN_24
	global BTN_25
	global BTN_26
	global BTN_27
	global BTN_28
	global BTN_30
	global BTN_31
	global BTN_32
	global BTN_33
	global BTN_34
	global BTN_35
	global BTN_36
	global BTN_37
	global BTN_38
	global BTN_40
	global BTN_41
	global BTN_42
	global BTN_43
	global BTN_44
	global BTN_45
	global BTN_46
	global BTN_47
	global BTN_48
	global BTN_50
	global BTN_51
	global BTN_52
	global BTN_53
	global BTN_54
	global BTN_55
	global BTN_56
	global BTN_57
	global BTN_58
	global BTN_60
	global BTN_61
	global BTN_62
	global BTN_63
	global BTN_64
	global BTN_65
	global BTN_66
	global BTN_67
	global BTN_68
	global BTN_70
	global BTN_71
	global BTN_72
	global BTN_73
	global BTN_74
	global BTN_75
	global BTN_76
	global BTN_77
	global BTN_78
	global BTN_80
	global BTN_81
	global BTN_82
	global BTN_83
	global BTN_84
	global BTN_85
	global BTN_86
	global BTN_87
	global BTN_88
	global BTN_num1
	global BTN_num2
	global BTN_num3
	global BTN_num4
	global BTN_num5
	global BTN_num6
	global BTN_num7
	global BTN_num8
	global BTN_num9
	global BTN_borrar
	BTN_00=BTN_01=BTN_02=BTN_03=BTN_04=BTN_05=BTN_06=BTN_07=BTN_08=BTN_10=BTN_11=BTN_12=BTN_13=BTN_14=BTN_15=BTN_16=BTN_17=BTN_18=BTN_20=BTN_21=BTN_22=BTN_23=BTN_24=BTN_25=BTN_26=BTN_27=BTN_28=BTN_30=BTN_31=BTN_32=BTN_33=BTN_34=BTN_35=BTN_36=BTN_37=BTN_38=BTN_40=BTN_41=BTN_42=BTN_43=BTN_44=BTN_45=BTN_46=BTN_47=BTN_48=BTN_50=BTN_51=BTN_52=BTN_53=BTN_54=BTN_55=BTN_56=BTN_57=BTN_58 = Button
	BTN_60=BTN_61=BTN_62=BTN_63=BTN_64=BTN_65=BTN_66=BTN_67=BTN_68=BTN_70=BTN_71=BTN_72=BTN_73=BTN_74=BTN_75=BTN_76=BTN_77=BTN_78=BTN_80=BTN_81=BTN_82=BTN_83=BTN_84=BTN_85=BTN_86=BTN_87=BTN_88=BTN_90=BTN_91=BTN_92=BTN_93=BTN_94=BTN_95=BTN_96=BTN_97=BTN_98=BTN_num1=BTN_num2=BTN_num3=BTN_num4=BTN_num5=BTN_num6=BTN_num7=BTN_num8=BTN_num9=BTN_borrar = Button

	BTN_num1 = Button(WIN_jugar, height = 50, width = 50, image = IMG_BTN_num1, borderwidth = 0, command = lambda : FN_add("1"))
	BTN_num2 = Button(WIN_jugar, height = 50, width = 50, image = IMG_BTN_num2, borderwidth = 0, command = lambda : FN_add("2"))
	BTN_num3 = Button(WIN_jugar, height = 50, width = 50, image = IMG_BTN_num3, borderwidth = 0, command = lambda : FN_add("3"))
	BTN_num4 = Button(WIN_jugar, height = 50, width = 50, image = IMG_BTN_num4, borderwidth = 0, command = lambda : FN_add("4"))
	BTN_num5 = Button(WIN_jugar, height = 50, width = 50, image = IMG_BTN_num5, borderwidth = 0, command = lambda : FN_add("5"))
	BTN_num6 = Button(WIN_jugar, height = 50, width = 50, image = IMG_BTN_num6, borderwidth = 0, command = lambda : FN_add("6"))
	BTN_num7 = Button(WIN_jugar, height = 50, width = 50, image = IMG_BTN_num7, borderwidth = 0, command = lambda : FN_add("7"))
	BTN_num8 = Button(WIN_jugar, height = 50, width = 50, image = IMG_BTN_num8, borderwidth = 0, command = lambda : FN_add("8"))
	BTN_num9 = Button(WIN_jugar, height = 50, width = 50, image = IMG_BTN_num9, borderwidth = 0, command = lambda : FN_add("9"))
	BTN_borrar = Button(WIN_jugar, image = IMG_BTN_WIN_jugar_borrar, height = 65, width = 65, borderwidth = 0, command = FN_borrar)
	
	if sel == 33 or sel == 44 or sel == 55 or sel == 0 or sel == 77 or sel == 88 or sel == 99:
		BTN_23 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("23"), state = DISABLED) 
		BTN_23.place (x = 285, y = 164)
		BTN_24 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("24"), state = DISABLED)
		BTN_24.place (x = 345, y = 164)
		BTN_25 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("25"), state = DISABLED)
		BTN_25.place (x = 405, y = 164)
		BTN_33 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("33"), state = DISABLED)
		BTN_33.place (x = 285, y = 216)
		BTN_34 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("34"), state = DISABLED)
		BTN_34.place (x = 345, y = 216)
		BTN_35 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("35"), state = DISABLED)
		BTN_35.place (x = 405, y = 216)
		BTN_43 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("43"), state = DISABLED)
		BTN_43.place (x = 285, y = 268)
		BTN_44 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("44"), state = DISABLED)
		BTN_44.place (x = 345, y = 268)
		BTN_45 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("45"), state = DISABLED)
		BTN_45.place (x = 405, y = 268)

		if lado_selec.get() == 0:
			BTN_num1.place (x = 680, y = 30)
			BTN_num2.place (x = 680, y = 90)
			BTN_num3.place (x = 680, y = 150)
			BTN_borrar.place (x = 677, y = 220)
		else:
			BTN_num1.place (x = 20, y = 30)
			BTN_num2.place (x = 20, y = 90)
			BTN_num3.place (x = 20, y = 150)
			BTN_borrar.place (x = 17, y = 220)
	
	if sel == 44 or sel == 55 or sel == 0 or sel == 77 or sel == 88 or sel == 99:
		BTN_22 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("22"), state = DISABLED)
		BTN_22.place (x = 225, y = 164)
		BTN_32 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("32"), state = DISABLED)
		BTN_32.place (x = 225, y = 216)
		BTN_42 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("42"), state = DISABLED)
		BTN_42.place (x = 225, y = 268)
		BTN_52 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("52"), state = DISABLED)
		BTN_52.place (x = 225, y = 320)
		BTN_53 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("53"), state = DISABLED)
		BTN_53.place (x = 285, y = 320)
		BTN_54 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("54"), state = DISABLED)
		BTN_54.place (x = 345, y = 320)
		BTN_55 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("55"), state = DISABLED)
		BTN_55.place (x = 405, y = 320)

		if lado_selec.get() == 0:
			BTN_num4.place (x = 680, y = 210)
			BTN_borrar.place (x = 677, y = 280)
		else:
			BTN_num4.place (x = 20, y = 210)
			BTN_borrar.place (x = 17, y = 280)

	if sel == 55 or sel == 0 or sel == 77 or sel == 88 or sel == 99:
		BTN_26 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("26"), state = DISABLED)
		BTN_26.place (x = 465, y = 164)
		BTN_36 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("36"), state = DISABLED)
		BTN_36.place (x = 465, y = 216)
		BTN_46 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("46"), state = DISABLED)
		BTN_46.place (x = 465, y = 268)
		BTN_56 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("56"), state = DISABLED)
		BTN_56.place (x = 465, y = 320)
		BTN_62 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("62"), state = DISABLED)
		BTN_62.place (x = 225, y = 372)
		BTN_63 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("63"), state = DISABLED)
		BTN_63.place (x = 285, y = 372)
		BTN_64 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("64"), state = DISABLED)
		BTN_64.place (x = 345, y = 372)
		BTN_65 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("65"), state = DISABLED)
		BTN_65.place (x = 405, y = 372)
		BTN_66 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("66"), state = DISABLED)
		BTN_66.place (x = 465, y = 372)
		if lado_selec.get() == 0:
			BTN_num5.place (x = 680, y = 270)
			BTN_borrar.place (x = 677, y = 340)
		else:
			BTN_num5.place (x = 20, y = 270)
			BTN_borrar.place (x = 17, y = 340)
	
	if sel == 0 or sel == 77 or sel == 88 or sel == 99:
		BTN_11 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("11"), state = DISABLED)
		BTN_11.place (x = 165, y = 112)
		BTN_12 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("12"), state = DISABLED)
		BTN_12.place (x = 225, y = 112)
		BTN_13 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("13"), state = DISABLED)
		BTN_13.place (x = 285, y = 112)
		BTN_14 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("14"), state = DISABLED)
		BTN_14.place (x = 345, y = 112)
		BTN_15 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("15"), state = DISABLED)
		BTN_15.place (x = 405, y = 112)
		BTN_16 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("16"), state = DISABLED)
		BTN_16.place (x = 465, y = 112)
		BTN_21 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("21"), state = DISABLED)
		BTN_21.place (x = 165, y = 164)
		BTN_31 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("31"), state = DISABLED)
		BTN_31.place (x = 165, y = 216)
		BTN_41 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("41"), state = DISABLED)
		BTN_41.place (x = 165, y = 268)
		BTN_51 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("51"), state = DISABLED)
		BTN_51.place (x = 165, y = 320)
		BTN_61 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("61"), state = DISABLED)
		BTN_61.place (x = 165, y = 372)
		if lado_selec.get() == 0:
			BTN_num6.place (x = 680, y = 330)
			BTN_borrar.place (x = 677, y = 400)
		else:
			BTN_num6.place (x = 20, y = 330)
			BTN_borrar.place (x = 17, y = 400)

	if sel == 77 or sel == 88 or sel == 99:
		BTN_17 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("17"), state = DISABLED)
		BTN_17.place (x = 525, y = 112)
		BTN_27 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("27"), state = DISABLED)
		BTN_27.place (x = 525, y = 164)
		BTN_37 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("37"), state = DISABLED)
		BTN_37.place (x = 525, y = 216)
		BTN_47 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("47"), state = DISABLED)
		BTN_47.place (x = 525, y = 268)
		BTN_57 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("57"), state = DISABLED)
		BTN_57.place (x = 525, y = 320)
		BTN_67 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("67"), state = DISABLED)
		BTN_67.place (x = 525, y = 372)
		BTN_71 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("71"), state = DISABLED)
		BTN_71.place (x = 165, y = 424)
		BTN_72 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("72"), state = DISABLED)
		BTN_72.place (x = 225, y = 424)
		BTN_73 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("73"), state = DISABLED)
		BTN_73.place (x = 285, y = 424)
		BTN_74 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("74"), state = DISABLED)
		BTN_74.place (x = 345, y = 424)
		BTN_75 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("75"), state = DISABLED)
		BTN_75.place (x = 405, y = 424)
		BTN_76 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("76"), state = DISABLED)
		BTN_76.place (x = 465, y = 424)
		BTN_77 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("77"), state = DISABLED)
		BTN_77.place (x = 525, y = 424)
		if lado_selec.get() == 0:
			BTN_num7.place (x = 680, y = 390)
			BTN_borrar.place (x = 677, y = 460)
		else:
			BTN_num7.place (x = 20, y = 390)
			BTN_borrar.place (x = 17, y = 460)

	if sel == 88 or sel == 99:
		BTN_00 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("00"), state = DISABLED)
		BTN_00.place (x = 105, y = 60)
		BTN_01 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("01"), state = DISABLED)
		BTN_01.place (x = 165, y = 60)
		BTN_02 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("02"), state = DISABLED)
		BTN_02.place (x = 225, y = 60)
		BTN_03 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("03"), state = DISABLED)
		BTN_03.place (x = 285, y = 60)
		BTN_04 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("04"), state = DISABLED)
		BTN_04.place (x = 345, y = 60)
		BTN_05 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("05"), state = DISABLED)
		BTN_05.place (x = 405, y = 60)
		BTN_06 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("06"), state = DISABLED)
		BTN_06.place (x = 465, y = 60)
		BTN_07 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("07"), state = DISABLED)
		BTN_07.place (x = 525, y = 60)
		BTN_10 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("10"), state = DISABLED)
		BTN_10.place (x = 105, y = 112)
		BTN_20 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("20"), state = DISABLED)
		BTN_20.place (x = 105, y = 164)
		BTN_30 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("30"), state = DISABLED)
		BTN_30.place (x = 105, y = 216)
		BTN_40 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("40"), state = DISABLED)
		BTN_40.place (x = 105, y = 268)
		BTN_50 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("50"), state = DISABLED)
		BTN_50.place (x = 105, y = 320)
		BTN_60 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("60"), state = DISABLED)
		BTN_60.place (x = 105, y = 372)
		BTN_70 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("70"), state = DISABLED)
		BTN_70.place (x = 105, y = 424)
		if lado_selec.get() == 0:
			BTN_num8.place (x = 680, y = 450)
			BTN_borrar.place (x = 677, y = 520)
		else:
			BTN_num8.place (x = 20, y = 450)
			BTN_borrar.place (x = 17, y = 520)

	if sel == 99:
		BTN_08 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("08"), state = DISABLED)
		BTN_08.place (x = 585, y = 60)
		BTN_18 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("18"), state = DISABLED)
		BTN_18.place (x = 585, y = 112)
		BTN_28 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("28"), state = DISABLED)
		BTN_28.place (x = 585, y = 164)
		BTN_38 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("38"), state = DISABLED)
		BTN_38.place (x = 585, y = 216)
		BTN_48 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("48"), state = DISABLED)
		BTN_48.place (x = 585, y = 268)
		BTN_58 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("58"), state = DISABLED)
		BTN_58.place (x = 585, y = 320)
		BTN_68 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("68"), state = DISABLED)
		BTN_68.place (x = 585, y = 372)
		BTN_78 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("78"), state = DISABLED)
		BTN_78.place (x = 585, y = 424)
		BTN_80 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("80"), state = DISABLED)
		BTN_80.place (x = 105, y = 476)
		BTN_81 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("81"), state = DISABLED)
		BTN_81.place (x = 165, y = 476)
		BTN_82 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("82"), state = DISABLED)
		BTN_82.place (x = 225, y = 476)
		BTN_83 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = ("Helvetica Neue", 12, "bold"), borderwidth = 2, command = lambda : FN_BTNS("83"), state = DISABLED)
		BTN_83.place (x = 285, y = 476)
		BTN_84 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("84"), state = DISABLED)
		BTN_84.place (x = 345, y = 476)
		BTN_85 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("85"), state = DISABLED)
		BTN_85.place (x = 405, y = 476)
		BTN_86 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("86"), state = DISABLED)
		BTN_86.place (x = 465, y = 476)
		BTN_87 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("87"), state = DISABLED)
		BTN_87.place (x = 525, y = 476)
		BTN_88 = Button(WIN_jugar, height = 2, width = 5, bg = "white", font = (("Helvetica Neue", 12, "bold")), borderwidth = 2, command = lambda : FN_BTNS("88"), state = DISABLED)
		BTN_88.place (x = 585, y = 476)
		if lado_selec.get() == 0:
			BTN_num9.place (x = 680, y = 510)
			BTN_borrar.place (x = 585, y = 530)
		else:
			BTN_num9.place (x = 20, y = 510)
			BTN_borrar.place (x = 100, y = 530)

	cuadrícula_color()

def FN_juegos_probables(índice, lista_completa):
	global elegido
	global juegos_probables
	global juego_num
	if juego_num == 0:
		juegos_probables = []
		
		contador = 0
		for i in lista_completa[índice]:
			juegos_probables.append(contador)
			contador += 1
		elegido = random.choice(juegos_probables)
		juegos_probables.remove(elegido)
	elif otro_juego == True:
		elegido = random.choice(juegos_probables)
		juegos_probables.remove(elegido)
	return elegido

def cuadrícula_color():
	TXT_cuadrículas = open("kenken_juegos.dat","r")
	TXT_cuadrículas_read = TXT_cuadrículas.read()
	string = "["
	lista_completa = []
	lista_nivel = []
	lista_juego = []
	contador = 0
	contador_nivel = 0

	TXT_operaciones = open("Operaciones.txt","r")
	TXT_operaciones_leer = TXT_operaciones.read()
	string2 = "["
	lista_completa2 = []
	lista_nivel2 = []
	contador_nivel2 = 0

	global juego_num
	global lst_juego_validar
	global lst_validar
	global lst_operaciones
	global juego_num
	global últ_btn
	global lst_colores
	global otro_juego
	lst_colores = ["HotPink", "BlueViolet", "Sienna", "DarkGreen", "DarkMagenta", "DarkKhaki", "MediumSlateBlue", "SeaGreen", "LightSlateGrey", "Indigo", "Teal", "Olive", "LightSalmon", "Lime", "Orchid", "ForestGreen", "Gold", "MediumAquaMarine", "CadetBlue", "DarkGrey", "MediumVioletRed", "Magenta", "Plum", "Navy", "SpringGreen", "SkyBlue", "DarkOrange", "SandyBrown", "MediumBlue", "SaddleBrown", "RoyalBlue", "Tomato", "Brown", "RosyBrown", "SteelBlue", "BurlyWood", "DodgerBlue", "OrangeRed", "Khaki", "GreenYellow"]
	índ_color = 0
	contador_lst_colores = 0
	sel = nivel_selec.get()
	contador_for = 0

	if sel == 33:
		índice = 0
	elif sel == 44:
		índice = 1
	elif sel == 55:
		índice = 2
	elif sel == 0:
		índice = 3
	elif sel == 77:
		índice = 4
	elif sel == 88:
		índice = 5
	elif sel == 99:
		índice = 6

	for i in TXT_cuadrículas_read:
		if i != "[" and i != "]":
			string += i
			contador_control = 1
		elif i == "]" and contador_control != 0:
			string += i
			lista_nivel.append(eval(string))
			string = "["
			contador_nivel += 1
		if contador_nivel == 4:
			lista_completa.append(lista_nivel)
			lista_nivel = []
			contador_nivel = 0
			contador_control = 0

	if juego_num == 0 or otro_juego == True:
		elegido = FN_juegos_probables(índice, lista_completa)
		lst_juego_validar = lista_completa[índice][elegido]
		lst_validar = []
		lst_temporal = []

		for r in lista_completa[índice][elegido]:
			for z in r:
				lst_temporal.append("")
			lst_validar.append(lst_temporal)
			lst_temporal = []

		for y in TXT_operaciones_leer:
			if y != "[" and y != "]":
				string2 += y
				contador_control = 1
			elif y == "]" and contador_control != 0:
				string2 += y
				lista_nivel2.append(eval(string2))
				string2 = "["
				contador_nivel2 += 1
			if contador_nivel2 == 4:
				lista_completa2.append(lista_nivel2)
				lista_nivel2 = []
				contador_nivel2 = 0
				contador_control = 0

		lst_operaciones = lista_completa2[índice][elegido]

	elif juego_num != 0 and pausa == True:
		FN_pausa ()
	for j in lst_juego_validar:
		contador_for += 1
		if len(lst_colores) - índ_color == 1:
			índ_color = 0
		for f in j:
			if sel == 33:
				lista_nom = ["23","24","25","33","34","35","43","44","45"]
				lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45]
				for p in lista_nom:	
					if str(f) == p and str(f) != but_press:
						índ_nom = lista_nom.index(p)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = lst_colores[índ_color], relief = RAISED)
					if juego_num == 0 and contador_for == 1:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
					elif contador_for == 1 and otro_juego == True:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
			elif sel == 44:
				lista_nom = ["23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
				lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
				for p in lista_nom:
					if str(f) == p and str(f) != but_press:
						índ_nom = lista_nom.index(p)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = lst_colores[índ_color], relief = RAISED)
					if juego_num == 0 and contador_for == 1:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
					elif contador_for == 1 and otro_juego == True:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
			elif sel == 55:
				lista_nom = ["26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
				lista_btn = [BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
				for p in lista_nom:
					if str(f) == p and str(f) != but_press:
						índ_nom = lista_nom.index(p)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = lst_colores[índ_color], relief = RAISED)
					if juego_num == 0 and contador_for == 1:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
					elif contador_for == 1 and otro_juego == True:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
			elif sel == 0:
				lista_nom = ["11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
				lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
				for p in lista_nom:
					if str(f) == p and str(f) != but_press:
						índ_nom = lista_nom.index(p)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = lst_colores[índ_color], relief = RAISED)
					if juego_num == 0 and contador_for == 1:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
					elif contador_for == 1 and otro_juego == True:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
			elif sel == 77:
				lista_nom = ["17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
				lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
				for p in lista_nom:
					if str(f) == p and str(f) != but_press:
						índ_nom = lista_nom.index(p)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = lst_colores[índ_color], relief = RAISED)
					if juego_num == 0 and contador_for == 1:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
					elif contador_for == 1 and otro_juego == True:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
			elif sel == 88:
				lista_nom = ["00","01","02","03","04","05","06","07","10","20","30","40","50","60","70","17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
				lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
				for p in lista_nom:
					if str(f) == p and str(f) != but_press:
						índ_nom = lista_nom.index(p)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = lst_colores[índ_color], relief = RAISED)
					if juego_num == 0 and contador_for == 1:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
					elif contador_for == 1 and otro_juego == True:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
			elif sel == 99:
				lista_nom = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
				lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
				for p in lista_nom:
					if str(f) == p and str(f) != but_press:
						índ_nom = lista_nom.index(p)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = lst_colores[índ_color], relief = RAISED)
					if juego_num == 0 and contador_for == 1:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
					elif contador_for == 1 and otro_juego == True:
						operaciones(str(f), lst_colores[índ_color], lst_operaciones[contador_lst_colores])
						contador_lst_colores += 1
						contador_for = 0
		índ_color += 1
	contador_lst_colores = 0
	juego_num += 1

def operaciones(casilla, color, operación):
	sel = nivel_selec.get()
	#operación = "1+"

	if sel == 33 or sel == 44 or sel == 55 or sel == 0 or sel == 77 or sel == 88 or sel == 99:
		if casilla == "23":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 286, y = 165)
		elif casilla == "24":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 346, y = 165)
		elif casilla == "25":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 406, y = 165)

		elif casilla == "33":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 286, y = 217)
		elif casilla == "34":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 346, y = 217)
		elif casilla == "35":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 406, y = 217)

		elif casilla == "43":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 286, y = 269)
		elif casilla == "44":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 346, y = 269)
		elif casilla == "45":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 406, y = 269)
	
	if sel == 44 or sel == 55 or sel == 0 or sel == 77 or sel == 88 or sel == 99:
		if casilla == "22":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 226, y = 165)
		elif casilla == "32":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 226, y = 217)
		elif casilla == "42":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 226, y = 269)
		elif casilla == "52":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 226, y = 321)
		elif casilla == "53":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 286, y = 321)
		elif casilla == "54":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 346, y = 321)
		elif casilla == "55":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 406, y = 321)
	
	if sel == 55 or sel == 0 or sel == 77 or sel == 88 or sel == 99:
		if casilla == "26":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 466, y = 165)
		elif casilla == "36":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 466, y = 217)
		elif casilla == "46":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 466, y = 269)
		elif casilla == "56":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 466, y = 321)
		elif casilla == "62":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 226, y = 373)
		elif casilla == "63":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 286, y = 373)
		elif casilla == "64":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 346, y = 373)
		elif casilla == "65":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 406, y = 373)
		elif casilla == "66":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 466, y = 373)

	if sel == 0 or sel == 77 or sel == 88 or sel == 99:
		if casilla == "11":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 166, y = 113)
		elif casilla == "12":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 226, y = 113)
		elif casilla == "13":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 286, y = 113)
		elif casilla == "14":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 346, y = 113)
		elif casilla == "15":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 406, y = 113)
		elif casilla == "16":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 466, y = 113)
		elif casilla == "21":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 166, y = 165)
		elif casilla == "31":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 166, y = 217)
		elif casilla == "41":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 166, y = 269)
		elif casilla == "51":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 166, y = 321)
		elif casilla == "61":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 166, y = 373)


	if sel == 77 or sel == 88 or sel == 99:
		if casilla == "17":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 526, y = 113)
		elif casilla == "27":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 526, y = 165)
		elif casilla == "37":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 526, y = 217)
		elif casilla == "47":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 526, y = 269)
		elif casilla == "57":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 526, y = 321)
		elif casilla == "67":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 526, y = 373)
		elif casilla == "71":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 166, y = 425)
		elif casilla == "72":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 226, y = 425)
		elif casilla == "73":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 286, y = 425)
		elif casilla == "74":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 346, y = 425)
		elif casilla == "75":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 406, y = 425)
		elif casilla == "76":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 466, y = 425)
		elif casilla == "77":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 526, y = 425)

	if sel == 88 or sel == 99:
		if casilla == "00":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 106, y = 61)
		elif casilla == "01":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 166, y = 61)
		elif casilla == "02":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 226, y = 61)
		elif casilla == "03":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 286, y = 61)
		elif casilla == "04":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 346, y = 61)
		elif casilla == "05":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 406, y = 61)
		elif casilla == "06":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 466, y = 61)
		elif casilla == "07":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 526, y = 61)
		elif casilla == "10":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 106, y = 113)
		elif casilla == "20":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 106, y = 165)
		elif casilla == "30":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 106, y = 217)
		elif casilla == "40":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 106, y = 269)
		elif casilla == "50":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 106, y = 321)
		elif casilla == "60":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 106, y = 373)
		elif casilla == "70":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 106, y = 425)

	if sel == 99:
		if casilla == "08":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 586, y = 61)
		elif casilla == "18":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 586, y = 113)
		elif casilla == "28":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 586, y = 165)
		elif casilla == "38":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 586, y = 217)
		elif casilla == "48":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 586, y = 269)
		elif casilla == "58":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 586, y = 321)
		elif casilla == "68":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 586, y = 373)
		elif casilla == "78":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 586, y = 425)
		elif casilla == "80":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 106, y = 477)
		elif casilla == "81":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 166, y = 477)
		elif casilla == "82":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 226, y = 477)
		elif casilla == "83":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 286, y = 477)
		elif casilla == "84":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 346, y = 477)
		elif casilla == "85":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 406, y = 477)
		elif casilla == "86":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 466, y = 477)
		elif casilla == "87":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 526, y = 477)
		elif casilla == "88":
			LBL_operación = Label(WIN_jugar, text = operación, font = ("Helvetica Neue", 8, "bold"), bg = color, fg = "White").place(x = 586, y = 477)

def validar (btn, num):
	global lst_validar
	lst_juego_validar
	índ_validar_lst_juego = 0
	
	if num != "*":
		for i in lst_juego_validar:
			
			for j in i:
				if str(j) == str(btn):
					x = lst_juego_validar[índ_validar_lst_juego].index(j)
					lst_temporal_validar = lst_validar[índ_validar_lst_juego]
					lst_temporal_validar.insert(x, int(num))
					lst_temporal_validar.pop(x + 1)
					return

			índ_validar_lst_juego += 1
	else:
		for i in lst_juego_validar:
			
			for j in i:
				if str(j) == str(btn):
					x = lst_juego_validar[índ_validar_lst_juego].index(j)
					lst_temporal_validar = lst_validar[índ_validar_lst_juego]
					lst_temporal_validar.pop(x)
					lst_temporal_validar.insert(x, "")
					return
			índ_validar_lst_juego += 1

def FN_validar ():
	global iniciado 
	global registrado
	global terminar

	if iniciado == False:
		messagebox.showerror("Error", "El juego no se ha iniciado.")
		return
	
	contador = 0
	índ_operación = 0
	lst_operación = []
	r = 0
	msg_error = False
	msg_terminar = True
	sel = nivel_selec.get()

	for i in lst_validar: #Inicia validación aritmética.
		contador = 0
		for j in i:
			if j == "":
				contador = 1
				lst_operación = []
				break
			lst_operación.append(j)

		if contador == 0 and lst_operación != []:
			índice_validar = lst_validar[índ_operación]

			if lst_operaciones[índ_operación][-1] == "+":
				r_correcto = lst_operaciones[índ_operación][:-1]
				for t in lst_operación:
					r += t
				lst_operación = []
				if int(r) != int(r_correcto):
					for j in lst_juego_validar[índ_operación]:
						if sel == 33:
							lista_nom = ["23","24","25","33","34","35","43","44","45"]
							lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 44:
							lista_nom = ["23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 55:
							lista_nom = ["26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 0:
							lista_nom = ["11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 77:
							lista_nom = ["17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 88:
							lista_nom = ["00","01","02","03","04","05","06","07","10","20","30","40","50","60","70","17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 99:
							lista_nom = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
							lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
				r = 0

			elif lst_operaciones[índ_operación][-1] == "-":
				r_correcto = lst_operaciones[índ_operación][:-1]
				r = lst_operación[0]
				for t in lst_operación[1:]:
					r -= t
				lst_operación = []
				if abs(r) != int(r_correcto):
					for j in lst_juego_validar[índ_operación]:
						if sel == 33:
							lista_nom = ["23","24","25","33","34","35","43","44","45"]
							lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 44:
							lista_nom = ["23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 55:
							lista_nom = ["26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 0:
							lista_nom = ["11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 77:
							lista_nom = ["17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 88:
							lista_nom = ["00","01","02","03","04","05","06","07","10","20","30","40","50","60","70","17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 99:
							lista_nom = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
							lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
				r = 0

			elif lst_operaciones[índ_operación][-1] == "/":
				r_correcto = lst_operaciones[índ_operación][:-1]
				if lst_operación[0] > lst_operación[1]:
					r = lst_operación[0] // lst_operación[1]
				else:
					r = lst_operación[1] // lst_operación[0]
				lst_operación = []
				if abs(r) != int(r_correcto):
					for j in lst_juego_validar[índ_operación]:
						if sel == 33:
							lista_nom = ["23","24","25","33","34","35","43","44","45"]
							lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 44:
							lista_nom = ["23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 55:
							lista_nom = ["26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 0:
							lista_nom = ["11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 77:
							lista_nom = ["17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 88:
							lista_nom = ["00","01","02","03","04","05","06","07","10","20","30","40","50","60","70","17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 99:
							lista_nom = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
							lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
				r = 0					
			
			elif lst_operaciones[índ_operación][-1] == "x":
				r = 1
				r_correcto = lst_operaciones[índ_operación][:-1]
				for t in lst_operación:
					r = r * t
				lst_operación = []
				if int(r) != int(r_correcto):
					for j in lst_juego_validar[índ_operación]:
						if sel == 33:
							lista_nom = ["23","24","25","33","34","35","43","44","45"]
							lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 44:
							lista_nom = ["23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 55:
							lista_nom = ["26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 0:
							lista_nom = ["11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 77:
							lista_nom = ["17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 88:
							lista_nom = ["00","01","02","03","04","05","06","07","10","20","30","40","50","60","70","17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
							lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
						elif sel == 99:
							lista_nom = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
							lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
							for p in lista_nom:
								if str(j) == p:
									índ_nom = lista_nom.index(p)
									elem_btn = lista_btn[índ_nom]
									elem_btn.config(bg = "Red")
									msg_error = True
				r = 0 
		else:
			lst_operación = []
		contador = 0
		índ_operación += 1
	
	contador_fila = 0
	lst_fila0 = ["00", "01", "02", "03", "04", "05", "06", "07", "08"]
	lst_fila0_validar = ["", "", "", "", "", "", "", "", ""]
	lst_fila1 = ["10", "11", "12", "13", "14", "15", "16", "17", "18"]
	lst_fila1_validar = ["", "", "", "", "", "", "", "", ""]
	lst_fila2 = ["20", "21", "22", "23", "24", "25", "26", "27", "28"]
	lst_fila2_validar = ["", "", "", "", "", "", "", "", ""]
	lst_fila3 = ["30", "31", "32", "33", "34", "35", "36", "37", "38"]
	lst_fila3_validar = ["", "", "", "", "", "", "", "", ""]
	lst_fila4 = ["40", "41", "42", "43", "44", "45", "46", "47", "48"]
	lst_fila4_validar = ["", "", "", "", "", "", "", "", ""]
	lst_fila5 = ["50", "51", "52", "53", "54", "55", "56", "57", "58"]
	lst_fila5_validar = ["", "", "", "", "", "", "", "", ""]
	lst_fila6 = ["60", "61", "62", "63", "64", "65", "66", "67", "68"]
	lst_fila6_validar = ["", "", "", "", "", "", "", "", ""]
	lst_fila7 = ["70", "71", "72", "73", "74", "75", "76", "77", "78"]
	lst_fila7_validar = ["", "", "", "", "", "", "", "", ""]
	lst_fila8 = ["80", "81", "82", "83", "84", "85", "86", "87", "88"]
	lst_fila8_validar = ["", "", "", "", "", "", "", "", ""]

	lst_columna0 = ["00", "10", "20", "30", "40", "50", "60", "70", "80"]
	lst_columna0_validar = ["", "", "", "", "", "", "", "", ""]
	lst_columna1 = ["01", "11", "21", "31", "41", "51", "61", "71", "81"]
	lst_columna1_validar = ["", "", "", "", "", "", "", "", ""]
	lst_columna2 = ["02", "12", "22", "32", "42", "52", "62", "72", "82"]
	lst_columna2_validar = ["", "", "", "", "", "", "", "", ""]
	lst_columna3 = ["03", "13", "23", "33", "43", "53", "63", "73", "83"]
	lst_columna3_validar = ["", "", "", "", "", "", "", "", ""]
	lst_columna4 = ["04", "14", "24", "34", "44", "54", "64", "74", "84"]
	lst_columna4_validar = ["", "", "", "", "", "", "", "", ""]
	lst_columna5 = ["05", "15", "25", "35", "45", "55", "65", "75", "85"]
	lst_columna5_validar = ["", "", "", "", "", "", "", "", ""]
	lst_columna6 = ["06", "16", "26", "36", "46", "56", "66", "76", "86"]
	lst_columna6_validar = ["", "", "", "", "", "", "", "", ""]
	lst_columna7 = ["07", "17", "27", "37", "47", "57", "67", "77", "87"]
	lst_columna7_validar = ["", "", "", "", "", "", "", "", ""]
	lst_columna8 = ["08", "18", "28", "38", "48", "58", "68", "78", "88"]
	lst_columna8_validar = ["", "", "", "", "", "", "", "", ""]

	for b in lst_juego_validar:
		for s in b:
			if sel == 33:
				if str(s) in lst_fila2:
					índ_nom = lst_fila2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila2_validar.insert(índ_nom, int(elemento))
						lst_fila2_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila3:
					índ_nom = lst_fila3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila3_validar.insert(índ_nom, int(elemento))
						lst_fila3_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila4:
					índ_nom = lst_fila4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila4_validar.insert(índ_nom, int(elemento))
						lst_fila4_validar.pop(índ_nom + 1)

				#A continuación se agregan los valores necesarios para la validación de columnas en 3 x 3.
				if str(s) in lst_columna3:
					índ_nom = lst_columna3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna3_validar.insert(índ_nom, int(elemento))
						lst_columna3_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna4:
					índ_nom = lst_columna4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna4_validar.insert(índ_nom, int(elemento))
						lst_columna4_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna5:
					índ_nom = lst_columna5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna5_validar.insert(índ_nom, int(elemento))
						lst_columna5_validar.pop(índ_nom + 1)

			elif sel == 44:
				if str(s) in lst_fila2:
					índ_nom = lst_fila2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila2_validar.insert(índ_nom, int(elemento))
						lst_fila2_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila3:
					índ_nom = lst_fila3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila3_validar.insert(índ_nom, int(elemento))
						lst_fila3_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila4:
					índ_nom = lst_fila4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila4_validar.insert(índ_nom, int(elemento))
						lst_fila4_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila5:
					índ_nom = lst_fila5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila5_validar.insert(índ_nom, int(elemento))
						lst_fila5_validar.pop(índ_nom + 1)

				#A continuación se agregan los valores necesarios para la validación de columnas en 4 x 4.
				if str(s) in lst_columna2:
					índ_nom = lst_columna2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna2_validar.insert(índ_nom, int(elemento))
						lst_columna2_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna3:
					índ_nom = lst_columna3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna3_validar.insert(índ_nom, int(elemento))
						lst_columna3_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna4:
					índ_nom = lst_columna4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna4_validar.insert(índ_nom, int(elemento))
						lst_columna4_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna5:
					índ_nom = lst_columna5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna5_validar.insert(índ_nom, int(elemento))
						lst_columna5_validar.pop(índ_nom + 1)
		
			elif sel == 55:
				if str(s) in lst_fila2:
					índ_nom = lst_fila2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila2_validar.insert(índ_nom, int(elemento))
						lst_fila2_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila3:
					índ_nom = lst_fila3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila3_validar.insert(índ_nom, int(elemento))
						lst_fila3_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila4:
					índ_nom = lst_fila4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila4_validar.insert(índ_nom, int(elemento))
						lst_fila4_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila5:
					índ_nom = lst_fila5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila5_validar.insert(índ_nom, int(elemento))
						lst_fila5_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila6:
					índ_nom = lst_fila6.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila6_validar.insert(índ_nom, int(elemento))
						lst_fila6_validar.pop(índ_nom + 1)

				#A continuación se agregan los valores necesarios para la validación de columnas en 5 x 5.
				if str(s) in lst_columna2:
					índ_nom = lst_columna2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna2_validar.insert(índ_nom, int(elemento))
						lst_columna2_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna3:
					índ_nom = lst_columna3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna3_validar.insert(índ_nom, int(elemento))
						lst_columna3_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna4:
					índ_nom = lst_columna4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna4_validar.insert(índ_nom, int(elemento))
						lst_columna4_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna5:
					índ_nom = lst_columna5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna5_validar.insert(índ_nom, int(elemento))
						lst_columna5_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna6:
					índ_nom = lst_columna6.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna6_validar.insert(índ_nom, int(elemento))
						lst_columna6_validar.pop(índ_nom + 1)
		
			elif sel == 0:
				if str(s) in lst_fila1:
					índ_nom = lst_fila1.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila1_validar.insert(índ_nom, int(elemento))
						lst_fila1_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila2:
					índ_nom = lst_fila2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila2_validar.insert(índ_nom, int(elemento))
						lst_fila2_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila3:
					índ_nom = lst_fila3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila3_validar.insert(índ_nom, int(elemento))
						lst_fila3_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila4:
					índ_nom = lst_fila4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila4_validar.insert(índ_nom, int(elemento))
						lst_fila4_validar.pop(índ_nom + 1)

				elif str(s) in lst_fila5:
					índ_nom = lst_fila5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila5_validar.insert(índ_nom, int(elemento))
						lst_fila5_validar.pop(índ_nom + 1)
				
				elif str(s) in lst_fila6:
					índ_nom = lst_fila6.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila6_validar.insert(índ_nom, int(elemento))
						lst_fila6_validar.pop(índ_nom + 1)

				#A continuación se agregan los valores necesarios para la validación de columnas en 6 x 6.
				if str(s) in lst_columna1:
					índ_nom = lst_columna1.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna1_validar.insert(índ_nom, int(elemento))
						lst_columna1_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna2:
					índ_nom = lst_columna2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna2_validar.insert(índ_nom, int(elemento))
						lst_columna2_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna3:
					índ_nom = lst_columna3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna3_validar.insert(índ_nom, int(elemento))
						lst_columna3_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna4:
					índ_nom = lst_columna4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna4_validar.insert(índ_nom, int(elemento))
						lst_columna4_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna5:
					índ_nom = lst_columna5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna5_validar.insert(índ_nom, int(elemento))
						lst_columna5_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna6:
					índ_nom = lst_columna6.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna6_validar.insert(índ_nom, int(elemento))
						lst_columna6_validar.pop(índ_nom + 1)

			elif sel == 77:
				if str(s) in lst_fila1:
					índ_nom = lst_fila1.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila1_validar.insert(índ_nom, int(elemento))
						lst_fila1_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila2:
					índ_nom = lst_fila2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila2_validar.insert(índ_nom, int(elemento))
						lst_fila2_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila3:
					índ_nom = lst_fila3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila3_validar.insert(índ_nom, int(elemento))
						lst_fila3_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila4:
					índ_nom = lst_fila4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila4_validar.insert(índ_nom, int(elemento))
						lst_fila4_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila5:
					índ_nom = lst_fila5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila5_validar.insert(índ_nom, int(elemento))
						lst_fila5_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila6:
					índ_nom = lst_fila6.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila6_validar.insert(índ_nom, int(elemento))
						lst_fila6_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila7:
					índ_nom = lst_fila7.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila7_validar.insert(índ_nom, int(elemento))
						lst_fila7_validar.pop(índ_nom + 1)

				#A continuación se agregan los valores necesarios para la validación de columnas en 7 x 7.
				if str(s) in lst_columna1:
					índ_nom = lst_columna1.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna1_validar.insert(índ_nom, int(elemento))
						lst_columna1_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna2:
					índ_nom = lst_columna2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna2_validar.insert(índ_nom, int(elemento))
						lst_columna2_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna3:
					índ_nom = lst_columna3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna3_validar.insert(índ_nom, int(elemento))
						lst_columna3_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna4:
					índ_nom = lst_columna4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna4_validar.insert(índ_nom, int(elemento))
						lst_columna4_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna5:
					índ_nom = lst_columna5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna5_validar.insert(índ_nom, int(elemento))
						lst_columna5_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna6:
					índ_nom = lst_columna6.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna6_validar.insert(índ_nom, int(elemento))
						lst_columna6_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna7:
					índ_nom = lst_columna7.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_columna7_validar.insert(índ_nom, int(elemento))
						lst_columna7_validar.pop(índ_nom + 1)
		
			elif sel == 88:
				if str(s) in lst_fila0:
					índ_nom = lst_fila0.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(str(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila0_validar.insert(índ_nom, int(elemento))
						lst_fila0_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila1:
					índ_nom = lst_fila1.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila1_validar.insert(índ_nom, int(elemento))
						lst_fila1_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila2:
					índ_nom = lst_fila2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila2_validar.insert(índ_nom, int(elemento))
						lst_fila2_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila3:
					índ_nom = lst_fila3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila3_validar.insert(índ_nom, int(elemento))
						lst_fila3_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila4:
					índ_nom = lst_fila4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila4_validar.insert(índ_nom, int(elemento))
						lst_fila4_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila5:
					índ_nom = lst_fila5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila5_validar.insert(índ_nom, int(elemento))
						lst_fila5_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila6:
					índ_nom = lst_fila6.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila6_validar.insert(índ_nom, int(elemento))
						lst_fila6_validar.pop(índ_nom + 1)
				
				elif str(s) in lst_fila7:
					índ_nom = lst_fila7.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila7_validar.insert(índ_nom, int(elemento))
						lst_fila7_validar.pop(índ_nom + 1)

				#A continuación se agregan los valores necesarios para la validación de columnas en 8 x 8.
				if str(s) in lst_columna0:
					if str(s) == "00":
						índ_nom = lst_columna0.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna0_validar.insert(índ_nom, int(elemento))
							lst_columna0_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna0.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna0_validar.insert(índ_nom, int(elemento))
							lst_columna0_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna1:
					if str(s) == "01":
						índ_nom = lst_columna1.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna1_validar.insert(índ_nom, int(elemento))
							lst_columna1_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna1.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna1_validar.insert(índ_nom, int(elemento))
							lst_columna1_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna2:
					if str(s) == "02":
						índ_nom = lst_columna2.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna2_validar.insert(índ_nom, int(elemento))
							lst_columna2_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna2.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna2_validar.insert(índ_nom, int(elemento))
							lst_columna2_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna3:
					if str(s) == "03":
						índ_nom = lst_columna3.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna3_validar.insert(índ_nom, int(elemento))
							lst_columna3_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna3.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna3_validar.insert(índ_nom, int(elemento))
							lst_columna3_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna4:
					if str(s) == "04":
						índ_nom = lst_columna4.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna4_validar.insert(índ_nom, int(elemento))
							lst_columna4_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna4.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna4_validar.insert(índ_nom, int(elemento))
							lst_columna4_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna5:
					if str(s) == "05":
						índ_nom = lst_columna5.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna5_validar.insert(índ_nom, int(elemento))
							lst_columna5_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna5.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna5_validar.insert(índ_nom, int(elemento))
							lst_columna5_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna6:
					if str(s) == "06":
						índ_nom = lst_columna6.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna6_validar.insert(índ_nom, int(elemento))
							lst_columna6_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna6.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna6_validar.insert(índ_nom, int(elemento))
							lst_columna6_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna7:
					if str(s) == "07":
						índ_nom = lst_columna7.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna7_validar.insert(índ_nom, int(elemento))
							lst_columna7_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna7.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna7_validar.insert(índ_nom, int(elemento))
							lst_columna7_validar.pop(índ_nom + 1)
			
			elif sel == 99:
				if str(s) in lst_fila0:
					índ_nom = lst_fila0.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(str(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila0_validar.insert(índ_nom, int(elemento))
						lst_fila0_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila1:
					índ_nom = lst_fila1.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila1_validar.insert(índ_nom, int(elemento))
						lst_fila1_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila2:
					índ_nom = lst_fila2.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila2_validar.insert(índ_nom, int(elemento))
						lst_fila2_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila3:
					índ_nom = lst_fila3.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila3_validar.insert(índ_nom, int(elemento))
						lst_fila3_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila4:
					índ_nom = lst_fila4.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila4_validar.insert(índ_nom, int(elemento))
						lst_fila4_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila5:
					índ_nom = lst_fila5.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila5_validar.insert(índ_nom, int(elemento))
						lst_fila5_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila6:
					índ_nom = lst_fila6.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila6_validar.insert(índ_nom, int(elemento))
						lst_fila6_validar.pop(índ_nom + 1)				
				elif str(s) in lst_fila7:
					índ_nom = lst_fila7.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila7_validar.insert(índ_nom, int(elemento))
						lst_fila7_validar.pop(índ_nom + 1)
				elif str(s) in lst_fila8:
					índ_nom = lst_fila8.index(str(s))
					índ_elemento = lst_juego_validar[contador_fila].index(int(s))
					elemento = lst_validar[contador_fila][índ_elemento]
					if elemento != "":
						lst_fila8_validar.insert(índ_nom, int(elemento))
						lst_fila8_validar.pop(índ_nom + 1)

				#A continuación se agregan los valores necesarios para la validación de columnas en 8 x 8.
				if str(s) in lst_columna0:
					if str(s) == "00":
						índ_nom = lst_columna0.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna0_validar.insert(índ_nom, int(elemento))
							lst_columna0_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna0.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna0_validar.insert(índ_nom, int(elemento))
							lst_columna0_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna1:
					if str(s) == "01":
						índ_nom = lst_columna1.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna1_validar.insert(índ_nom, int(elemento))
							lst_columna1_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna1.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna1_validar.insert(índ_nom, int(elemento))
							lst_columna1_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna2:
					if str(s) == "02":
						índ_nom = lst_columna2.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna2_validar.insert(índ_nom, int(elemento))
							lst_columna2_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna2.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna2_validar.insert(índ_nom, int(elemento))
							lst_columna2_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna3:
					if str(s) == "03":
						índ_nom = lst_columna3.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna3_validar.insert(índ_nom, int(elemento))
							lst_columna3_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna3.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna3_validar.insert(índ_nom, int(elemento))
							lst_columna3_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna4:
					if str(s) == "04":
						índ_nom = lst_columna4.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna4_validar.insert(índ_nom, int(elemento))
							lst_columna4_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna4.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna4_validar.insert(índ_nom, int(elemento))
							lst_columna4_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna5:
					if str(s) == "05":
						índ_nom = lst_columna5.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna5_validar.insert(índ_nom, int(elemento))
							lst_columna5_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna5.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna5_validar.insert(índ_nom, int(elemento))
							lst_columna5_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna6:
					if str(s) == "06":
						índ_nom = lst_columna6.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna6_validar.insert(índ_nom, int(elemento))
							lst_columna6_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna6.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna6_validar.insert(índ_nom, int(elemento))
							lst_columna6_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna7:
					if str(s) == "07":
						índ_nom = lst_columna7.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna7_validar.insert(índ_nom, int(elemento))
							lst_columna7_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna7.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna7_validar.insert(índ_nom, int(elemento))
							lst_columna7_validar.pop(índ_nom + 1)

				elif str(s) in lst_columna8:
					if str(s) == "08":
						índ_nom = lst_columna8.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(str(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna8_validar.insert(índ_nom, int(elemento))
							lst_columna8_validar.pop(índ_nom + 1)
					else:
						índ_nom = lst_columna8.index(str(s))
						índ_elemento = lst_juego_validar[contador_fila].index(int(s))
						elemento = lst_validar[contador_fila][índ_elemento]
						if elemento != "":
							lst_columna8_validar.insert(índ_nom, int(elemento))
							lst_columna8_validar.pop(índ_nom + 1)

		contador_fila += 1

	contador_fila = 1
	contador_columna = 1
	if sel == 33:
		for q in lst_fila2_validar:
			if q in lst_fila2_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila2_validar.index(q)
				botón = lst_fila2[índ_elemento]
				lista_nom = ["23","24","25"]
				lista_btn = [BTN_23,BTN_24,BTN_25]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila3_validar:
			if q in lst_fila3_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila3_validar.index(q)
				botón = lst_fila3[índ_elemento]
				lista_nom = ["33", "34", "35"]
				lista_btn = [BTN_33,BTN_34,BTN_35]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila4_validar:
			if q in lst_fila4_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila4_validar.index(q)
				botón = lst_fila4[índ_elemento]
				lista_nom = ["43", "44", "45"]
				lista_btn = [BTN_43,BTN_44,BTN_45]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		#A continuación inicia validación de columnas en 3 x 3.
		contador_columna = 1
		for q in lst_columna3_validar:
			if q in lst_columna3_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna3_validar.index(q)
				botón = lst_columna3[índ_elemento]
				lista_nom = ["23","33","43"]
				lista_btn = [BTN_23,BTN_33,BTN_43]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna4_validar:
			if q in lst_columna4_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna4_validar.index(q)
				botón = lst_columna4[índ_elemento]
				lista_nom = ["24","34","44"]
				lista_btn = [BTN_24,BTN_34,BTN_44]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna5_validar:
			if q in lst_columna5_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna5_validar.index(q)
				botón = lst_columna5[índ_elemento]
				lista_nom = ["25","35","45"]
				lista_btn = [BTN_25,BTN_35,BTN_45]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1
	
	elif sel == 44:
		for q in lst_fila2_validar:
			if q in lst_fila2_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila2_validar.index(q)
				botón = lst_fila2[índ_elemento]
				lista_nom = ["22","23","24","25"]
				lista_btn = [BTN_22,BTN_23,BTN_24,BTN_25]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila3_validar:
			if q in lst_fila3_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila3_validar.index(q)
				botón = lst_fila3[índ_elemento]
				lista_nom = ["32","33", "34", "35"]
				lista_btn = [BTN_32,BTN_33,BTN_34,BTN_35]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila4_validar:
			if q in lst_fila4_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila4_validar.index(q)
				botón = lst_fila4[índ_elemento]
				lista_nom = ["42","43", "44", "45"]
				lista_btn = [BTN_42,BTN_43,BTN_44,BTN_45]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1
		
		contador_fila = 1
		for q in lst_fila5_validar:
			if q in lst_fila5_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila5_validar.index(q)
				botón = lst_fila5[índ_elemento]
				lista_nom = ["52","53", "54", "55"]
				lista_btn = [BTN_52,BTN_53,BTN_54,BTN_55]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		#A continuación inicia validación de columnas en 4 x 4.
		contador_columna = 1
		for q in lst_columna2_validar:
			if q in lst_columna2_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna2_validar.index(q)
				botón = lst_columna2[índ_elemento]
				lista_nom = ["22", "32", "42", "52"]
				lista_btn = [BTN_22,BTN_32,BTN_42, BTN_52]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna3_validar:
			if q in lst_columna3_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna3_validar.index(q)
				botón = lst_columna3[índ_elemento]
				lista_nom = ["23","33","43","53"]
				lista_btn = [BTN_23,BTN_33,BTN_43, BTN_53]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna4_validar:
			if q in lst_columna4_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna4_validar.index(q)
				botón = lst_columna4[índ_elemento]
				lista_nom = ["24","34","44","54"]
				lista_btn = [BTN_24,BTN_34,BTN_44, BTN_54]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna5_validar:
			if q in lst_columna5_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna5_validar.index(q)
				botón = lst_columna5[índ_elemento]
				lista_nom = ["25","35","45","55"]
				lista_btn = [BTN_25,BTN_35,BTN_45, BTN_55]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1
	
	elif sel == 55:
		for q in lst_fila2_validar:
			if q in lst_fila2_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila2_validar.index(q)
				botón = lst_fila2[índ_elemento]
				lista_nom = ["22","23","24","25", "26"]
				lista_btn = [BTN_22,BTN_23,BTN_24,BTN_25,BTN_26]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila3_validar:
			if q in lst_fila3_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila3_validar.index(q)
				botón = lst_fila3[índ_elemento]
				lista_nom = ["32","33", "34", "35", "36"]
				lista_btn = [BTN_32,BTN_33,BTN_34,BTN_35,BTN_36]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila4_validar:
			if q in lst_fila4_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila4_validar.index(q)
				botón = lst_fila4[índ_elemento]
				lista_nom = ["42","43", "44", "45", "46"]
				lista_btn = [BTN_42,BTN_43,BTN_44,BTN_45,BTN_46]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila5_validar:
			if q in lst_fila5_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila5_validar.index(q)
				botón = lst_fila5[índ_elemento]
				lista_nom = ["52","53", "54", "55", "56"]
				lista_btn = [BTN_52,BTN_53,BTN_54,BTN_55, BTN_56]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1
		
		contador_fila = 1
		for q in lst_fila6_validar:
			if q in lst_fila6_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila6_validar.index(q)
				botón = lst_fila6[índ_elemento]
				lista_nom = ["62","63", "64", "65", "66"]
				lista_btn = [BTN_62,BTN_63,BTN_64,BTN_65, BTN_66]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		#A continuación inicia validación de columnas en 5 x 5.
		contador_columna = 1
		for q in lst_columna2_validar:
			if q in lst_columna2_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna2_validar.index(q)
				botón = lst_columna2[índ_elemento]
				lista_nom = ["22", "32", "42", "52","62"]
				lista_btn = [BTN_22,BTN_32,BTN_42, BTN_52, BTN_62]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna3_validar:
			if q in lst_columna3_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna3_validar.index(q)
				botón = lst_columna3[índ_elemento]
				lista_nom = ["23","33","43","53", "63"]
				lista_btn = [BTN_23,BTN_33,BTN_43, BTN_53, BTN_63]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna4_validar:
			if q in lst_columna4_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna4_validar.index(q)
				botón = lst_columna4[índ_elemento]
				lista_nom = ["24","34","44","54", "64"]
				lista_btn = [BTN_24,BTN_34,BTN_44, BTN_54, BTN_64]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna5_validar:
			if q in lst_columna5_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna5_validar.index(q)
				botón = lst_columna5[índ_elemento]
				lista_nom = ["25","35","45","55", "65"]
				lista_btn = [BTN_25,BTN_35,BTN_45, BTN_55, BTN_65]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna6_validar:
			if q in lst_columna6_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna6_validar.index(q)
				botón = lst_columna6[índ_elemento]
				lista_nom = ["26","36","46","56", "66"]
				lista_btn = [BTN_26,BTN_36,BTN_46, BTN_56, BTN_66]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

	elif sel == 0:
		for q in lst_fila1_validar:
			if q in lst_fila1_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila1_validar.index(q)
				botón = lst_fila1[índ_elemento]
				lista_nom = ["11","12","13","14","15", "16"]
				lista_btn = [BTN_22,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila2_validar:
			if q in lst_fila2_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila2_validar.index(q)
				botón = lst_fila2[índ_elemento]
				lista_nom = ["21","22","23","24","25", "26"]
				lista_btn = [BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila3_validar:
			if q in lst_fila3_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila3_validar.index(q)
				botón = lst_fila3[índ_elemento]
				lista_nom = ["31","32","33", "34", "35", "36"]
				lista_btn = [BTN_21,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila4_validar:
			if q in lst_fila4_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila4_validar.index(q)
				botón = lst_fila4[índ_elemento]
				lista_nom = ["41","42","43", "44", "45", "46"]
				lista_btn = [BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila5_validar:
			if q in lst_fila5_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila5_validar.index(q)
				botón = lst_fila5[índ_elemento]
				lista_nom = ["51","52","53", "54", "55", "56"]
				lista_btn = [BTN_51,BTN_52,BTN_53,BTN_54,BTN_55, BTN_56]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1
		
		contador_fila = 1
		for q in lst_fila6_validar:
			if q in lst_fila6_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila6_validar.index(q)
				botón = lst_fila6[índ_elemento]
				lista_nom = ["61","62","63", "64", "65", "66"]
				lista_btn = [BTN_61,BTN_62,BTN_63,BTN_64,BTN_65, BTN_66]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		#A continuación inicia validación de columnas en 6 x 6.
		contador_columna = 1
		for q in lst_columna1_validar:
			if q in lst_columna1_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna1_validar.index(q)
				botón = lst_columna1[índ_elemento]
				lista_nom = ["11","21", "31", "41", "51","61"]
				lista_btn = [BTN_11,BTN_21,BTN_31,BTN_41, BTN_51, BTN_61]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna2_validar:
			if q in lst_columna2_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna2_validar.index(q)
				botón = lst_columna2[índ_elemento]
				lista_nom = ["12","22", "32", "42", "52","62"]
				lista_btn = [BTN_12,BTN_22,BTN_32,BTN_42, BTN_52, BTN_62]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna3_validar:
			if q in lst_columna3_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna3_validar.index(q)
				botón = lst_columna3[índ_elemento]
				lista_nom = ["13","23","33","43","53", "63"]
				lista_btn = [BTN_13,BTN_23,BTN_33,BTN_43, BTN_53, BTN_63]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna4_validar:
			if q in lst_columna4_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna4_validar.index(q)
				botón = lst_columna4[índ_elemento]
				lista_nom = ["14","24","34","44","54", "64"]
				lista_btn = [BTN_14,BTN_24,BTN_34,BTN_44, BTN_54, BTN_64]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna5_validar:
			if q in lst_columna5_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna5_validar.index(q)
				botón = lst_columna5[índ_elemento]
				lista_nom = ["15","25","35","45","55", "65"]
				lista_btn = [BTN_15,BTN_25,BTN_35,BTN_45, BTN_55, BTN_65]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna6_validar:
			if q in lst_columna6_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna6_validar.index(q)
				botón = lst_columna6[índ_elemento]
				lista_nom = ["16","26","36","46","56", "66"]
				lista_btn = [BTN_16,BTN_26,BTN_36,BTN_46, BTN_56, BTN_66]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

	elif sel == 77:
		for q in lst_fila1_validar:
			if q in lst_fila1_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila1_validar.index(q)
				botón = lst_fila1[índ_elemento]
				lista_nom = ["11","12","13","14","15", "16", "17"]
				lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila2_validar:
			if q in lst_fila2_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila2_validar.index(q)
				botón = lst_fila2[índ_elemento]
				lista_nom = ["21","22","23","24","25", "26","27"]
				lista_btn = [BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila3_validar:
			if q in lst_fila3_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila3_validar.index(q)
				botón = lst_fila3[índ_elemento]
				lista_nom = ["31","32","33", "34", "35", "36", "37"]
				lista_btn = [BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila4_validar:
			if q in lst_fila4_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila4_validar.index(q)
				botón = lst_fila4[índ_elemento]
				lista_nom = ["41","42","43", "44", "45", "46","47"]
				lista_btn = [BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila5_validar:
			if q in lst_fila5_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila5_validar.index(q)
				botón = lst_fila5[índ_elemento]
				lista_nom = ["51","52","53", "54", "55", "56","57"]
				lista_btn = [BTN_51,BTN_52,BTN_53,BTN_54,BTN_55, BTN_56,BTN_57]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1
		
		contador_fila = 1
		for q in lst_fila6_validar:
			if q in lst_fila6_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila6_validar.index(q)
				botón = lst_fila6[índ_elemento]
				lista_nom = ["61","62","63", "64", "65", "66","67"]
				lista_btn = [BTN_61,BTN_62,BTN_63,BTN_64,BTN_65, BTN_66,BTN_67]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila7_validar:
			if q in lst_fila7_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila7_validar.index(q)
				botón = lst_fila7[índ_elemento]
				lista_nom = ["71","72","73", "74", "75", "76","77"]
				lista_btn = [BTN_71,BTN_72,BTN_73,BTN_74,BTN_75, BTN_76,BTN_77]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1


		#A continuación inicia validación de columnas en 7 x 7.
		contador_columna = 1
		for q in lst_columna1_validar:
			if q in lst_columna1_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna1_validar.index(q)
				botón = lst_columna1[índ_elemento]
				lista_nom = ["11","21", "31", "41","51","61","71"]
				lista_btn = [BTN_11,BTN_21,BTN_31,BTN_41, BTN_51, BTN_61,BTN_71]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna2_validar:
			if q in lst_columna2_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna2_validar.index(q)
				botón = lst_columna2[índ_elemento]
				lista_nom = ["12","22", "32","42","52","62","72"]
				lista_btn = [BTN_12,BTN_22,BTN_32,BTN_42, BTN_52, BTN_62,BTN_72]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna3_validar:
			if q in lst_columna3_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna3_validar.index(q)
				botón = lst_columna3[índ_elemento]
				lista_nom = ["13","23","33","43","53","63","73"]
				lista_btn = [BTN_13,BTN_23,BTN_33,BTN_43, BTN_53, BTN_63,BTN_73]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna4_validar:
			if q in lst_columna4_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna4_validar.index(q)
				botón = lst_columna4[índ_elemento]
				lista_nom = ["14","24","34","44","54","64","74"]
				lista_btn = [BTN_14,BTN_24,BTN_34,BTN_44, BTN_54, BTN_64,BTN_74]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna5_validar:
			if q in lst_columna5_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna5_validar.index(q)
				botón = lst_columna5[índ_elemento]
				lista_nom = ["15","25","35","45","55","65","75"]
				lista_btn = [BTN_15,BTN_25,BTN_35,BTN_45, BTN_55, BTN_65,BTN_75]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna6_validar:
			if q in lst_columna6_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna6_validar.index(q)
				botón = lst_columna6[índ_elemento]
				lista_nom = ["16","26","36","46","56","66","67"]
				lista_btn = [BTN_16,BTN_26,BTN_36,BTN_46, BTN_56, BTN_66,BTN_76]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna7_validar:
			if q in lst_columna7_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna7_validar.index(q)
				botón = lst_columna7[índ_elemento]
				lista_nom = ["17","27","37","47","57","67","77"]
				lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47, BTN_57, BTN_67,BTN_77]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1
	
	elif sel == 88:
		for q in lst_fila0_validar:
			if q in lst_fila0_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila0_validar.index(q)
				botón = lst_fila0[índ_elemento]
				lista_nom = ["00","01","02","03","04","05", "06", "07"]
				lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07]
				for z in lista_nom:
					if str(botón) == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila1_validar:
			if q in lst_fila1_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila1_validar.index(q)
				botón = lst_fila1[índ_elemento]
				lista_nom = ["10","11","12","13","14","15", "16", "17"]
				lista_btn = [BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17]
				for z in lista_nom:
					if str(botón) == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila2_validar:
			if q in lst_fila2_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila2_validar.index(q)
				botón = lst_fila2[índ_elemento]
				lista_nom = ["20","21","22","23","24","25", "26","27"]
				lista_btn = [BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila3_validar:
			if q in lst_fila3_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila3_validar.index(q)
				botón = lst_fila3[índ_elemento]
				lista_nom = ["30","31","32","33", "34", "35", "36", "37"]
				lista_btn = [BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila4_validar:
			if q in lst_fila4_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila4_validar.index(q)
				botón = lst_fila4[índ_elemento]
				lista_nom = ["40","41","42","43", "44", "45", "46","47"]
				lista_btn = [BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila5_validar:
			if q in lst_fila5_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila5_validar.index(q)
				botón = lst_fila5[índ_elemento]
				lista_nom = ["50","51","52","53", "54", "55", "56","57"]
				lista_btn = [BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55, BTN_56,BTN_57]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1
		
		contador_fila = 1
		for q in lst_fila6_validar:
			if q in lst_fila6_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila6_validar.index(q)
				botón = lst_fila6[índ_elemento]
				lista_nom = ["60","61","62","63", "64", "65", "66","67"]
				lista_btn = [BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65, BTN_66,BTN_67]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila7_validar:
			if q in lst_fila7_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila7_validar.index(q)
				botón = lst_fila7[índ_elemento]
				lista_nom = ["70","71","72","73", "74", "75", "76","77"]
				lista_btn = [BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75, BTN_76,BTN_77]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		#A continuación inicia validación de columnas en 8 x 8.
		contador_columna = 1
		for q in lst_columna0_validar:
			if q in lst_columna0_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna0_validar.index(q)
				botón = lst_columna0[índ_elemento]
				lista_nom = ["00","10","20", "30", "40","50","60","70"]
				lista_btn = [BTN_00,BTN_10,BTN_20,BTN_30,BTN_40, BTN_50, BTN_60,BTN_70]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna1_validar:
			if q in lst_columna1_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna1_validar.index(q)
				botón = lst_columna1[índ_elemento]
				lista_nom = ["01","11","21","31", "41","51","61","71"]
				lista_btn = [BTN_01,BTN_11,BTN_21,BTN_31,BTN_41, BTN_51, BTN_61,BTN_71]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna2_validar:
			if q in lst_columna2_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna2_validar.index(q)
				botón = lst_columna2[índ_elemento]
				lista_nom = ["02","12","22", "32","42","52","62","72"]
				lista_btn = [BTN_02,BTN_12,BTN_22,BTN_32,BTN_42, BTN_52, BTN_62,BTN_72]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna3_validar:
			if q in lst_columna3_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna3_validar.index(q)
				botón = lst_columna3[índ_elemento]
				lista_nom = ["03","13","23","33","43","53","63","73"]
				lista_btn = [BTN_03,BTN_13,BTN_23,BTN_33,BTN_43, BTN_53, BTN_63,BTN_73]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna4_validar:
			if q in lst_columna4_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna4_validar.index(q)
				botón = lst_columna4[índ_elemento]
				lista_nom = ["04","14","24","34","44","54","64","74"]
				lista_btn = [BTN_04,BTN_14,BTN_24,BTN_34,BTN_44, BTN_54, BTN_64,BTN_74]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna5_validar:
			if q in lst_columna5_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna5_validar.index(q)
				botón = lst_columna5[índ_elemento]
				lista_nom = ["05","15","25","35","45","55","65","75"]
				lista_btn = [BTN_05,BTN_15,BTN_25,BTN_35,BTN_45, BTN_55, BTN_65,BTN_75]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna6_validar:
			if q in lst_columna6_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna6_validar.index(q)
				botón = lst_columna6[índ_elemento]
				lista_nom = ["06","16","26","36","46","56","66","67"]
				lista_btn = [BTN_06,BTN_16,BTN_26,BTN_36,BTN_46, BTN_56, BTN_66,BTN_76]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna7_validar:
			if q in lst_columna7_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna7_validar.index(q)
				botón = lst_columna7[índ_elemento]
				lista_nom = ["07","17","27","37","47","57","67","77"]
				lista_btn = [BTN_07,BTN_17,BTN_27,BTN_37,BTN_47, BTN_57, BTN_67,BTN_77]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

	elif sel == 99:
		for q in lst_fila0_validar:
			if q in lst_fila0_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila0_validar.index(q)
				botón = lst_fila0[índ_elemento]
				lista_nom = ["00","01","02","03","04","05", "06", "07", "08"]
				lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08]
				for z in lista_nom:
					if str(botón) == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila1_validar:
			if q in lst_fila1_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila1_validar.index(q)
				botón = lst_fila1[índ_elemento]
				lista_nom = ["10","11","12","13","14","15", "16", "17", "18"]
				lista_btn = [BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18]
				for z in lista_nom:
					if str(botón) == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila2_validar:
			if q in lst_fila2_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila2_validar.index(q)
				botón = lst_fila2[índ_elemento]
				lista_nom = ["20","21","22","23","24","25", "26","27", "28"]
				lista_btn = [BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila3_validar:
			if q in lst_fila3_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila3_validar.index(q)
				botón = lst_fila3[índ_elemento]
				lista_nom = ["30","31","32","33", "34", "35", "36", "37", "38"]
				lista_btn = [BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila4_validar:
			if q in lst_fila4_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila4_validar.index(q)
				botón = lst_fila4[índ_elemento]
				lista_nom = ["40","41","42","43", "44", "45", "46","47", "48"]
				lista_btn = [BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila5_validar:
			if q in lst_fila5_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila5_validar.index(q)
				botón = lst_fila5[índ_elemento]
				lista_nom = ["50","51","52","53", "54", "55", "56","57", "58"]
				lista_btn = [BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55, BTN_56,BTN_57,BTN_58]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1
		
		contador_fila = 1
		for q in lst_fila6_validar:
			if q in lst_fila6_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila6_validar.index(q)
				botón = lst_fila6[índ_elemento]
				lista_nom = ["60","61","62","63", "64", "65", "66","67", "68"]
				lista_btn = [BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65, BTN_66,BTN_67,BTN_68]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila7_validar:
			if q in lst_fila7_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila7_validar.index(q)
				botón = lst_fila7[índ_elemento]
				lista_nom = ["70","71","72","73", "74", "75", "76","77","78"]
				lista_btn = [BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75, BTN_76,BTN_77,BTN_78]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		contador_fila = 1
		for q in lst_fila8_validar:
			if q in lst_fila8_validar[contador_fila:] and q != "":
				índ_elemento = lst_fila8_validar.index(q)
				botón = lst_fila8[índ_elemento]
				lista_nom = ["80","81","82","83", "84", "85", "86","87","88"]
				lista_btn = [BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85, BTN_86,BTN_87,BTN_88]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_fila += 1

		#A continuación inicia validación de columnas en 9 x 9.
		contador_columna = 1
		for q in lst_columna0_validar:
			if q in lst_columna0_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna0_validar.index(q)
				botón = lst_columna0[índ_elemento]
				lista_nom = ["00","10","20", "30", "40","50","60","70","80"]
				lista_btn = [BTN_00,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_80]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna1_validar:
			if q in lst_columna1_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna1_validar.index(q)
				botón = lst_columna1[índ_elemento]
				lista_nom = ["01","11","21","31","41","51","61","71","81"]
				lista_btn = [BTN_01,BTN_11,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61,BTN_71,BTN_81]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna2_validar:
			if q in lst_columna2_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna2_validar.index(q)
				botón = lst_columna2[índ_elemento]
				lista_nom = ["02","12","22", "32","42","52","62","72","82"]
				lista_btn = [BTN_02,BTN_12,BTN_22,BTN_32,BTN_42, BTN_52, BTN_62,BTN_72,BTN_82]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna3_validar:
			if q in lst_columna3_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna3_validar.index(q)
				botón = lst_columna3[índ_elemento]
				lista_nom = ["03","13","23","33","43","53","63","73","83"]
				lista_btn = [BTN_03,BTN_13,BTN_23,BTN_33,BTN_43, BTN_53, BTN_63,BTN_73,BTN_83]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna4_validar:
			if q in lst_columna4_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna4_validar.index(q)
				botón = lst_columna4[índ_elemento]
				lista_nom = ["04","14","24","34","44","54","64","74","84"]
				lista_btn = [BTN_04,BTN_14,BTN_24,BTN_34,BTN_44, BTN_54, BTN_64,BTN_74,BTN_84]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna5_validar:
			if q in lst_columna5_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna5_validar.index(q)
				botón = lst_columna5[índ_elemento]
				lista_nom = ["05","15","25","35","45","55","65","75","85"]
				lista_btn = [BTN_05,BTN_15,BTN_25,BTN_35,BTN_45, BTN_55, BTN_65,BTN_75,BTN_85]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna6_validar:
			if q in lst_columna6_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna6_validar.index(q)
				botón = lst_columna6[índ_elemento]
				lista_nom = ["06","16","26","36","46","56","66","76","86"]
				lista_btn = [BTN_06,BTN_16,BTN_26,BTN_36,BTN_46, BTN_56, BTN_66,BTN_76,BTN_86]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna7_validar:
			if q in lst_columna7_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna7_validar.index(q)
				botón = lst_columna7[índ_elemento]
				lista_nom = ["07","17","27","37","47","57","67","77","87"]
				lista_btn = [BTN_07,BTN_17,BTN_27,BTN_37,BTN_47, BTN_57, BTN_67,BTN_77,BTN_87]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

		contador_columna = 1
		for q in lst_columna8_validar:
			if q in lst_columna8_validar[contador_columna:] and q != "":
				índ_elemento = lst_columna8_validar.index(q)
				botón = lst_columna8[índ_elemento]
				lista_nom = ["08","18","28","38","48","58","68","78","88"]
				lista_btn = [BTN_08,BTN_18,BTN_28,BTN_38,BTN_48, BTN_58, BTN_68,BTN_78,BTN_88]
				for z in lista_nom:
					if botón == z:
						índ_nom = lista_nom.index(z)
						elem_btn = lista_btn[índ_nom]
						elem_btn.config(bg = "Red")
						msg_error = True 
			contador_columna += 1

	if msg_error == True and terminar == False:
		messagebox.showerror("Error", "Hay errores en el juego.")
		return

	for k in lst_validar:
		for o in k:
			if o == "":
				return False
	
	if msg_error == False and msg_terminar == True:
		if terminar == False:
			registrado = True
			terminar = True
			FN_top10(1)
			if sonido_selec.get() == 1:
				THRD_FN_sonido_aplausos = Thread (target = FN_sonido_aplausos, args = ())
				THRD_FN_sonido_aplausos.start()
			messagebox.showinfo("Terminado", "¡Felicitaciones, juego completado!")
			resultado = messagebox.askquestion("Terminar", "¿Desea jugar otro KenKen del mismo nivel?")
			if resultado == "yes":
				FN_otro("validar")
			else:
				BTN_terminar.config(state = DISABLED)
				BTN_validar.config(state = DISABLED)
				BTN_menú_jugar.config(state = NORMAL)
		return True

def FN_WIN_validar_completo ():
	WIN_menú.withdraw()
	global WIN_validar_completo
	WIN_validar_completo.deiconify()
	WIN_validar_completo.geometry("500x225")
	WIN_validar_completo.title("Función Extra")
	WIN_validar_completo.resizable(width = FALSE, height = FALSE)
	centrar (WIN_validar_completo)
	WIN_validar_completo.protocol("WM_DELETE_WINDOW", lambda : WIN_validar_completo.destroy())

	global validar_completo_respuesta

	LBL_título = Label(WIN_validar_completo, text = "Validación completa",font = ("Helvetica Neue", 18, "bold")).place(x = 150, y = 10)
	LBL_validar_completo = Label(WIN_validar_completo, text = "Validar completo:", font = ("Helvetica Neue", 16, "bold")).place(x = 10, y = 60)
	LBL_menú = Label(WIN_validar_completo, text = "Menú", font = (("Helvetica Neue", 15))).place (x = 181, y = 191)
	LBL_jugar = Label(WIN_validar_completo, text = "Jugar", font = (("Helvetica Neue", 15))).place (x = 281, y = 191)

	BTN_menú = Button(WIN_validar_completo, image = IMG_BTN_menú, height = 65, width = 65, borderwidth = 0, command = menú_volver).place (x = 175, y = 127)
	BTN_jugar = Button(WIN_validar_completo, image = IMG_BTN_WIN_menú_configurar, height = 65, width = 65, borderwidth = 0, command = FN_THRDs).place (x = 275, y = 127)

	RDB_validar_completo = Radiobutton(WIN_validar_completo, text = "Sí", font = ("Helvetica Neue", 14), variable = validar_completo_respuesta, value = 1).place(x = 195, y = 60)
	RDB_validar_completo = Radiobutton(WIN_validar_completo, text = "No", font = ("Helvetica Neue", 14), variable = validar_completo_respuesta, value = 0).place(x = 195, y = 90)

def FN_validar_completo ():
	contador = 0
	contador2 = 0
	índ_operación = 0
	lst_operación = []
	r = 0
	msg_error = False
	msg_terminar = True

	sel = nivel_selec.get()

	if sel == 33:
		índice = 0
	elif sel == 44:
		índice = 1
	elif sel == 55:
		índice = 2
	elif sel == 0:
		índice = 3
	elif sel == 77:
		índice = 4
	elif sel == 88:
		índice = 5
	elif sel == 99:
		índice = 6

	TXT_respuestas = open("Respuestas.txt","r")
	TXT_respuestas_read = TXT_respuestas.read()
	string = "["
	lista_completa = []
	lista_nivel = []
	lista_juego = []
	contador_nivel = 0

	for i in TXT_respuestas_read:
		if i != "[" and i != "]":
			string += i
			contador_control = 1
		elif i == "]" and contador_control != 0:
			string += i
			lista_nivel.append(eval(string))
			string = "["
			contador_nivel += 1
		if contador_nivel == 4:
			lista_completa.append(lista_nivel)
			lista_nivel = []
			contador_nivel = 0
			contador_control = 0
	global registrado
	global terminar

	for i in lst_validar:
		for j in i:
			if j == "":
				messagebox.showerror("Error", "Debe completar todas las casillas antes de validar completamente.")
				return

	for i in lst_validar:
		for j in i:
			if sel == 33:
				if str(j) != str(lista_completa[índice][elegido][contador][contador2]):
					botón = str(lst_juego_validar[contador][contador2])
					lista_nom = ["23","24","25","33","34","35","43","44","45"]
					lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45]
					for p in lista_nom:	
						if botón == str(p):
							índ_nom = lista_nom.index(p)
							elem_btn = lista_btn[índ_nom]
							elem_btn.config(bg = "Red")
				contador2 += 1
			elif sel == 44:
				if str(j) != str(lista_completa[índice][elegido][contador][contador2]):
					botón = str(lst_juego_validar[contador][contador2])
					lista_nom = ["23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
					lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
					for p in lista_nom:	
						if str(botón) == str(p):
							índ_nom = lista_nom.index(p)
							elem_btn = lista_btn[índ_nom]
							elem_btn.config(bg = "Red")
					contador2 += 1
				else:
					contador2 += 1
			elif sel == 55:
				if str(j) != str(lista_completa[índice][elegido][contador][contador2]):
					botón = str(lst_juego_validar[contador][contador2])
					lista_nom = ["26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
					lista_btn = [BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
					for p in lista_nom:	
						if str(botón) == str(p):
							índ_nom = lista_nom.index(p)
							elem_btn = lista_btn[índ_nom]
							elem_btn.config(bg = "Red")
					contador2 += 1
				else:
					contador2 += 1
			elif sel == 0:
				if str(j) != str(lista_completa[índice][elegido][contador][contador2]):
					botón = str(lst_juego_validar[contador][contador2])
					lista_nom = ["11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
					lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
					for p in lista_nom:	
						if str(botón) == str(p):
							índ_nom = lista_nom.index(p)
							elem_btn = lista_btn[índ_nom]
							elem_btn.config(bg = "Red")
					contador2 += 1
				else:
					contador2 += 1
			elif sel == 77:
				if str(j) != str(lista_completa[índice][elegido][contador][contador2]):
					botón = str(lst_juego_validar[contador][contador2])
					lista_nom = ["17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
					lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
					for p in lista_nom:	
						if str(botón) == str(p):
							índ_nom = lista_nom.index(p)
							elem_btn = lista_btn[índ_nom]
							elem_btn.config(bg = "Red")
					contador2 += 1
				else:
					contador2 += 1
			elif sel == 88:
				if str(j) != str(lista_completa[índice][elegido][contador][contador2]):
					botón = str(lst_juego_validar[contador][contador2])
					lista_nom = ["00","01","02","03","04","05","06","07","10","20","30","40","50","60","70","17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
					lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
					for p in lista_nom:	
						if str(botón) == str(p):
							índ_nom = lista_nom.index(p)
							elem_btn = lista_btn[índ_nom]
							elem_btn.config(bg = "Red")
					contador2 += 1
				else:
					contador2 += 1
			elif sel == 99:
				if str(j) != str(lista_completa[índice][elegido][contador][contador2]):
					botón = str(lst_juego_validar[contador][contador2])
					lista_nom = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
					lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
					for p in lista_nom:	
						if str(botón) == str(p):
							índ_nom = lista_nom.index(p)
							elem_btn = lista_btn[índ_nom]
							elem_btn.config(bg = "Red")
					contador2 += 1
				else:
					contador2 += 1
		contador2 = 0
		contador += 1

def FN_BTNS(button):
	global but_press
	global otro_juego
	but_press = button
	otro_juego = False

	lista_nom = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
	lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
	for p in lista_nom:
		if button == p:
			índ_nom = lista_nom.index(p)
			elem_btn = lista_btn[índ_nom]
			elem_btn.config(relief = SUNKEN, bg = "DarkTurquoise")
			cuadrícula_color()

def FN_add (add):
	if pausa == True:
		FN_pausa ()
	global but_press
	a = but_press
	cuadrícula_color()
	if a == "":
		messagebox.showerror("Error", "Primero debe seleccionar una casilla.")
		return
	validar(a, add)
	sel = nivel_selec.get()
	if sel == 33:
		lista_nom = ["23","24","25","33","34","35","43","44","45"]
		lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i) 
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = add, bg = "DarkTurquoise")
	elif sel == 44:
		lista_nom = ["23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
		lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = add, bg = "DarkTurquoise")
	elif sel == 55:
		lista_nom = ["26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
		lista_btn = [BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = add, bg = "DarkTurquoise")
	elif sel == 0:
		lista_nom = ["11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
		lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = add, bg = "DarkTurquoise")
	elif sel == 77:
		lista_nom = ["17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
		lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = add, bg = "DarkTurquoise")
	elif sel == 88:
		lista_nom = ["00","01","02","03","04","05","06","07","10","20","30","40","50","60","70","17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
		lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = add, bg = "DarkTurquoise")
	elif sel == 99:
		lista_nom = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
		lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = add, bg = "DarkTurquoise")

def FN_borrar ():
	if pausa == True:
		FN_pausa ()
	global but_press
	a = but_press
	if a == "":
		messagebox.showerror("Error", "Primero debe seleccionar una casilla.")
		return
	validar(a, "*")
	sel = nivel_selec.get()
	if sel == 33:
		lista_nom = ["23","24","25","33","34","35","43","44","45"]
		lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "")
	elif sel == 44:
		lista_nom = ["23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
		lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "")
	elif sel == 55:
		lista_nom = ["26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
		lista_btn = [BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "")
	elif sel == 0:
		lista_nom = ["11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
		lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "")
	elif sel == 77:
		lista_nom = ["17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
		lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "")
	elif sel == 88:
		lista_nom = ["00","01","02","03","04","05","06","07","10","20","30","40","50","60","70","17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
		lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "")
	elif sel == 99:
		lista_nom = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
		lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
		for i in lista_nom:
			if a == i:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "")

def FN_sonido_aplausos(): #Reproduce el sonido de aplausos si el usuario lo seleccionó.
	winsound.PlaySound("SOUND_aplausos.wav", winsound.SND_FILENAME)
#———————————————————————————————————————————————————————————Fin Cuadrícula—————————————————————————————————————————————————————————#
#—————————————————————————————————————————————————————————————Terminar—————————————————————————————————————————————————————————————#
def FN_terminar ():
	if iniciado == False:
		messagebox.showerror("Error", "El juego no se ha iniciado.")
		return
	global pausa
	if pausa == False:
		pausa = True
	resultado = messagebox.askquestion("Finalizar", "¿Está seguro de terminar el juego?")
	if resultado == "yes":
		global terminar
		terminar = True
		correcto = FN_validar ()
		if correcto == True and registrado == False:
			resultado2 = messagebox.askquestion("Guardar", "El juego está completo y correcto. ¿Desea guardar las estadísticas del juego?")
			if resultado2 == "yes":
				FN_top10 (1)
		global juego_num
		juego_num = 0
		WIN_jugar.withdraw()
		WIN_menú.deiconify()
	else:
		if pausa == True:
			pausa = False
#———————————————————————————————————————————————————————————Fin Terminar———————————————————————————————————————————————————————————#
#——————————————————————————————————————————————————————————————Top 10——————————————————————————————————————————————————————————————#
def FN_top10 (a):
	#TXT_top10 = eval(open("Top10.txt", "r").read()) #Abre el archivo, lo lee y lo convierte en diccionario.
	sel = nivel_selec.get()
	if sel == 33:
		índice = 0
	elif sel == 44:
		índice = 1
	elif sel == 55:
		índice = 2
	elif sel == 0:
		índice = 3
	elif sel == 77:
		índice = 4
	elif sel == 88:
		índice = 5
	elif sel == 99:
		índice = 6

	kenken_top10 = open("kenken_top10.dat","r")
	kenken_top10_read = kenken_top10.read()
	string = ""
	lista = []
	for i in kenken_top10_read:
		if i != "]":
			string += i
		else:
			string += i
			if string == "]":
				break
			while string[1] == "[":
				string = string[1:]
			while string[0] != "[":
				string = string[1:]
			lista.append(eval(string))
			string = ""
	lst_nivel = lista[índice]
	global h
	global m
	global s
	global h2
	global m2
	global s2

	if a == 1: #¿Escribir?
		FN_pausa()
		if a == 1 and timer_estado == False and clock_estado == True:
			h2 = h
			m2 = m
			s2 = s
		elif a == 1 and timer_estado == True and clock_estado == True:
			h2 = (h + h2) - h2
			m2 = (m + m2) - m2
			s2 = (s + s2) - s2

		contador = 0
		agregado = 0
		name = nombre.get()
		
		if h2 < 9:
			str_hora = "0" + str(h2)
		else:
			str_hora = str(h2)
		if m2 < 9:
			str_minuto = "0" + str(m2)
		else:
			str_minuto = str(m2)
		if s2 < 9:
			str_segundo = "0" + str(s2)
		else:
			str_segundo = str(s2)

		tiempo = str_hora + str_minuto + str_segundo

		if len(lst_nivel) < 10:
			if len(lst_nivel) == 0:
				lst_nivel.insert(contador, (name, tiempo))
			else:
				for j in lst_nivel:
					if int(j[1]) > int(tiempo):
						lst_nivel.insert(contador, (name, tiempo))
						agregado = 1
						break
					elif int(j[1]) == int(tiempo):
						lst_nivel.insert(contador + 1, (name, tiempo))
						agregado = 1
						break
					contador += 1
				if agregado == 0:
					lst_nivel.append((name, tiempo))
				contador = 0
				agregado = 0

		else:
			for j in lst_nivel:
				if int(j[1]) > int(tiempo):
					lst_nivel.pop(contador)
					lst_nivel.insert(contador, (name, tiempo))
					break
				elif int(j[1]) == int(tiempo):
					lst_nivel.insert(contador + 1, (name, tiempo))
					lst_nivel.pop()
					agregado = 1
					break
				contador += 1
			contador = 0

		kenken_top10 = open("kenken_top10.dat","w")
		kenken_top10.write(str(lista))

	else:
		y = 70
		pos = 1
		for k in lst_nivel:
			name = k[0]
			tiempo = k[1]
			lbl_top10 = Label(WIN_top10, text = str(pos) + ". " + name, font = (("Helvetica Neue", 12))).place (x = 5, y = y)
			lbl_top10_tiempo = Label(WIN_top10, text = tiempo[:2] + "     :      " + tiempo[2:4] + "        :        " + tiempo[4:], font = (("Helvetica Neue", 12))).place (x = 416, y = y)
			pos += 1
			y += 30

def WIN_top10 ():
	#WIN_jugar.withdraw()
	global WIN_top10
	WIN_top10 = Toplevel()
	WIN_top10.geometry("620x370")
	WIN_top10.title("Top 10")
	WIN_top10.resizable(width = FALSE, height = FALSE)
	centrar (WIN_top10)

	WIN_top10.protocol("WM_DELETE_WINDOW", lambda : WIN_top10.destroy())

	sel = nivel_selec.get()
	if sel == 33:
		top_lvl = "3 x 3"
	elif sel == 44:
		top_lvl = "4 x 4"
	elif sel == 55:
		top_lvl = "5 x 5"
	elif sel == 0:
		top_lvl = "6 x 6"
	elif sel == 77:
		top_lvl = "7 x 7"
	elif sel == 88:
		top_lvl = "8 x 8"
	elif sel == 99:
		top_lvl = "9 x 9"

	LBL_título = Label(WIN_top10, text = "Top 10 - " + top_lvl, font = (("Helvetica Neue", 16, "bold"))).place (x = 260, y = 10)
	LBL_nombre = Label(WIN_top10, text = "Nombre", font = (("Helvetica Neue", 13, "bold"))).place (x = 5, y = 40)
	LBL_horas = Label(WIN_top10, text = "Horas", font = (("Helvetica Neue", 13, "bold"))).place (x = 400, y = 40)
	LBL_minutos = Label(WIN_top10, text = "Minutos", font = (("Helvetica Neue", 13, "bold"))).place (x = 461, y = 40)
	LBL_segundos = Label(WIN_top10, text = "Segundos", font = (("Helvetica Neue", 13, "bold"))).place (x = 534, y = 40)

	FN_top10(0)
#————————————————————————————————————————————————————————————Fin Top 10————————————————————————————————————————————————————————————#
#————————————————————————————————————————————————————————————————————Fin Ventana Jugar——————————————————————————————————————————————————————————————————#
#———————————————————————————————————————————————————————————————————Ventana Configurar——————————————————————————————————————————————————————————————————#
def FN_WIN_configurar ():
	WIN_menú.withdraw()
	global WIN_configurar
	WIN_configurar = Toplevel()
	WIN_configurar.protocol("WM_DELETE_WINDOW", lambda : WIN_configurar.destroy())

	WIN_configurar.geometry("600x600")
	WIN_configurar.title("Configurar KENKEN")
	WIN_configurar.resizable(width = FALSE, height = FALSE)
	centrar (WIN_configurar)

	global nivel_selec
	nivel_selec = IntVar()
	global reloj_selec
	reloj_selec = IntVar()
	global lado_selec
	lado_selec = IntVar()
	global sonido_selec
	sonido_selec = IntVar()

	BTN_menú = Button(WIN_configurar, image = IMG_BTN_menú, height = 65, width = 65, borderwidth = 0, command = menú_volver).place (x = 210, y = 500)
	BTN_jugar = Button(WIN_configurar, image = IMG_BTN_WIN_menú_configurar, height = 65, width = 65, borderwidth = 0, command = FN_WIN_jugar).place (x = 320, y = 500)

	LBL_título = Label(WIN_configurar, text = "Configuración", font = ("Helvetica Neue", 18, "bold")).place(x = 220, y = 10)
	LBL_nivel = Label(WIN_configurar, text = "Nivel", font = ("Helvetica Neue", 14, "bold")).place(x = 27, y = 55)
	LBL_reloj = Label(WIN_configurar, text = "Reloj", font = ("Helvetica Neue", 14, "bold")).place(x = 170, y = 55)
	LBL_panel_pos = Label(WIN_configurar, text = "Posición del panel de números y el borrador:", font = ("Helvetica Neue", 13, "bold")).place(x = 27, y = 370)
	LBL_sonido = Label(WIN_configurar, text = "Sonido cuando termina el juego exitosamente:", font = ("Helvetica Neue", 13, "bold")).place(x = 27, y = 440)
	LBL_menú = Label(WIN_configurar, text = "Menú", font = ("Helvetica Neue", 12)).place(x = 221, y = 566)
	LBL_jugar = Label(WIN_configurar, text = "Jugar", font = ("Helvetica Neue", 12)).place(x = 331, y = 566)

	RDB_nivel_3x3 = Radiobutton(WIN_configurar, text = "3 x 3", font = ("Helvetica Neue", 14), variable = nivel_selec, value = 33).place(x = 27, y = 85)
	RDB_nivel_4x4 = Radiobutton(WIN_configurar, text = "4 x 4", font = ("Helvetica Neue", 14), variable = nivel_selec, value = 44).place(x = 27, y = 115)
	RDB_nivel_5x5 = Radiobutton(WIN_configurar, text = "5 x 5", font = ("Helvetica Neue", 14), variable = nivel_selec, value = 55).place(x = 27, y = 145)
	RDB_nivel_6x6 = Radiobutton(WIN_configurar, text = "6 x 6", font = ("Helvetica Neue", 14), variable = nivel_selec, value = 0).place(x = 27, y = 175)
	RDB_nivel_7x7 = Radiobutton(WIN_configurar, text = "7 x 7", font = ("Helvetica Neue", 14), variable = nivel_selec, value = 77).place(x = 27, y = 205)
	RDB_nivel_8x8 = Radiobutton(WIN_configurar, text = "8 x 8", font = ("Helvetica Neue", 14), variable = nivel_selec, value = 88).place(x = 27, y = 235)
	RDB_nivel_9x9 = Radiobutton(WIN_configurar, text = "9 x 9", font = ("Helvetica Neue", 14), variable = nivel_selec, value = 99).place(x = 27, y = 265)

	RDB_reloj_sí = Radiobutton(WIN_configurar, text = "Sí", font = ("Helvetica Neue", 14), variable = reloj_selec, value = 0).place(x = 170, y = 85)
	RDB_reloj_no = Radiobutton(WIN_configurar, text = "No", font = ("Helvetica Neue", 14), variable = reloj_selec, value = 1).place(x = 170, y = 115)
	RDB_reloj_timer = Radiobutton(WIN_configurar, text = "Timer", font = ("Helvetica Neue", 14), variable = reloj_selec, value = 2, command = FN_timer_configurar).place(x = 170, y = 145)

	RDB_derecha = Radiobutton(WIN_configurar, text = "Derecha", font = ("Helvetica Neue", 14), variable = lado_selec, value = 0).place(x = 392 , y = 366)
	RDB_izquierda = Radiobutton(WIN_configurar, text = "Izquierda", font = ("Helvetica Neue", 14), variable = lado_selec, value = 1).place(x = 392 , y = 396)

	RBD_sonido_no = Radiobutton(WIN_configurar, text = "No", font = ("Helvetica Neue", 14), variable = sonido_selec, value = 0).place(x = 392 , y = 436)
	RBD_sonido_sí = Radiobutton(WIN_configurar, text = "Sí", font = ("Helvetica Neue", 14), variable = sonido_selec, value = 1).place(x = 392 , y = 466)

def menú_volver (): #Regresar al menú principal, lo utilizan las WIN jugar, configurar, validar y ayuda.
	global juego_num
	global iniciado
	iniciado = False
	if reloj_selec.get() == 2 and juego_num == 0:
		if default_horas.get() == "0" and default_minutos.get() == "0" and default_segundos.get() == "0":
			messagebox.showerror("Error", "Si selecciona el timer los segundos, los minutos o las horas deben ser mayores a 0.")
			return
	juego_num = 0
	WIN_jugar.withdraw()
	WIN_configurar.withdraw()
	WIN_validar_completo.withdraw()
	WIN_ayuda.withdraw()
	WIN_menú.deiconify()

def FN_timer_configurar ():
	global default_horas 
	default_horas = StringVar() 
	global default_minutos 
	default_minutos = StringVar()
	global default_segundos 
	default_segundos = StringVar()

	default_horas.set("0")#Valor default de los SPNBX.   
	default_minutos.set("0")
	default_segundos.set("0")

	LBL_horas = Label(WIN_configurar, text = "Horas", font = ("Helvetica Neue", 13)).place(x = 300, y = 55)
	LBL_minutos = Label(WIN_configurar, text = "Minutos", font = ("Helvetica Neue", 13)).place(x = 355, y = 55)
	LBL_segundos = Label(WIN_configurar, text = "Segundos", font = ("Helvetica Neue", 13)).place(x = 420, y = 55)
	LBL_sugeridos = Label(WIN_configurar, text = "Tiempos sugeridos:", font = ("Helvetica Neue", 13)).place(x = 300, y = 130)
	

	SPNBX_horas = Spinbox(WIN_configurar, width = 2, font = ("Helvetica Neue", 12), from_ = 0, to = 3, textvariable = default_horas, wrap = True).place(x = 308, y = 90)
	SPNBX_minutos = Spinbox(WIN_configurar, width = 2, font = ("Helvetica Neue", 12), from_ = 0, to = 59, textvariable = default_minutos, wrap = True).place(x = 370, y = 90)
	SPNBX_segundos = Spinbox(WIN_configurar, width = 2, font = ("Helvetica Neue", 12), from_ = 0, to = 59, textvariable = default_segundos, wrap = True).place(x = 440, y = 90)

	LBL_sugerido3x3 = Label(WIN_configurar, text = "• Para el nivel 3 x 3: 5 minutos.", font = ("Helvetica Neue", 11)).place(x = 300, y = 160)
	LBL_sugerido4x4 = Label(WIN_configurar, text = "• Para el nivel 4 x 4: 10 minutos.", font = ("Helvetica Neue", 11)).place(x = 300, y = 190)
	LBL_sugerido5x5 = Label(WIN_configurar, text = "• Para el nivel 5 x 5: 20 minutos.", font = ("Helvetica Neue", 11)).place(x = 300, y = 220)
	LBL_sugerido6x6 = Label(WIN_configurar, text = "• Para el nivel 6 x 6: 25 minutos.", font = ("Helvetica Neue", 11)).place(x = 300, y = 250)
	LBL_sugerido7x7 = Label(WIN_configurar, text = "• Para el nivel 7 x 7: 30 minutos.", font = ("Helvetica Neue", 11)).place(x = 300, y = 280)
	LBL_sugerido8x8 = Label(WIN_configurar, text = "• Para el nivel 8 x 8: 35 minutos.", font = ("Helvetica Neue", 11)).place(x = 300, y = 310)
	LBL_sugerido9x9 = Label(WIN_configurar, text = "• Para el nivel 9 x 9: 40 minutos.", font = ("Helvetica Neue", 11)).place(x = 300, y = 340)

def FN_timer ():
	global timer_estado
	timer_estado = True

	global resultado
	resultado = ""
	global h
	global m
	global s
	global h2
	h2 = 0
	global m2
	m2 = 0
	global s2
	s2 = 0

	h = int(default_horas.get())
	m = int(default_minutos.get())
	s = int(default_segundos.get())

	while h != 0 or m != 0 or s >= 0:
		if terminar == True:
			LBL_clock = Label(WIN_jugar, text = " "+"0"+ "0" + "       " + "0"+ "0" + "        " + "0"+ "0" +" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			return
		if pausa == False:
			if s < 10 and m < 10 and h < 10:
				LBL_segundos = Label(WIN_jugar, text = " "+"0"+str(h) + "       " + "0"+str(m) + "        " + "0"+str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			elif s >= 10 and m < 10 and h < 10:
				LBL_segundos = Label(WIN_jugar, text = " "+"0"+str(h) + "       " + "0"+str(m) + "        " + str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			elif s >= 10 and m >= 10 and h < 10:
				LBL_segundos = Label(WIN_jugar, text = " "+"0"+str(h) + "       " + str(m) + "        " + str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			elif s < 10 and m < 10 and h >= 10:
				LBL_segundos = Label(WIN_jugar, text = " "+str(h) + "       " + "0"+str(m) + "        " + "0"+str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			elif s < 10 and m >= 10 and h >= 10:
				LBL_segundos = Label(WIN_jugar, text = " "+str(h) + "       " + str(m) + "        " + "0"+str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			elif s < 10 and m >= 10 and h < 10:
				LBL_segundos = Label(WIN_jugar, text = " "+"0"+str(h) + "       " + str(m) + "        " + "0"+str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			else:
				LBL_segundos = Label(WIN_jugar, text = " "+str(h) + "       " + str(m) + "        " + str(s)+" ", font = ("Helvetica Neue", 16)).place(x = 774, y = 44)
			time.sleep(0.99)
			s2 += 1
			if m2 == 59 and s == 60:
				h2 += 1
				m2 = 0
				s2 = 0
			elif s2 == 60:
				m2 += 1
				s2 = 0
			if m > 0 and s == 0:
				m -= 1
				s = 59
			elif h > 0 and m == 0 and s == 0:
				h -= 1
				m = 59
				s = 59
			elif h == 0 and m == 0 and s == 0:
				h = int(default_horas.get())
				m = int(default_minutos.get())
				s = int(default_segundos.get())
				if terminar == False and iniciado == True:
					resultado = messagebox.askquestion("Tiempo agotado", "El timer finalizó. ¿Desea continuar?")
					if resultado == "yes":
						clock()
						return
					messagebox.showinfo("Terminado", "Juego terminado.")	
					return
			s -= 1

def FN_otro (a):
	global juego_num
	global otro_juego
	global terminar
	global iniciado
	global but_press 
	global h
	global m
	global s

	if a == "otro":
		if iniciado == False:
			messagebox.showerror("Error", "El juego no se ha iniciado.")
			return

		resultado = messagebox.askquestion("Otro juego", "¿Está seguro de terminar este juego y empezar con otro?")
	else:
		resultado = "yes"

	if resultado == "yes":
		terminar = True
		iniciado = False
		but_press = ""
		h = 0
		m = 0
		s = 0
		WIN_jugar.withdraw()

		if len(juegos_probables) == 0:
			juego_num = 0
		otro_juego = True
		FN_THRDs()

def FN_reiniciar ():
	global terminar
	global iniciado 
	global otro_juego
	global but_press
	global h
	global m
	global s
	if iniciado == False:
		messagebox.showerror("Error", "El juego no se ha iniciado.")
		return

	resultado = messagebox.askquestion("Reiniciar", "¿Está seguro de reiniciar el juego? Perderá todo el progreso.")

	if resultado == "yes":
		terminar = True
		iniciado = False
		otro_juego = False
		but_press = ""
		h = 0
		m = 0
		s = 0
		BTN_iniciar.config(state = NORMAL)
		TXT_nombre.config(state = NORMAL)
		BTN_terminar.config(state = NORMAL)
		BTN_validar.config(state = NORMAL)
		BTN_menú_jugar.config(state = DISABLED)

		but_press = ""
		cuadrícula_color()
		sel = nivel_selec.get()
		if sel == 33:
			lista_nom = ["23","24","25","33","34","35","43","44","45"]
			lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45]
			for i in lista_nom:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "", state = DISABLED)
		elif sel == 44:
			lista_nom = ["23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
			lista_btn = [BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
			for i in lista_nom:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "", state = DISABLED)
		elif sel == 55:
			lista_nom = ["26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
			lista_btn = [BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
			for i in lista_nom:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "", state = DISABLED)
		elif sel == 0:
			lista_nom = ["11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
			lista_btn = [BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
			for i in lista_nom:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "", state = DISABLED)
		elif sel == 77:
			lista_nom = ["17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
			lista_btn = [BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
			for i in lista_nom:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "", state = DISABLED)
		elif sel == 88:
			lista_nom = ["00","01","02","03","04","05","06","07","10","20","30","40","50","60","70","17","27","37","47","57","67","71","72","73","74","75","76","77","11","12","13","14","15","16","21","31","41","51","61","26","36","46","56","62","63","64","65","66","23","24","25","33","34","35","43","44","45","22","32","42","52","53","54","55"]
			lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_10,BTN_20,BTN_30,BTN_40,BTN_50,BTN_60,BTN_70,BTN_17,BTN_27,BTN_37,BTN_47,BTN_57,BTN_67,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_21,BTN_31,BTN_41,BTN_51,BTN_61, BTN_26,BTN_36,BTN_46,BTN_56,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_23,BTN_24,BTN_25,BTN_33,BTN_34,BTN_35,BTN_43,BTN_44,BTN_45,BTN_22,BTN_32,BTN_42,BTN_52,BTN_53,BTN_54,BTN_55]
			for i in lista_nom:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "", state = DISABLED)
		elif sel == 99:
			lista_nom = ["00","01","02","03","04","05","06","07","08","10","11","12","13","14","15","16","17","18","20","21","22","23","24","25","26","27","28","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","50","51","52","53","54","55","56","57","58","60","61","62","63","64","65","66","67","68","70","71","72","73","74","75","76","77","78","80","81","82","83","84","85","86","87","88"]
			lista_btn = [BTN_00,BTN_01,BTN_02,BTN_03,BTN_04,BTN_05,BTN_06,BTN_07,BTN_08,BTN_10,BTN_11,BTN_12,BTN_13,BTN_14,BTN_15,BTN_16,BTN_17,BTN_18,BTN_20,BTN_21,BTN_22,BTN_23,BTN_24,BTN_25,BTN_26,BTN_27,BTN_28,BTN_30,BTN_31,BTN_32,BTN_33,BTN_34,BTN_35,BTN_36,BTN_37,BTN_38,BTN_40,BTN_41,BTN_42,BTN_43,BTN_44,BTN_45,BTN_46,BTN_47,BTN_48,BTN_50,BTN_51,BTN_52,BTN_53,BTN_54,BTN_55,BTN_56,BTN_57,BTN_58,BTN_60,BTN_61,BTN_62,BTN_63,BTN_64,BTN_65,BTN_66,BTN_67,BTN_68,BTN_70,BTN_71,BTN_72,BTN_73,BTN_74,BTN_75,BTN_76,BTN_77,BTN_78,BTN_80,BTN_81,BTN_82,BTN_83,BTN_84,BTN_85,BTN_86,BTN_87,BTN_88]
			for i in lista_nom:
				índ_nom = lista_nom.index(i)
				elem_btn = lista_btn[índ_nom]
				elem_btn.config(text = "", state = DISABLED)
#—————————————————————————————————————————————————————————————————Fin Ventana Configurar————————————————————————————————————————————————————————————————#
#—————————————————————————————————————————————————————————————————————Ventana Ayuda—————————————————————————————————————————————————————————————————————#
def FN_WIN_ayuda ():
	WIN_menú.withdraw()
	global WIN_ayuda
	WIN_ayuda = Toplevel()
	WIN_ayuda.protocol("WM_DELETE_WINDOW", lambda : WIN_ayuda.destroy())

	WIN_ayuda.geometry("300x400")
	WIN_ayuda.title("Ayuda KENKEN")
	WIN_ayuda.resizable(width = FALSE, height = FALSE)
	centrar (WIN_ayuda)

	LBL_título = Label(WIN_ayuda, text = "KenKen", font = ("Helvetica Neue", 18, "bold")).place(x = 101, y = 5)
	LBL_función = Label(WIN_ayuda, text = "Pasatiempo Aritmético", font = ("Helvetica Neue", 14)).place(x = 51, y = 35)
	LBL_desarrollador = Label(WIN_ayuda, text = "Desarrollador", font = ("Helvetica Neue", 12, "underline")).place(x = 97, y = 84)
	LBL_autor = Label(WIN_ayuda, text = "José Daniel Delgado Segura", font = ("Helvetica Neue", 12, "bold")).place(x = 37, y = 108)
	LBL_correo = Label(WIN_ayuda, text = "Correo electrónico", font = ("Helvetica Neue", 12, "underline")).place(x = 80, y = 137)
	LBL_gmail = Label(WIN_ayuda, text = "jddsegura14@gmail.com", font = ("Helvetica Neue", 12, "bold")).place(x = 53, y = 161)
	LBL_fecha = Label(WIN_ayuda, text = "KenKen 1.0\n21-05-2015", font = ("Helvetica Neue", 10)).place(x = 115, y = 190)

	LBL_menú = Label(WIN_ayuda, text = "Menú", font = ("Helvetica Neue", 12)).place(x = 221, y = 566)

	BTN_menú = Button(WIN_ayuda, image = IMG_BTN_menú, height = 65, width = 65, borderwidth = 0, command = menú_volver).place (x = 70, y = 240)
	BTN_manual = Button(WIN_ayuda, image = IMG_BTN_WIN_ayuda_manual, height = 65, width = 65, borderwidth = 0, command = lambda : os.startfile("kenken_manual_de_usuario.pdf")).place (x = 165, y = 240)
#———————————————————————————————————————————————————————————————————Fin Ventana Ayuda———————————————————————————————————————————————————————————————————#
#————————————————————————————————————————————————————————————————————Programa Principal—————————————————————————————————————————————————————————————————#
from tkinter import *
from threading import *
import os #Se utiliza en las funciones: FN_timer, clock, FN_WIN_jugar.
import time #Se utiliza en las funciones: FN_timer, clock, FN_WIN_jugar.
import random #Se utiliza en la función: FN_juegos_probables.
import winsound #Se utiliza en la función: FN_validar. 

WIN_menú = Tk()
WIN_menú.geometry("600x460")
WIN_menú.title("KENKEN")
WIN_menú.resizable(width = FALSE, height = FALSE)
centrar (WIN_menú)
WIN_menú.protocol("WM_DELETE_WINDOW", lambda : WIN_menú.destroy())

#-------------------Asignación Variables Programa Principal-------------------#
global IMG_BTN_WIN_menú_jugar
IMG_BTN_WIN_menú_jugar = PhotoImage(file = "IMG_BTN_WIN_menú_jugar.png")
global IMG_BTN_WIN_menú_configurar
IMG_BTN_WIN_menú_configurar = PhotoImage(file = "IMG_BTN_WIN_menú_configurar.png")
global IMG_BTN_WIN_menú_config
IMG_BTN_WIN_menú_config = PhotoImage(file = "IMG_BTN_WIN_menú_config.png")
global IMG_BTN_WIN_menú_adici
IMG_BTN_WIN_menú_adici = PhotoImage(file = "IMG_BTN_WIN_menú_adici.png")
global IMG_BTN_WIN_menú_ayuda
IMG_BTN_WIN_menú_ayuda = PhotoImage(file = "IMG_BTN_WIN_menú_ayuda.png")
global IMG_BTN_WIN_menú_salir
IMG_BTN_WIN_menú_salir = PhotoImage(file = "IMG_BTN_WIN_menú_salir.png")
global IMG_BTN_menú
IMG_BTN_menú = PhotoImage(file = "IMG_BTN_menú.png")
global IMG_BTN_WIN_jugar_borrar
IMG_BTN_WIN_jugar_borrar = PhotoImage(file = "IMG_BTN_WIN_jugar_borrar.png")
global IMG_BTN_WIN_validar_completo
IMG_BTN_WIN_validar_completo = PhotoImage(file = "IMG_BTN_WIN_validar_completo.png")
global IMG_BTN_WIN_ayuda_manual
IMG_BTN_WIN_ayuda_manual = PhotoImage(file = "IMG_BTN_WIN_ayuda_manual.png")

global IMG_BTN_num1
IMG_BTN_num1 = PhotoImage(file = "BTN_num1.png")
global IMG_BTN_num2
IMG_BTN_num2 = PhotoImage(file = "BTN_num2.png")
global IMG_BTN_num3
IMG_BTN_num3 = PhotoImage(file = "BTN_num3.png")
global IMG_BTN_num4
IMG_BTN_num4 = PhotoImage(file = "BTN_num4.png")
global IMG_BTN_num5
IMG_BTN_num5 = PhotoImage(file = "BTN_num5.png")
global IMG_BTN_num6
IMG_BTN_num6 = PhotoImage(file = "BTN_num6.png")
global IMG_BTN_num7
IMG_BTN_num7 = PhotoImage(file = "BTN_num7.png")
global IMG_BTN_num8
IMG_BTN_num8 = PhotoImage(file = "BTN_num8.png")
global IMG_BTN_num9
IMG_BTN_num9 = PhotoImage(file = "BTN_num9.png")

global IMG_BTN_WIN_jugar_iniciar
IMG_BTN_WIN_jugar_iniciar = PhotoImage(file = "IMG_BTN_WIN_jugar_iniciar.png")
global IMG_BTN_WIN_jugar_validar
IMG_BTN_WIN_jugar_validar = PhotoImage(file = "IMG_BTN_WIN_jugar_validar.png")
global IMG_BTN_WIN_jugar_otro
IMG_BTN_WIN_jugar_otro = PhotoImage(file = "IMG_BTN_WIN_jugar_otro.png")
global IMG_BTN_WIN_jugar_reiniciar
IMG_BTN_WIN_jugar_reiniciar = PhotoImage(file = "IMG_BTN_WIN_jugar_reiniciar.png")
global IMG_BTN_WIN_jugar_terminar
IMG_BTN_WIN_jugar_terminar = PhotoImage(file = "IMG_BTN_WIN_jugar_terminar.png")
global IMG_BTN_WIN_jugar_top10
IMG_BTN_WIN_jugar_top10 = PhotoImage(file = "IMG_BTN_WIN_jugar_top10.png")

global pausa #Pausa de clock.
pausa = False
global timer_estado
timer_estado = False
global clock_estado
clock_estado = False
global registrado
registrado = False
global terminar
terminar = False
global iniciado
iniciado = False
global otro_juego #Si es True significa que el usuario solicitó un nuevo juego.
otro_juego = False
global but_press
but_press = ""
global últ_btn
últ_btn = ""
global juego_num
juego_num = 0
global validar_completo #Se activa cuando el usuario selecciona que desea jugar con el validar completo.
validar_completo = False

#Valores por default:
global nivel_selec 
nivel_selec = IntVar()
global reloj_selec
reloj_selec = IntVar()
global lado_selec
lado_selec = IntVar()
global sonido_selec
sonido_selec = IntVar()
global validar_completo_respuesta
validar_completo_respuesta = IntVar()
global default_horas 
default_horas = StringVar() 
global default_minutos 
default_minutos = StringVar()
global default_segundos 
default_segundos = StringVar()

global WIN_jugar
WIN_jugar = Toplevel()
WIN_jugar.withdraw()
global WIN_configurar
WIN_configurar = Toplevel()
WIN_configurar.withdraw()
global WIN_validar_completo
WIN_validar_completo = Toplevel()
WIN_validar_completo.withdraw()
global WIN_ayuda
WIN_ayuda = Toplevel()
WIN_ayuda.withdraw()
#-----------------Fin Asignación Variables Programa Principal-----------------#

LBL_título = Label(WIN_menú, text = "Menú Principal", font = (("Helvetica Neue", 22, "bold"))).place(x = 205, y = 10)

LBL_jugar = Label(WIN_menú, text = "Jugar", font = (("Helvetica Neue", 16))).place (x = 77, y = 210)
LBL_config = Label(WIN_menú, text = "Configurar", font = (("Helvetica Neue", 16))).place (x = 257, y = 210)
LBL_adici = Label(WIN_menú, text = "Validar completo", font = (("Helvetica Neue", 16))).place (x = 416, y = 210) #Función extra
LBL_ayuda = Label(WIN_menú, text = "Ayuda", font = (("Helvetica Neue", 16))).place (x = 175, y = 405)
LBL_salir = Label(WIN_menú,  text = "Salir", font = (("Helvetica Neue", 16))).place (x = 380, y = 405)


BTN_jugar = Button(WIN_menú, image = IMG_BTN_WIN_menú_jugar, height = 130, width = 130, borderwidth = 0, command = FN_THRDs)
BTN_jugar.place (x = 40, y = 75)
BTN_config = Button(WIN_menú, image = IMG_BTN_WIN_menú_config, height = 130, width = 130, borderwidth = 0, command = FN_WIN_configurar)
BTN_config.place (x = 240, y = 75)
BTN_adici = Button(WIN_menú, image = IMG_BTN_WIN_menú_adici, height = 130, width = 130, borderwidth = 0, command = FN_WIN_validar_completo)
BTN_adici.place (x = 428, y = 75)
BTN_ayuda = Button(WIN_menú, image = IMG_BTN_WIN_menú_ayuda, height = 130, width = 130, borderwidth = 0, command = FN_WIN_ayuda)
BTN_ayuda.place (x = 140, y = 270)
BTN_salir = Button(WIN_menú, image = IMG_BTN_WIN_menú_salir, height = 130, width = 130, borderwidth = 0, command = WIN_menú.destroy)
BTN_salir.place (x = 335, y = 270)

WIN_menú.mainloop()
#————————————————————————————————————————————————————————————————————Fin Programa Principal—————————————————————————————————————————————————————————————————#
