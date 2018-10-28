from definicion_item import Item
import pickle


class GestorItemes:
	def __init__(self):
		# Creacion variables
		self.i = 1
		self.itemes = []
		self.iden_a = ""
		self.iden_b = ""


	# Definicion funciones
	def msg_mensaje_inicial(self):
		_rep = " ## Programa para agregar itemes a sistema ##\n\n"
		_rep += "¡¡ Si desea finalizar con la creación de itemes, escriba 'exit' !!\n"
		_rep += "¡¡ Si desea modificar el actual item, escriba '-1' !!\n"
		_rep += "¡¡ Si desea ver los itemes agregados, editar, eliminar, escriba '-2' !!\n"
		return _rep

	def msg_inicio_creacion_item(self, i):
		_rep = "Creación del item {}".format(i) 
		return _rep

	def mostrar_lista_itemes(self):
		_rep = "[\n"
		for i, it in zip(range(len(self.itemes)), self.itemes):
			_rep += "n° {}: {},\n".format(i, it)
		_rep += "]"
		return _rep

	def msg_consulta_eliminar_item(self):
		_rep = " Indique el n° item que desea eliminar\n"
		_rep +=" Si desea salir escriba -1"
		return _rep

	def crear_item(self, iden_a, iden_b):
		item = Item()
		item.dar_iden_a(iden_a)
		item.dar_iden_b(iden_b)
		return item

	def msg_creacion_item_exito(self, i):
		_rep = "item {} creado con éxito\n".format(i)
		_rep += "-"*20 + "\n"
		return _rep

	def obtener_iden(self, letra_iden):
		if letra_iden == "a":
			print("identificador A: ")
			iden = input(">> ")
		elif letra_iden == "b":
			print("identificador B: ")
			iden = input(">> ")
		return iden

	def msg_reseteando_item_actual(self):
		_rep = "Reseteando item actual\n"
		_rep += "-"*20 + "\n" 
		return _rep

	def modificar_archivo(self, path):
		with open('{}'.format(path), 'rb') as f:
    		self.itemes = pickle.load(f)

    	print(self.mostrar_lista_itemes())

	def generar_archivo(self):
		# Inicio programa
		print(self.msg_mensaje_inicial())

		while True:
			print(self.msg_inicio_creacion_item(self.i))

			self.iden_a = self.obtener_iden("a")
			if self.iden_a == "exit":
				break
			elif self.iden_a == "-1":
				print(self.msg_reseteando_item_actual())
				continue
			elif self.iden_a == "-2":
				print(self.mostrar_list_itemes(self.itemes))
				print(self.msg_consulta_eliminar_item())

				resp_user = input("n°: ")
				while True:
					if resp_user == "-1":
						break
					if resp_user.isdigit():
						if int(resp_user) in range(len(self.itemes)):
							self.itemes.pop(int(resp_user))
						break
					else:
						print("ERROR! vuelva a ingresarlo")
						resp_user = input("n°: ")
				continue

			print()

			self.iden_b = self.obtener_iden("b")
			if self.iden_b == "exit":
				break
			elif self.iden_b == "-1":
				print(self.msg_reseteando_item_actual())
				continue
			elif self.iden_a == "-2":
				print(self.mostrar_list_itemes(self.itemes))
				print(self.msg_consulta_eliminar_item())
				resp_user = input("n°: ")
				while True:
					if resp_user == "-1":
						break
					if resp_user.isdigit():
						if int(resp_user) in range(len(self.itemes)):
							self.itemes.pop(int(resp_user))
						break
					else:
						print("ERROR! vuelva a ingresarlo")
						resp_user = input("n°: ")
				
				continue

			print()

			item = self.crear_item(iden_a, iden_b)
			self.itemes.append(item)

			print(msg_creacion_item_exito(self.i))
			self.i += 1

		print("Indique el nombre del archivo a guardar:")
		resp_user = input(">> ")

		with open('{}.pickle'.format(resp_user), 'wb') as f:
		    pickle.dump(itemes, f, pickle.HIGHEST_PROTOCOL)

		print()
		print("Archivo creado con éxito")







	

if __name__ == "__main__":
	generador_itemes = GeneradorItemes()
	generador_itemes.generar_archivo()
    # item_a = Item("raiz de 2", str(1.414))
    # item_b = Item("raiz de 3", str(1.732))
    # sist = Sistema()
    # sist.banco_itemes.append(item_a)
    # sist.banco_itemes.append(item_b)
    # sist.iniciar_sistema()

