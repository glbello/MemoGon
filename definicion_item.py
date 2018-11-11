import datetime


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

    def dar_iden_a(self, iden_a):
        self.iden_a = iden_a

    def dar_iden_b(self, iden_b):
        self.iden_b = iden_b

    def mostrar(self):
        print(self.iden_a)
        self.veces_mostradas += 1

    def acierta(self):
        self.veces_acertadas += 1

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
    resp_user = input("n°: ")
    while True:
        if resp_user == "-1":
            break
        if resp_user.isdigit():
            if int(resp_user) > 10:
                break
        else:
            print("ERROR! vuelva a ingresarlo")
            resp_user = input("n°: ")
    print("Terminamos")