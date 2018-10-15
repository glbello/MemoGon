from definicion_item import Item
import pickle

# item_a = Item("raiz de 2", str(1.414))
#     item_b = Item("raiz de 3", str(1.732))
#     list_itemes = [item_a, item_b]

#     with open('data.pickle', 'wb') as f:
#     	pickle.dump(list_itemes, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
	with open('data.pickle', 'rb') as f:
		data = pickle.load(f)
		print()



