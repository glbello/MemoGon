def destacar(palabra):
    palabra = palabra.upper()
    gato = 4
    espaciado = 2
    raya_con_borde = "#" * 4 + "#" * espaciado + \
        "#" * len(palabra) + "#" * espaciado + "#" * 4
    raya_con_espacio = "#" * 4 + " " * espaciado + \
        " " * len(palabra) + " " * espaciado + "#" * 4
    raya_con_palabra = "#" * 4 + " " * espaciado + \
        palabra + " " * espaciado + "#" * 4
    _rep = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        raya_con_borde, raya_con_borde, raya_con_espacio, raya_con_palabra, raya_con_espacio, raya_con_borde, raya_con_borde)
    return _rep


if __name__ == "__main__":
    pass
