estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(first_name, estudiantes):
    for diccionario in estudiantes:
        print (diccionario[first_name])
        print()

iterateDictionary2('first_name', estudiantes)