def countdown(number):
    lista=[]
    for i in range(number, 0, -1):
        lista.append(i)
    return lista


countdown(5)
print (countdown(5))