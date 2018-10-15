# MemoGon
Programa para practicar la memoria, se evalua más adelantes que otros usos se le puede dar al programa.

### Serializar objetos **Pickle**

Conversión del diccionario `data` al archivo `data.pickle`
```python
import pickle

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3, 4],
    'b': ("character string", b"byte string"),
    'c': set([None, True, False])
}

with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
```

Se obtiene el contenido del archivo `data.pickle` a la variable `data`
```python
import pickle

with open('data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)
```

### Bibliografía

[pickle](https://docs.python.org/3.4/library/pickle.html) - 12.1.8 Examples