import funciones

deposito = ['PBA', 'CABA', 'Chubut', 'Tucuman', 'Mendoza']
tipo_juguete = ['autos', 'muñecas', 'trenes', 'peluches', 'spinners', 'cartas']
existencias = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

# 1
existencias_prueba = funciones.cargar_existencias(existencias)

# 2
total_juguetes_prueba = funciones.calcular_total_juguetes(existencias)
print('total de juguetes por depósito:', total_juguetes_prueba)

# 3
reponer_prueba = funciones.reponer_juguetes(existencias)
print('juguetes para reponer en cada depósito:', reponer_prueba)
