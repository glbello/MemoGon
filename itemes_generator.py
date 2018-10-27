from definicion_item import Item
import pickle

# Definicion funciones
def msg_mensaje_inicial():
	_rep = " ## Programa para agregar itemes a sistema ##\n\n"
	_rep += "¡¡ Si desea finalizar con la creación de itemes, escriba 'exit' !!\n"
	_rep += "¡¡ Si desea modificar el actual item, escriba '-1' !!\n"
	_rep += "¡¡ Si desea ver los itemes agregados, editar, eliminar, escriba '-2' !!\n"
	return _rep

def msg_inicio_creacion_item(i):
	_rep = "Creación del item {}".format(i) 
	return _rep

def mostrar_list_itemes(lista_itemes):
	_rep = "[\n"
	for i, it in zip(range(len(lista_itemes)), lista_itemes):
		_rep += "n° {}: {},\n".format(i, it)
	_rep += "]"
	return _rep

def msg_consulta_eliminar_item():
	_rep = " Indique el n° item que desea eliminar\n"
	_rep +=" Si desea salir escriba -1"
	return _rep

def crear_item(iden_a, iden_b):
	item = Item()
	item.dar_iden_a(iden_a)
	item.dar_iden_b(iden_b)
	return item

def msg_creacion_item_exito(i):
	_rep = "item {} creado con éxito\n".format(i)
	_rep += "-"*20 + "\n"
	return _rep

def obtener_iden(letra_iden):
	if letra_iden == "a":
		print("identificador A: ")
		iden = input(">> ")
	elif letra_iden == "b":
		print("identificador B: ")
		iden = input(">> ")
	return iden

def msg_reseteando_item_actual():
	_rep = "Reseteando item actual\n"
	_rep += "-"*20 + "\n" 
	return _rep


# Creacion variables
i = 1
itemes = []
iden_a = ""
iden_b = ""

# Inicio programa
print(msg_mensaje_inicial())

while True:
	print(msg_inicio_creacion_item(i))
	iden_a = obtener_iden("a")
	if iden_a == "exit":
		break
	elif iden_a == "-1":
		print(msg_reseteando_item_actual())
		continue
	elif iden_a == "-2":
		print(mostrar_list_itemes(itemes))
		print(msg_consulta_eliminar_item())

		resp_user = input("n°: ")
		while True:
			if resp_user == "-1":
				break
			if resp_user.isdigit():
				if int(resp_user) in range(len(itemes)):
					itemes.pop(int(resp_user))
				break
			else:
				print("ERROR! vuelva a ingresarlo")
				resp_user = input("n°: ")
		if resp_user == "-1":
				continue

	print()

	iden_b = obtener_iden("b")
	if iden_b == "exit":
		break
	elif iden_b == "-1":
		print(msg_reseteando_item_actual())
		continue
	elif iden_a == "-2":
		print(mostrar_list_itemes(itemes))
		print(msg_consulta_eliminar_item())
				resp_user = input("n°: ")
		while True:
			if resp_user == "-1":
				break
			if resp_user.isdigit():
				if int(resp_user) in range(len(itemes)):
					itemes.pop(int(resp_user))
				break
			else:
				print("ERROR! vuelva a ingresarlo")
				resp_user = input("n°: ")
		if resp_user == "-1":
				continue

	print()

	item = crear_item(iden_a, iden_b)
	itemes.append(item)

	print(msg_creacion_item_exito(i))
	i += 1

with open('data.pickle', 'wb') as f:
    pickle.dump(itemes, f, pickle.HIGHEST_PROTOCOL)

print()
print("Archivo creado con éxito")
	

if __name__ == "__main__":
	pass
    # item_a = Item("raiz de 2", str(1.414))
    # item_b = Item("raiz de 3", str(1.732))
    # sist = Sistema()
    # sist.banco_itemes.append(item_a)
    # sist.banco_itemes.append(item_b)
    # sist.iniciar_sistema()

