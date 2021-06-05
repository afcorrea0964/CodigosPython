import numpy   #Usamos la libreria Numpy  la cual nos permite una serie de operaciones matematicas en#
#este caso con matrices#


x=numpy.array([[1,2], [3,4]])  #Aquí damos la forma de la matriz, que es una lista de números enteros#
 # que dan el tamaño de la matriz a lo largo de cada dimensión#


y=numpy.linalg.inv(x) #Este comando nos permite calcular la inversa de la matriz#

# Por ultimo imprimimos los resultados #

print(x)

print (y)