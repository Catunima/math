#texto titulo
#hola nose y ya
import math

print("welcome")
menu = ""#variable para datos


option = ""
while option != "4":
    print("selecciona una option")
    print ("1. Newton Raphson")
    print("2. Integration under the curve")
    print("3. Integration by Trapecio")
    print("4. Exit")
    option = input("Selecciona una opcion > ")#recibir datos
    if option == "1":
        print("=======Newton Raphson========")
        print("y =1/2(x^2)(sin(x)+1)")
        print("x(n+1)     |x(n)     |f(x_n)        |f'(x_n)    ")
        valorInicial = 0.5
        equis = 0
        fx = math.cos(equis) - equis**3
        f_prime_x = math.sin(equis) -3*equis**2
        epsilon = 1.8*(10**-10)
        count = 0
        NR_inicial = equis-(fx/f_prime_x)
        error = (NR_inicial-equis)/NR_inicial
        


            




        #fuccion
    if option == "2": #Opcion para trabajar con integración bajo la curva
        print("===========Integration under the curve======")
        print("y = 1/2(x^2)(sin(x)+1) de 1 a 5")
        print()
        print("x     |x(med)     |f(x)        |Area   ")
        intervalo = 1#variable para el inicio del intervalo
        intervalo_anterior = 0 #variable para el anterior
        x_med = 0.0
        function = 0.0
        area = 0.0
        result = 0.0
        x = 0 #variable de x para la función
        
        while intervalo != 5:
            intervalo_anterior = intervalo
            intervalo = intervalo + 0.4
            intervalo = round(intervalo, 1)
            x_med = (intervalo+intervalo_anterior)/2
            x_med = round(x_med,3)
            intervalo_elevado = x_med**2
            function = (1/2) * (((intervalo_elevado))*(math.sin(x_med)+1))
            #function = (math.cos(x_med))/(intervalo_elevado+1)
            function = round(function,8)
            area =0.4*function
            result = result +area
            print("{}   |{}        |{}|{}      ".format(intervalo, x_med,function,area))
        print("                             |{}".format(result))
    if option == "3":
        print("======Integration by Trapecio======")
        print("ecuacion tal")
