from definicion_item import Item
from random import choice, shuffle
import pickle

class Sistema:
    def __init__(self):
        self.banco_itemes = []
        self.n = 3

    def cargar_datos(self, path):
    	with open('data.pickle', 'rb') as f:
    		self.banco_itemes = pickle.load(f)

    def iniciar_sistema(self):
        shuffle(self.banco_itemes)
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

    def obtener_item(self, n):
        item = min(self.banco_itemes, key= lambda item:item.veces_acertadas)
        if item.veces_acertadas == n:
            return False
        return item


if __name__ == "__main__":
    item_a = Item("raiz de 2", str(1.414))
    item_b = Item("raiz de 3", str(1.732))
    sist = Sistema()
    sist.banco_itemes.append(item_a)
    sist.banco_itemes.append(item_b)
    sist.iniciar_sistema()

