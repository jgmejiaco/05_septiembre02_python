# Analogía con un Objeto

diccionario = {
    'nombre':"Sara",
    'edad':7,
    'hinchaVerde':True,
    'estatura':1.50,
    'tieneVoz':False,
    'nacimiento':"2014-10-12",
}

print(diccionario)
# print(diccionario.nombre)
# print(diccionario.edad)
# print(diccionario.hinchaVerde)
# print(diccionario.estatura)
# print(diccionario.tieneVoz)
# print(diccionario.nacimiento)

#Recorriendo un diccionario
for clave,valor in diccionario.items():
    print(clave, valor)