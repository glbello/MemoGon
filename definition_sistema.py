from definicion_item import Item
from random import choice, shuffle
import pickle
from os import listdir

class Sistema:
    def __init__(self):
        self.list_itemes = []
        self.cantidad_a_mostrar = 2

    def elegir_archivo(self):
	list_archivos = [archivo for archivo in listdir() if ".pickle" in archivo]
	for i, archivo in zip(range(len(list_archivos)), list_archivos):
		print("{}) {}".format(i, archivo.rstrip(".pickle")))

	print()	
	resp_user = input("Elija archivo: ")
	return list_archivos[int(resp_user)]


    def cargar_datos(self, path):
    	with open('data.pickle', 'rb') as f:
    		self.list_itemes = pickle.load(f)

    def iniciar_sistema(self):
    	print("-"*10 + " MemoGon " + "-"*10)
    	print()
    	print("A continuación seleccione el archivo que desea trabajar:")
    	
    	path_archivo = self.elegir_archivo()

    	with open('{}'.format(path_archivo), 'rb') as f:
            self.list_itemes = pickle.load(f)






        item = self.obtener_item(self.n)
        while item:
            self.mostrar_item(item)
            self.prueba(item)
            item = self.obtener_item(self.n)
        print("Fin del programa")
        
    def mostrar_item(self, item):
        item.mostrar()

    def prueba(self, item):
        resp_usuario = input(">> ")
        if resp_usuario == item.iden_b:
            item.acierta()
            print("Correcto! :D")
        else:
            i = 2
            print("Incorrecto :(")
            print("Respuesta correcta: {}".format(item.iden_b))
            print()
            print("Deberas volver a escribirlo dos veces más")
            while i != 0:
                print("Quedan {}".format(i))
                resp_usuario = input(">> ")
                if resp_usuario == item.iden_b:
                    print("Correcto")
                    i -= 1
                else:
                    print("Malo, vuelve a interntarlo")

    def item_a_preguntar(self):

        


if __name__ == "__main__":
	pass
	class box:
		def __init__(self, number):
			self.number = number
		def __repr__(self):
			return str(self.number)

	a = box(0)
	b = box(1)
	c = box(2)
	d = box(3)
	e = box(4)
	f = box(5)
	_list = [a,b,c,d,e,f]
	l = choice([i for i in _list if i.number > 9])
	print(l)
    # item_a = Item("raiz de 2", str(1.414))
    # item_b = Item("raiz de 3", str(1.732))
    # sist = Sistema()
    # sist.list_itemes.append(item_a)
    # sist.list_itemes.append(item_b)
    # sist.iniciar_sistema()

