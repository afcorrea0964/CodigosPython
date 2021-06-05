import math  #Importamos la librería math#
def sin(x,n): #Definimos la función seno#

    sine=0 #Tomamos un argumento (x = número) y devuelve su seno en radianes.#

    for i in range(n): #Para un valor de  i definimos un valor de n#
        sign=math.pow(-1,i)
        pi=math.pi #Usamos este comando que  representa la relacion entre la longitud de la circunferencia de un circulo y su diametro.
        a=x*(pi/180) #Convertimos de radianes a grados#
        sine=sine+(sign*(a**(2.0*i+1))/math.factorial(2*i+1))#Colocamos la formula de la serie de Taylor#
        print(sine) #Imprimimos en lista los resultados hasta que nos salga el valor de n#

        # Le indicamos al programa las opciones para que el usuario ingrese#
    return sine
x=float(input('Ingrese el angulo que desee calcular: ' ))
n=int(input('Ingrese el numero de terminos: '))

print(sin(x,n)) #Finalmente imprimimos el código#



