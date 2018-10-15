from definicion_item import Item
import pickle

print(" ## Programa para agregar itemes a sistema ##")
print()
print("¡¡ Si desea finalizar la operación, escriba 'exit' !!")
print("¡¡ Si desea modificar el actual item, escriba '-1' !!")
print()
print()
i = 1
itemes = []

iden_a = ""
iden_b = ""
while True:
	print("Creación del item {}".format(i))
	print()
	print("identificador A: ")
	iden_a = input(">> ")
	if iden_a == "exit":
		break
	elif iden_a == "-1":
		print("Reseteando item actual")
		print('-'*20 + "\n")
		continue
	print()
	print("identificador B: ")
	iden_b = input(">> ")
	if iden_b == "exit":
		break
	elif iden_b == "-1":
		print("Reseteando item actual")
		print('-'*20 + "\n")
		continue
	print()
	item = Item()
	item.dar_iden_a(iden_a)
	item.dar_iden_b(iden_b)
	itemes.append(item)
	print("item {} creado con éxito".format(i))
	print('-'*20 + "\n")
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

