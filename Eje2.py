
ops = ['+','D','C']
datos = True
Datos = []
def buscar(r, e):
    for i in range (len(r)):
        if r[i] == e:
            return True
    return False

def ops():
    return input("----------Menu----------\n Ingresar valor de 0 a 9  \n Registrar = +, \n registro doble = D, \n Cancelar puntuacion anterior = C, \n Final = F\n Ingresar ops:")

while datos == True:
    operaciones = ops()

    isnumeric = operaciones.isnumeric()

    if isnumeric == True:
        Datos.append(operaciones)
        print('Valor agregado')
    else:
        if operaciones == 'F':
            datos = False
        else:
            ops2 =buscar(ops, operaciones)
            if len(Datos) > 0 and ops2:
                Datos.append(operaciones)
                print('Valor agregado')
            else:
                print('Valor no agregado')
print(Datos)
ant = 0
newarray = []
total = 0
for dato in Datos:
    num = dato.isnumeric()
    if num == True:
        newarray.append(dato)
        ant = dato;
    elif dato == '+':
        longitud = len(newarray)
        newarray.append(int(newarray[longitud -1]) + int(newarray[longitud -2]))
    elif dato == 'D':
        longitud = len(newarray)
        newarray.append(int(newarray[longitud -1]) * 2)
    elif dato == 'C':
        longitud = len(newarray)
        newarray.pop()
print(newarray)
for valor in newarray:
    total += int(valor)
print(total)