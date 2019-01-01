from os import listdir

PATH_CARPETA_PICKLES = "data_pickle"


def elegir_archivo():
    list_archivos = [archivo for archivo in listdir(
        PATH_CARPETA_PICKLES) if ".pickle" in archivo]
    for i, archivo in zip(range(len(list_archivos)), list_archivos):
        print("{}) {}".format(i, archivo.rstrip(".pickle")))

    print()
    while True:
        try:
            resp_user = input("Elija archivo: ")
            return "{}/{}".format(PATH_CARPETA_PICKLES, list_archivos[int(resp_user)])
        except IndexError:
            print("ERROR valor ingresado fuera del rango, vuelva a intentarlo")
            print()


if __name__ == "__main__":
    print(listdir("data_pickle"))
