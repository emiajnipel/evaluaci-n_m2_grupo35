#Función transforma input usuario a abaco
def createAbacus(user_number):
    '''
    Funcion createAbacus: crea diccionario con datos ingresados por el usuario
    Variables:
        user_number: numero ingresado por el usuario
        number: string que es llenado con 0 si sus digitos son menos que 6
        abacus: diccionario
    Return abacus: diccionario
    '''
    #Si el largo del numero es menor a 6 dígitos
    if len(user_number)<6:
        #Llenar los digitos faltantes con 0 a la izquierda
        number='0'*(6-len(user_number))+user_number
    else:
        number=user_number
    
    #Crea diccionario
    abacus={'cmil':int(number[0]),
           'dmil':int(number[1]),
           'mil':int(number[2]),
           'centena':int(number[3]),
           'decena':int(number[4]),
           'unidad':int(number[5])}
           
    #Retorna el diccionario generado
    return abacus 
    
    
def print_emptyAbacus():
    '''
    Funcion print_emptyAbacus: grafica un abaco vacío
    Variables:
        ispace,hbAbacus,emptyRod,rod,hb_line,empty_line,unity_line: caracteres para crear abaco
    '''

    # Espacio entre varillas
    ispace='   '
    # sección superior e inferior de la varilla
    hbAbacus=' +-+ '
    # Varilla vacía
    emptyRod=' | | '
    # Cuentas
    rod='XXXXX'

    # linea superior e inferior de varillas
    hb_line=ispace+(hbAbacus+ispace)*6
    # linea con varillas vacías
    empty_line=ispace+(emptyRod+ispace)*6
    # Línea con unidades de medida del abaco
    unity_line=' '+'100.000'+ispace+'10.000'+ispace+'1.000'+ispace+'100'+ispace*2+'10'+ispace*2+'0'+ispace

    #Imprime un abaco vacío
    print(hb_line+'\n'+(empty_line+'\n')*10+hb_line)
    print(unity_line)
    
    
def print_fullAbacus(user_Abacus):
    '''
    Funcion print_fullAbacus: grafica un abaco con el numero entregado por usuario
    Variables:
        ispace,hbAbacus,emptyRod,rod,hb_line,empty_line,unity_line: caracteres para crear abaco
        lineList: lista que almacenará cada linea del abaco (10)
        tempLine: almacena la linea que se está generando de manera temporal       
    '''
    #-----------------VARIABLES CON TEXTOS PARA GRAFICAR EL ABACO ------------------------------------#
    # Espacio entre varillas
    ispace='   '
    # sección superior e inferior de la varilla
    hbAbacus=' +-+ '
    # Varilla vacía
    emptyRod=' | | '
    # Cuentas
    rod='XXXXX'
    # linea superior e inferior de varillas
    hb_line=ispace+(hbAbacus+ispace)*6
    # linea con varillas vacías
    empty_line=ispace+(emptyRod+ispace)*6
    # Línea con unidades de medida del abaco
    unity_line=' '+'100.000'+ispace+'10.000'+ispace+'1.000'+ispace+'100'+ispace*2+'10'+ispace*2+'0'+ispace


    #------------------------------CODIGO GENERADOR DEL ABACO-----------------------------------------#

    #Lista con las lineas a imprimir
    lineList=[]

    for lines in range(1,11):
        #Crear una linea vacía
        tempLine=''
        #Por cada elemento del abaco
        for v in user_Abacus.values():
            # Si el n° a graficar aun no completa sus piezas 
            if lines <= v:
                #añade pieza
                tempLine=tempLine+ispace+rod
            else:
                #imprime varilla
                tempLine=tempLine+ispace+emptyRod
                
        #Añade linea al abaco graficado
        lineList.append(tempLine)
    
    #revierte el orden de las lineas
    lineList=list(reversed(lineList))

    #Imprime el abaco
    print(hb_line)   
    
    for l in lineList:
        print(l)  
    
    print(hb_line)  
    print(unity_line+'\n')
    
    #imprime el diccionario que contiene los valores ingresados por el usuario
    for k,v in user_Abacus.items():
        print(f'{k}: {v}')