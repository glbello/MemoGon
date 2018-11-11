from definicion_item import Item
from funcion_mostrar_archivos import elegir_archivo
import pickle


class GestorItemes:
    def __init__(self):
        # Creacion variables
        self.itemes = []
        self.iden_a = ""
        self.iden_b = ""
        self._i = 0

    @property
    def i(self):
        self._i = len(self.itemes)
        return self._i

    @i.setter
    def i(self, value):
        self._i = value
        return self._i  
    
    # Definicion funciones
    def msg_mensaje_inicial(self):
        _rep = " ---- Sistema para creación de archivo de itemes ----\n"
        return _rep

    def indicacion_opciones_iniciales(self):
        _rep = "1) Crear archivo\n"
        _rep += "2) Editar archivo\n"
        print(_rep)
        resp_user = input(">> ")
        while True:
            try:
                while True:
                    resp_user = int(resp_user)
                    if resp_user not in [1,2]:
                        break
                        print("Error, vuelva a ingresarlo")
                return resp_user
            except ValueError:
                print("Error, vuelva a ingresarlo")

    def msg_indicaciones_usuario(self):
        _rep = "--> Si desea finalizar, escriba 'exit'\n"
        _rep += "--> Si desea modificar el actual item, escriba '-1'\n"
        _rep += "--> Si desea ver los itemes agregados o eliminar algún item, escriba '-2'\n"
        return _rep     

    def msg_inicio_creacion_item(self, i):
        _rep = "Creación del item {}".format(i) 
        return _rep

    def mostrar_lista_itemes(self):
        _rep = "[\n"
        for i, it in zip(range(len(self.itemes)), self.itemes):
            _rep += "n° {}: {},\n".format(i, it)
        _rep += "]\n"
        return _rep

    def msg_consulta_eliminar_item(self):
        _rep = "Indique el n° item que desea eliminar\n"
        _rep +="Si desea salir escriba -1"
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
        _rep = "item {} reseteado\n".format(self.i)
        _rep += "-"*20 + "\n" 
        return _rep

    def modificar_archivo(self, path):
        with open('{}'.format(path), 'rb') as f:
            self.itemes = pickle.load(f)
        self.generar_archivo(mode=1)

    def generar_archivo(self, mode=0):
        if mode == 1:
            print("Estos son los itemes que tiene en este archivo")
            print(self.mostrar_lista_itemes())

        while True:

            print(self.msg_indicaciones_usuario())
            print(self.msg_inicio_creacion_item(self.i))

            self.iden_a = self.obtener_iden("a")
            print()
            if self.iden_a == "exit":
                break
            elif self.iden_a == "-1":
                print(self.msg_reseteando_item_actual())
                continue
            elif self.iden_a == "-2":
                print(self.mostrar_lista_itemes())
                print(self.msg_consulta_eliminar_item())

                resp_user = input(">> ")
                while True:
                    if resp_user == "-1":
                        print()
                        break
                    if resp_user.isdigit():
                        if int(resp_user) in range(len(self.itemes)):
                            self.itemes.pop(int(resp_user))
                            print()
                            break
                        else:
                            print("ERROR! vuelva a ingresarlo")
                            resp_user = input(">> ")
                    else:
                        print("Error, vuelva a intentarlo")
                continue


            self.iden_b = self.obtener_iden("b")
            print()
            if self.iden_b == "exit":
                break
            elif self.iden_b == "-1":
                print(self.msg_reseteando_item_actual())
                continue
            elif self.iden_a == "-2":
                print(self.mostrar_lista_itemes(self.itemes))
                print(self.msg_consulta_eliminar_item())
                resp_user = input("n°: ")
                while True:
                    if resp_user == "-1":
                        print()
                        break
                    if resp_user.isdigit():
                        if int(resp_user) in range(len(self.itemes)):
                            self.itemes.pop(int(resp_user))
                            print()
                            break
                        else:
                            print("ERROR! vuelva a ingresarlo")
                            resp_user = input("n°: ")
                    else:
                        print("Error, vuelva a intentarlo")                
                continue

            print()

            item = self.crear_item(self.iden_a, self.iden_b)
            self.itemes.append(item)

            print(self.msg_creacion_item_exito(self.i))

        if mode == 0:
            print("Indique el nombre del archivo a guardar:")
            resp_user = input(">> ")

            with open('{}.pickle'.format(resp_user), 'wb') as f:
                pickle.dump(self.itemes, f, pickle.HIGHEST_PROTOCOL)

            print()
            print("Archivo creado con éxito")

        elif mode == 1:
            with open('{}'.format(self.path_archivo), 'wb') as f:
                pickle.dump(self.itemes, f, pickle.HIGHEST_PROTOCOL)

            print("Archivo {} modificado con éxito".format(self.path_archivo))

    def iniciar_programa(self):      
        resp_user = self.indicacion_opciones_iniciales()
        print()
        if resp_user == 1:
                self.generar_archivo()
            elif resp_user == 2:
                self.path_archivo = elegir_archivo()
                print()
                self.modificar_archivo(self.path_archivo)
            
    

if __name__ == "__main__":
    generador_itemes = GestorItemes()
    generador_itemes.iniciar_programa()
    # item_a = Item("raiz de 2", str(1.414))
    # item_b = Item("raiz de 3", str(1.732))
    # sist = Sistema()
    # sist.banco_itemes.append(item_a)
    # sist.banco_itemes.append(item_b)
    # sist.iniciar_sistema()

