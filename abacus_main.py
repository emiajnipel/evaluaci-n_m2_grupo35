#abacus_main.py
'''
Llama a las funciones de Abacus en base a lo ingresado por el usuario:
* createAbacus: Crea un diccionario con el valor entregado por el usuario
* print_emptyAbacus: imprime el abaco sin piezas
* print_fullAbacus: imprime el abaco con las piezas correspondientes al numero ingresado por usuario

Variables:
exit: 0 hasta que el usuario decida salir
intento: lista que guarda los intentos del usuario
user_input: n° ingresado por usuario
numero: almacena la versión int del input del usuario
userAbacus: abaco generado con la funcion createAbacus
'''

#import de funciones creadas para el juego
import abacusFx as fx

#Inicialización de variables
exit=0
intento=[]

#Mientras el usuario no indique finalizar el juego
while(exit==0):

    # Verificar si lo ingresado por el usuario es un valor válido [0...9]+'exit
    try:
    
        # Usuario ingresa numero por consola
        user_input=input('Ingrese un n° entero entre 0 y 999999, o exit para dejar de jugar\n')
        
        #Si el usuario indica exit, salir del juego
        if user_input=='exit':
            break
        else:
            #transformar input a int
            numero=int(user_input)

            if numero ==0:
                #Si el numero es 0, genera un abaco vacío
                userAbacus=fx.createAbacus(user_input)
                #Imprime abaco generado
                print(f"El abaco es {userAbacus}\n")
                #Imprime abaco vacío
                fx.print_emptyAbacus()
                #Guarda intento en lista
                intento.append(numero)
                
            elif numero>0 and numero<1000000:
                #Si el numero está entre 1 y 999.999,genera un abaco con piezas
                userAbacus=fx.createAbacus(user_input)
                #imprime el abaco generado
                print(f"El abaco es {userAbacus}\n")
                #Imprime abaco con piezas
                fx.print_fullAbacus(userAbacus)
                #Guarda intento en lista
                intento.append(numero)

            else: 
                # Si el n° se sale del rango
                print(f"N° no válido")

    except ValueError:
        #Si el valor ingresado por el usuario no es válido
        print(f"Valor no válido")

#Si el usuario elige la opción exit, imprime los intentos
print('Intentos realizados\n')
for f in intento:
    print('{:,}'.format(f).replace(",", "."))