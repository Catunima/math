#texto titulo
#hola nose y ya
import math

print("welcome")
menu = ""#variable para datos
print("selecciona una option")
print ("1. Newton Raphson")
print("2. Integration under the curve")
print("3. Integration by Trapecio")

option = input("Selecciona una opcion > ")#recibir datos

if option == "1":
    print("=======Newton Raphson========")
    print("y =1/2(x^2)(sin(x)+1)")
    intervalo_inicial = 1
    print("ecuacion tal")
    #fuccion
if option == "2": #Opcion para trabajar con integración bajo la curva
    print("===========Integration under the curve======")
    print("y = 1/2(x^2)(sin(x)+1) de 1 a 5")
    intervalo = 1#variable para el inicio del intervalo
    intervalo_anterior = 0 #variable para el anterior
    x_med = 0.0
    function = 0.0
    area = 0.0
    intervalo_anterior = intervalo
    x = 0 #variable de x para la función
    intervalo = intervalo + 0.4
    x_med = (intervalo+intervalo_anterior)/2
    function = 1/2 * (intervalo)*(math.sin(intervalo)+1)
    area =0.4*function

    print("x     |x(med)     |f(x)        |Area   ")
    print("{}   |{}          |{}|{}      ".format(intervalo, x_med,function,area))

if option == "3":
    print("======Integration by Trapecio======")
    print("ecuacion tal")
