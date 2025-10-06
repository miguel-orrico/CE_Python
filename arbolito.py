#Realiza un programa que calcule las raíces de un polinomio de 2º grado. 
#Nota: un polinomio de 2º grado es de la siguiente: 
#ax2 + bx + c = 0. 
#y su formula
# 
# 
# 

a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))

coeficientes = (a, b, c)

discriminante = coeficientes[1]**2 - 4*coeficientes[0]*coeficientes[2]
if discriminante < 0:
    print("No existen raices reales")
elif discriminante == 0: