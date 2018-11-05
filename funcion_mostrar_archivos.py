from os import listdir


def elegir_archivo():
	list_archivos = [archivo for archivo in listdir if ".pickle" in archivo]
	resp_user = input("Elija archivo: ")
	return list_archivos[int(resp_user) + 1]


if __name__ == "__main__":
	l = [1,2,3,4,5]
	ll = [p for p in l if p >  2]
	print(ll)