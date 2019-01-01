import datetime
from playsound import playsound
from random import choice


class Item:
    _id = 0

    def __init__(self):
        self.id = Item._id
        Item._id += 1

        self.iden_a = ""
        self.iden_b = ""
        self.fecha_creacion = datetime.datetime.now()  # fecha actual de creacion
        self.veces_mostradas = 0
        self.veces_acertadas = 0
        self.direccion_sonido = []

    def dar_iden_a(self, iden_a):
        self.iden_a = iden_a

    def dar_iden_b(self, iden_b):
        self.iden_b = iden_b

    def mostrar(self):
        print(self.iden_a)
        self.veces_mostradas += 1

    def agregar_sonido(self, nombre_archivo):
        self.direccion_sonido.append(nombre_archivo)

    def reproducir_sonido(self):
        playsound(choice(self.direccion_sonido))

    def acierta(self):
        self.veces_acertadas += 1

    def preguntar_iden_b(self, resp_user):
        if resp_user != self.iden_b:
            return False
        else:
            return True

    @property
    def tasa_aciertos(self):
        if self.veces_mostradas != 0:
            return self.veces_acertadas / self.veces_mostradas
        else:
            return 0

    def resetear(self):
        self.veces_mostradas = 0
        self.veces_acertadas = 0

    def __repr__(self):
        _repr = "{} --> {}".format(self.iden_a, self.iden_b)
        return _repr

if __name__ == "__main__":
    pass
