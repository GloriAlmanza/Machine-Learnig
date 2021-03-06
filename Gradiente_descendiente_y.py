import matplotlib.pyplot as plt
from numpy.random import randint
from numpy import linspace

x_inicial = randint(10)
alpha = 0.1
n_iteraciones = 100
tolerancia = 0.00000001

iteraciones = []
y = []

x = x_inicial
for i in range(n_iteraciones):
	print('----------------------------------------------------------')
	print('iteración ', str(i+1))

	# Calcular gradiente
	gradiente = 2*x

	# Actualizar "x" usando gradiente descendente
	x = x - alpha*gradiente

	# Almacenar iteración y valor correspondiente
	y.append(x**2)
	iteraciones.append(i+1)

	if (i == 0):
		error = abs(x_inicial**2 - x**2)
	else:
		error = abs(y[i] - y[i-1])

	if (error >= tolerancia):
		# Imprimir resultados
		print('x = ', str(x), ', y = ', str(x**2), ', error = ', str(error))
	else:
		print('x = ', str(x), ', y = ', str(x ** 2), ', error = ', str(error))
		print('Dentro del rango de tolerancia')
		break

plt.subplot(1,2,1)
plt.plot(iteraciones,y)
plt.xlabel('Iteración')
plt.ylabel('y')

X = linspace(-5,5,100)
Y = X**2
plt.subplot(1,2,2)
plt.plot(X,Y,0.0,0.0,'ro')
plt.xlabel('x')
plt.ylabel('y')

plt.show()