
lista=[5,2,3,2,1,4]

def valores_mayores_que_el_segundo(lista):
    
    resultado=[]
    
    for number in lista:
        if number > lista[1]:
            resultado.append(number)
    print(resultado)

valores_mayores_que_el_segundo(lista)
