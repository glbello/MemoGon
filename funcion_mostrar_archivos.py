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
	class box:
		def __init__(self, valor):
			self.valor = valor

		def __repr__(self):
			return str(self.valor)

	a = box(1)
	b = box(3)
	c = box(5)
	d = box(2)
	e = box(6)
	f = box(9)

	l = [a, b, c, d, e, f]

	ll = max(l, key=lambda x : x.valor)
	print(ll)
	# ll = [i for i in l if i.valor > 4]
	# print(ll)


	


















