#Podemos declarar algunas variables para el uso de expresiones matemáticas y polinomios #
#usando sympy. método de símbolos ().#

from sympy.plotting import plot
from sympy import Symbol #Importamos Symb

x= Symbol('x')

#A continuación ingresamos las 2 funciones, Seguido del titulo, y las leyendas#
graph= plot(x**2-x+1, (2/(x-1)), (x,-15,15), title="Grafico", legend= True, xlabel='x', ylabel='f(x)', show=False)

# A continuación asignamos el color a cada grafica#
graph[0].line_color= 'b'
graph[1].line_color='g'

# Finalmente Imprimimos y mostramos  nuestro código#
graph.save('Multiple-functions.png')
graph.show()