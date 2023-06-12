dojo= {
    'ubicaciones': ['San José', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for clave, valor in dojo.items():
        print(f"{len(valor)} {clave.upper()}")
        for elemento in valor:
            print(f"{elemento}")
        print()

print(printInfo(dojo))