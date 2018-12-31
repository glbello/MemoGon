# MemoGon
Programa para practicar la memoria, se evalua más adelantes que otros usos se le puede dar al programa.

### Serializar objetos **Pickle**

Conversión del diccionario `data` al archivo `data.pickle`
```python
import pickle

data = {
    'a': [1, 2.0, 3, 4],
    'b': ("character string", b"byte string"),
    'c': set([None, True, False])
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
```

Se obtiene el contenido del archivo `data.pickle` a la variable `data`
```python
import pickle

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
```

### Ver archivos de carpeta local

```python
from os import listdir

lista_archivos = listdir()
```

### Ver archivos de carpeta local

Para reproducir sonidos, usar `playsound` (solo formatos wav)

```python
import playsound

playsound.playsound("musica.wav")
```
Si intenta con mp3 saldrá error de iniciar MCI.


### Bibliografía

[pickle](https://docs.python.org/3.4/library/pickle.html) - 12.1.8 Examples