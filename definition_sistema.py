from definicion_item import Item
from random import choice, shuffle
import pickle
from os import listdir


class Sistema:

    def __init__(self):
        self.list_itemes = []
        self.cantidad_a_mostrar = 2

    def elegir_archivo(self):
        list_archivos = [archivo for archivo in listdir()
                         if ".pickle" in archivo]
        for i, archivo in zip(range(len(list_archivos)), list_archivos):
            print("{}) {}".format(i, archivo.rstrip(".pickle")))

        print()
        while True:
            resp_user = input("Elija archivo: ")
            try:
                return list_archivos[int(resp_user)]
            except (IndexError, ValueError):
                print("ERROR vuelva a intentarlo")

    def cargar_datos(self, path):
        with open('data.pickle', 'rb') as f:
            self.list_itemes = pickle.load(f)

    def indicar_cant_veces_mostrar(self):
        print("Indique la cantidad de veces que desea que se muestre las palabras:")
        print("(Por defecto: 2")
        print("")

        while True:
            try:
                resp_user = input(">> ")
                if resp_user == "":
                    return 2

                resp_user = int(resp_user)

                if resp_user <= 0:
                    print(
                        "ERROR no puede ser menor o igual a cero, vuelva a intentarlo")
                    continue
                return resp_user

            except ValueError:
                print("ERROR vuelva a intentarlo")

    def iniciar_sistema(self):
        print("-" * 10 + " MemoGon " + "-" * 10)
        print()
        print("A continuación seleccione el archivo que desea trabajar:")

        path_archivo = self.elegir_archivo()

        with open('{}'.format(path_archivo), 'rb') as f:
            self.list_itemes = pickle.load(f)

        cant_i_menor_mostrada = 0  # numero random >0
        print("Si desea escuchar nuevamente el audio ingrese '1'\n")
        while self.cantidad_a_mostrar > cant_i_menor_mostrada:

            item_menor_cantidad_mostrada = min(
                self.list_itemes, key=lambda x: x.veces_mostradas)

            cant_i_menor_mostrada = item_menor_cantidad_mostrada.veces_mostradas

            item = choice(
                [i for i in self.list_itemes if i.veces_mostradas == cant_i_menor_mostrada])

            item.reproducir_sonido()

            while True:
                resp_user = input(">> ")
                resp_user = resp_user.strip()
                if resp_user != '1':
                    break
                item.reproducir_sonido()

            if resp_user == item.iden_a:
                print("Correcto!\n")
            else:
                print("Incorrecto, la respuesta correcta era:")
                print(item.iden_a)
                item.reproducir_sonido()
                i = self.cantidad_a_mostrar
                print("Ahora deberas volver a escribirlo {} mas\n".format(i))
                while True:
                    while True:
                        print(item.iden_a)
                        print()
                        resp_user = input(">> ")
                        resp_user = resp_user.strip()
                        item.reproducir_sonido()
                        if resp_user != '1':
                            break
                        item.reproducir_sonido()

                    if resp_user == item.iden_a:
                        i -= 1
                        print("Correcto!\n")
                        if i == 0:
                            break
                        print("Ya te quedan {} veces más".format(i))
                    else:
                        print("Mal vuelve a interntarlo\n")
                        item.reproducir_sonido()

                print("Ahora escribe su traduccion al espanol")

            while True:
                resp_user = input(">> ")
                resp_user = resp_user.strip()
                if resp_user != '1':
                    break
                item.reproducir_sonido()

            if resp_user == item.iden_b:
                print("Correcto!\n")
            else:
                print("Incorrecto, la respuesta correcta era:")
                print(item.iden_b)
                i = self.cantidad_a_mostrar
                print("Ahora deberas volver a escribirlo {} mas\n".format(i))
                while True:
                    while True:
                        print(item.iden_b)
                        print()
                        resp_user = input(">> ")
                        resp_user = resp_user.strip()
                        if resp_user != '1':
                            break
                        item.reproducir_sonido()

                    if resp_user == item.iden_b:
                        i -= 1
                        print("Correcto!\n")
                        if i == 0:
                            break
                        print("Ya te quedan {} veces más".format(i))
                    else:
                        print("Mal vuelve a interntarlo\n")

        print("Fin del programa")


if __name__ == "__main__":
    s = Sistema()
    s.iniciar_sistema()
