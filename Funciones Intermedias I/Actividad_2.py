estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(estudiantes):
    for diccionario in estudiantes:
        for clave, valor in diccionario.items():
             print (f"{clave}:{valor}")
        print()

iterateDictionary(estudiantes)