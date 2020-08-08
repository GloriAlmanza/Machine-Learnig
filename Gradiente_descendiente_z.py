import matplotlib.pyplot as plt
from numpy.random import randint
from numpy import linspace

x_inicial = randint(10)
y_inicial = randint(10)

alpha = 0.1
n_iteraciones = 100
tolerancia = 0.00000001

iteraciones = []
z = []

x = x_inicial
y = y_inicial

for i in range(n_iteraciones):
	print('----------------------------------------------------------')
	print('iteración ', str(i+1))

	# Calcular gradiente
	gradiente = 2*x + 2*y

	# Actualizar "x" usando gradiente descendente
	x = x - alpha*gradiente
	y = y - alpha*gradiente

	# Almacenar iteración y valor correspondiente
	z.append(x**2 + y**2)
	iteraciones.append(i+1)

	if (i == 0):
		error = abs((x_inicial**2 + y_inicial**2) - (x**2 + y**2))
	else:
		error = abs(z[i] - z[i-1])

	if (error >= tolerancia):
		# Imprimir resultados
		print('x = ', str(x), ', y = ', str(y), ', z = ', str(z[i]), ', error = ', str(error))
	else:
		print('x = ', str(x), ', y = ', str(y), ', z = ', str(z[i]), ', error = ', str(error))
		print('Dentro del rango de tolerancia')
		break