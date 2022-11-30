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
        print("y =cos(x)-x**3")
        print("x(n+1)     |x(n)      |f(x_n)     |f'(x_n)     |error")
        valorInicial = 0
        fx_ev = 1
        while fx_ev > 0 and fx_ev  :
            valor_nearzero  = valorInicial
            fx_ev = math.cos(valorInicial) - valorInicial**3
            valorInicial += 0.05

        valorInicial = valor_nearzero #valor incial de x que se usara dentro de la funcion
        equis = valorInicial # valor de x para pruebas, funcion PENDIENTEEE*
        fx = math.cos(equis) - equis**3 #funcion fx
        f_prime_x = -math.sin(equis)-3*(equis**2)  # funcion derivda fx
        epsilon = 1.8*(10**-10) # comparador de error
        count = 0 # counter de veces que se hace
        nr_inicial = equis-(fx/f_prime_x) #Newton-Rapson
        error = abs((nr_inicial-equis)/nr_inicial) #calculo del error en ese intervalo
        print("{} |{}       |{} |{} |{}      ".format(round(nr_inicial,8), valorInicial, round(fx,8), round(f_prime_x,8),round(error,8)))



        while error > epsilon:
            new_x = nr_inicial #los valores de NR seran evaluados en la función
            fx = math.cos(new_x) - new_x**3 #funcion fx con nueva x
            f_prime_x = -math.sin(new_x)-3*(new_x**2)  # funcion derivada fx con nueva x
            nr_inicial = new_x-(fx/f_prime_x)
            error = abs((nr_inicial-new_x)/nr_inicial)
            print("{} |{}|{}|{}   |{}      ".format(round(nr_inicial,8), round(new_x,8), round(fx,8), round(f_prime_x,8),round(error,15)))
   
    
        #fuccion
    if option == "2": #Opcion para trabajar con integración bajo la curva
        print("===========Integration under the curve======")
        print("y = 1/2(x^2)(sin(x)+1) de 1 a 5")
        print()
        print("x     |x(med)     |f(x)        |Area   ")
        intervalo = 0#variable para el inicio del intervalo
        intervalo_anterior = 0 #variable para el anterior
        x_med = 0.0
        function = 0.0
        area = 0.0
        result = 0.0
        x = 0 #variable de x para la función
        
        while intervalo != 5:
            intervalo_anterior = intervalo
            intervalo = intervalo + 0.25
            intervalo = round(intervalo, 2)
            x_med = (intervalo+intervalo_anterior)/2
            x_med = round(x_med,3)
            intervalo_elevado = x_med**2
            #function = (1/2) * (((intervalo_elevado))*(math.sin(x_med)+1))
            function = (math.cos(x_med))/(intervalo_elevado+1)
            function = round(function,8)
            area =0.25*function
            result = result +area
            print("{}   |{}        |{}|{}      ".format(intervalo, x_med,function,area))
        print("                             |{}".format(result))
    if option == "3":
        print("======Integration by Trapecio======")
        print("y = 1/2(x^2)(sin(x)+1) de 1 a 5")
        print()
        print("x     ||f(x)        |Area   ")
        intervalo = 0#variable para el inicio del intervalo
        intervalo_anterior = 0 #variable para el anterior
        #function = 0.92073549
        function = 0
        area = 0.0
        result = 0.0
        x = 0 #variable de x para la función
        intervalo_elevado = intervalo**2
        function = (math.cos(intervalo))/(intervalo_elevado+1)
        print("{}   |{}|{}      ".format(intervalo,function,area))
        while intervalo != 5:
            intervalo_anterior = intervalo
            intervalo = intervalo + 0.25
            intervalo = round(intervalo, 2)
            intervalo_elevado = intervalo**2
            function_anterior = function
            #function = (1/2) * (((intervalo_elevado))*(math.sin(intervalo)+1))
            
            function = (math.cos(intervalo))/(intervalo_elevado+1)
            
            #function = round(function,8)
            area =(0.25*(function+function_anterior))/2
            result = result +area
            print("{}   |{}|{}      ".format(intervalo,function,area))
        print("                  |{}".format(result))

print("Gracias por utilizar nuestro software etc. Michi, richi, Tulio, Alexis y edu.")