from os import listdir


def elegir_archivo():
	list_archivos = [archivo for archivo in listdir() if ".pickle" in archivo]
	for i, archivo in zip(range(len(list_archivos)), list_archivos):
		print("{}) {}".format(i, archivo.rstrip(".pickle")))

	print()	
	resp_user = input("Elija archivo: ")
	return list_archivos[int(resp_user)]


if __name__ == "__main__":
	# list_archivos = (archivo for archivo in listdir() if ".pickle" in archivo)
	# print(len(list_archivos))
	# print(list_archivos)
	pass
















