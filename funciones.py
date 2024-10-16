# Una empresa se dedica al almacenamiento y posterior distribución de juguetes en el interior
# del país. Para ello cuentan con 5 depósitos distribuidos en diferentes provincias (PBA,
# CABA, Chubut, Tucumán y Mendoza).
# Los depósitos pueden almacenar 6 tipos diferentes de juguetes: autos, muñecas, trenes,
# peluches, spinners y cartas.
# La oficina central, recibe mensualmente una planilla de existencias donde se indican las
# existencias de cada juguete para cada depósito.

# Realizar un menú de opciones:
# 1. Obtener existencias: para ello deberá cargar en el main la existencia de cada juguete
# en todos los depósitos. En una lista de cantidad, no uno por uno. Por lo que habrá una
# matriz con 3 columnas o filas, provincia, tipo de juguete y cantidad.

deposito = ['PBA', 'CABA', 'Chubut', 'Tucuman', 'Mendoza']
tipo_juguete = ['autos', 'muñecas', 'trenes', 'peluches', 'spinners', 'cartas']

def cargar_existencias(existencias):
    for i in range(len(deposito)):
        print(f'Ingresar existencias para el depósito {deposito[i]}:')
        for j in range(len(tipo_juguete)):
            existencias[i][j] = int(input(f'Ingrese la cantidad de {tipo_juguete[j]}: '))
    return existencias

# 2. Calcular por cada depósito la cantidad total de juguetes almacenados entre todos los tipos.
def apend(lista, elemento):
    nueva_lista = [0] * (len(lista) + 1)
    for i in range(len(lista)):
        nueva_lista[i] = lista[i]
    nueva_lista[-1] = elemento
    return nueva_lista

def calcular_total_juguetes(existencias):
    totales = []
    for i in range(len(existencias)):
        total = 0
        for cantidad in existencias[i]:
            total += cantidad
        totales = apend(totales, total)
    return totales

# 3. Obtener los nombres de los juguetes que es necesario reponer en cada depósito.
# Crear una función que devuelva todos los juguetes con menos de 500 unidades.

def reponer_juguetes(existencias):
    para_reponer = []
    for i in range(len(existencias)):
        reponer = []
        for j in range(len(existencias[i])):
            if existencias[i][j] < 500:
                reponer = apend(reponer, tipo_juguete[j])
        para_reponer = apend(para_reponer, reponer)
    return para_reponer