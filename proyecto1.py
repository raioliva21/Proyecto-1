
import random

from time import sleep

# funcion que define caracter (parametro ingresado) depenendiendo de la columna en que se ubica tal caracter 
# 'caracter' puede ser casilla vacia, particula, elemento (letra) o numero indicador de coordenada en pseudomatriz
def definir_caracter(fila, columna, caracter):

    if fila != 0 and columna != 0:
        if columna < 10:
            caracteres = f" {caracter} |"
        else:
            caracteres = f"  {caracter} |"

    #se retorna variable 'caracteres' la cual representa la cadena de caracteres que sera impresa explicitamente en matriz
    return caracteres

# se definde la posicion incial o posicion de ingreso de particula en matriz 
def posicion_incial_particula(cantidad_filas,cantidad_columnas):

    # 'fila' representara la fila en que particula se ubica en pseudmatriz
    fila = random.randrange(1, cantidad_filas)
    # misma caso anterior, esta vez para 'columna' en vez de 'fila'
    columna = random.randrange(1, cantidad_columnas)

    print(fila, columna)

    #se retorna la fila y columna incial de particula en matriz
    return fila, columna

def ingreso_elementos_matriz(cantidad_filas, cantidad_columnas, fila, columna):

    # determinacion de la cantidad de elementos (letras) en base a la cantidad de filas de matriz 
    if cantidad_filas < 7:
        cantidad_elementos = 6
    elif cantidad_filas >= 7 and 12 >= cantidad_filas:
        cantidad_elementos = 12
    else:
        cantidad_elementos = 24

    #lista 'elemento' corresponde a la lista en que se alamacenaran los valores de cada elemento (letra)
    elemento = []
    # lista 'coordenadas_elemento' es ingresada a lista 'elemento' y luego vaciada por cada ciclo transcurrido
    coordenadas_elemento = []
    # 'reevaluar_elemento' determinara si se debe asignar nuevos valores relativos a la posicion del elemento en cuestion
    # tal que posicion de elemento de indice determinado debe distinto a la posicion de particula y elementos ya ingresados
    # si 'reevaluar_elemento' es igual a uno, indice en ciclo 'while' no aumentara, tal que se daran nuevos valores a posicion.
    reevaluar_posicion_elemento = 0
    indice = 0

    #por cada ciclo e indice que aumenta una unidad, se determina la posicion incial de cada elemento (letra) en matriz
    while indice != cantidad_elementos:
        #'coordenadas_elemento' se vacia en cada periodo
        coordenadas_elemento = []
        #se asigna valor pseudoaltearorio de rango = [1,'cantidad_filas')
        fila_elemento = random.randrange(1,cantidad_filas)
        #mismo caso para la columna de determinado elemento
        columna_elemento = random.randrange(1,cantidad_columnas)
        # si punto del elemento es distinto del punto de particula
        # tal que una de las dos variables, sea fila o columna de particula, sea diferente a fila o columna de elemento.
        if fila_elemento != fila or columna != columna_elemento:
            # si indice en ciclo actual es diferente a cero
            # tal que se pueda comparar la posicion de elemento actual con posicion de elementos anteriores ya ingresados en lista
            if indice != 0:
                # 'aux' se ocupa como auxiliar, se emplea del mismo modo en que se usa 'indice'
                # se realiza ciclo hasta comparar posicion de elemento actual con posicion de elemento con indice 'aux' = 0
                for aux in range(indice - 1, -1, -1):
                    # si posicion (fila y columna) de elemento actual es distina a la de los elementos ya ingresados en 'elemento'
                    if fila_elemento != elemento[aux][0] or columna_elemento != elemento[aux][1]:
                        # entonces no se reevalua posicion de elemento actual, tal que se ingresa a lista 'elemento'
                        reevaluar_posicion_elemento = 0
                    # si posicion (fila y columna) de elemento actual es igual a posicin de un elemento ya registrado en lista
                    else:
                        reevaluar_posicion_elemento = 1
                        #se sale de ciclo interno
                        break
                if reevaluar_posicion_elemento == 1:
                    # se vuelve a inicio de ciclo y no se sigue ejecutando las lineas siguientes
                    continue       
            # en caso de que no se tenga que reevaluar posicion de elemento
            # se agrega fila y columna de elemento, en dicho orden, a lista 'coordenadas_elemento'
            coordenadas_elemento.append(fila_elemento)
            coordenadas_elemento.append(columna_elemento)
            # se ingresa la lista recien mencionada, relativa a la posicion de elemento en cuestion, en lista 'elemento'
            elemento.append(coordenadas_elemento)
            # se amuenta valor de indice en una unidad para luego seguir con la determinacion de la posicion de proximo elemento
            indice += 1
        # en caso de que la poscion de elemento en cuestion sea diferente a posicion de la particula
        else:
            continue
    
    # se retorna la matriz bidimensional 'elemento' que contiene la cantidad de elementos totales 
    return elemento, cantidad_elementos



def funcion_letras(indice, matriz, elemento, letras, cantidad_filas, cantidad_columnas, casilla_vacia):
    # se retorna matriz actualizada 
    
    #La letra A es un elemento que permanecer ́a inm ́ovil en la matriz y permitir ́a a la “part ́ıcula” rebotar
    #tal cual lo hace contra una pared

    #letras = ['A','B','E','F','S','A']     len(letras) = 6  :  indices = [0,5]
    #letras = [ 0 , 1 , 2 , 3 , 4 , 5 ]

    # si letra es A
    # particula realiza rebote
    # no se imprime particula en posicion de letra A, pues letra A permanece inmovil
    # se otorga nuevo valor de dirreccion movimiento, dependiente del movimiento de la particula al realizar rebote
    # se rompe ciclo relativo a la direccion de movimiento de particula
    # no se ingresa a funcion movimiento_rebote_particula dentro de funcion movimiento_particula
    # el movimiento rebote de particula ya ha sido dado por letra A

    # como retornar vairable que use para todos los casos

    if letras[indice] == 'A':
        pass

    elif letras[indice] == 'B':
        # en vez de se imprima particula, se imprime 'B' y particula rebota, tal que se debe cerrar ciclo
        #caracter_letra = definir_caracter(elemento[indice][0], elemento[indice][1],letras[indice])
        #matriz[elemento[indice][0]][elemento[indice][1]] = caracter_letra
        #visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz)
        pass
                
    elif letras[indice] == 'E':
        # elemento 'E' se mueve a posicion incial de matriz o posicion final de matriz
        #casilla_vacia_matriz = definir_caracter(elemento[indice][0], elemento[indice][1],casilla_vacia)
        #matriz[elemento[indice][0]][elemento[indice][1]] = casilla_vacia_matriz
        casilla_vacia_matriz = f" {casilla_vacia} |"
        if cantidad_filas > 10:
            casilla_vacia_matriz_aux = f"  {casilla_vacia} |"
        if cantidad_filas <= 10:
            casilla_vacia_matriz_aux = f" {casilla_vacia} |"
        if matriz[1][1] == casilla_vacia_matriz:
            caracter_letra = definir_caracter(elemento[indice][0], elemento[indice][1],letras[indice])
            matriz[1][1] = caracter_letra
        elif matriz[cantidad_filas - 1][cantidad_columnas - 1] == casilla_vacia_matriz_aux:
            lim_max_fila = cantidad_filas - 1 
            lim_max_columna = cantidad_columnas - 1
            caracter_letra = definir_caracter(elemento[indice][lim_max_fila],elemento[indice][lim_max_columna],letras[indice])
            matriz[lim_max_fila][lim_max_columna] = caracter_letra
        else:
            pass
                    
    elif letras[indice] == 'F':
        pass
                    
    elif letras[indice] == 'S':
        #if elemento[indice][0] 
        pass
    else:
        print("Error, ninguna posicion de elemento coincide con posicion de particula") 


#funcion en donde se evalua si particula choca con algun elemento (particula)
def evaluar_choque_con_elementos(fila, columna, elemento, cantidad_elementos):
    for indice in range (0,cantidad_elementos):
        if fila == elemento[indice][0] and columna == elemento[indice][1]:
            choque_particula_con_elemento = 1
            break
        else:
            choque_particula_con_elemento = 0
    
    return indice, choque_particula_con_elemento



def movimiento_particula(fila,columna,cantidad_filas,cantidad_columnas, matriz,limite_matriz,particula,casilla_vacia):

    # se ingresa a funcion que determina la cantidad y posicion de elementos (letras) en matriz
    # se decidio registrar variable relativa a las letras como 'elemento', pues va mas acorde al caso que se intenta recrear
    # cada elemento se identifica con una letra en especifico, que cumple determinada funcion
    elemento, cantidad_elementos = ingreso_elementos_matriz(cantidad_filas, cantidad_columnas, fila, columna)

    # se define de manera arbitraria los elementos contenidos en lista 'letras'
    letras = ['A','B','E','F','S','A']

    # se evalua el tamaño de lista 'letras' en dependencia de la cantidad de elementos determinados en funcion anterior
    if cantidad_elementos == 6:
        letras = letras
    elif cantidad_elementos == 12:
        letras = letras * 2
    else:
        letras = letras * 4

    # en lista bidimensional 'elemento', el subindice = 0 representa la posicion de la fila de la letra determinada
    fila_letra = 0
    # mientras que subindice = 1 representa la posicion de la fila columna de la letra determianda
    columna_letra = 1

    # se ingresa a ciclo en donde se asigna la letra a la posicion respectiva en matriz
    for indice in range(0,len(letras)):
        # se asigna cadena que sera imprimido en matriz
        caracter_letra = definir_caracter(elemento[indice][fila_letra], elemento[indice][columna_letra],letras[indice])
        matriz[elemento[indice][fila_letra]][elemento[indice][columna_letra]] = caracter_letra
    
    # se determina pseudaleatoriamente el movimiento de la particula
    # existen 8 movimientos posibles de particula
    direccion_movimiento = random.randrange(1,9)
    direccion_movimiento = 1
    print("El movimiento de particula es ", direccion_movimiento)

    cantidad_rebotes_particula = int(input("Ingrese cantidad de rebotes que particula realizara\n"))

    for rebotes_particula in range(0, cantidad_rebotes_particula):

        indice = None
        acabar_programa = None

        # si movimoento de particula es en direccion a su esquina superior izquierda
        if direccion_movimiento == 1:
            # recordar que a elementos de indice 0 o subindice 0 de matriz se les asigna caracteres iguales a enteros
            # tales enteros representan el numero de fila o columna de la pseudomatriz
            # coordenada de fila (ciclo) llega hasta limite inferior, valor = 1 (fila 1 y comienzo de filas en pseudomatriz)
            # tal que el 'print' de particula nunca se sobrepondra en los indicadores de fila y columna de pseudomatriz
            for fila in range(fila,limite_matriz, -1):
                # si casilla anterior a casilla actual en orden al movimiento respectivo esta dentro del rango de pseudomatriz
                # tal que se imprima una casilla vacia en la posicion de particula inscrita en ciclo anterior
                if columna != cantidad_columnas - 1 and fila != cantidad_filas - 1:
                    # se define caracteres que seran impresos en matriz
                    indice, choque_con_elementos = evaluar_choque_con_elementos(fila + 1,columna + 1,elemento,cantidad_elementos)
                    if choque_con_elementos == 0:
                        casilla_vacia_matriz = definir_caracter(fila + 1, columna + 1, casilla_vacia)
                        matriz[fila+1][columna+1] = casilla_vacia_matriz
                    else:
                        pass
                # se evalua choque de particula con algun elemento
                indice, choque_con_elementos = evaluar_choque_con_elementos(fila, columna, elemento, cantidad_elementos)
                # si existe choque de particula con algun elemento
                if choque_con_elementos == 1:
                    funcion_letras(indice, matriz, elemento, letras, cantidad_filas, cantidad_columnas, casilla_vacia)
                if choque_con_elementos == 0 or letras[indice] == 'B' or letras[indice] == 'E' or letras[indice] == 'S':
                    particula_matriz = definir_caracter(fila, columna, particula)
                    matriz[fila][columna] = particula_matriz
                    if letras[indice] == 'B' and fila - 1 != limite_matriz and columna - 1 != limite_matriz:
                        caracter_letra = definir_caracter(elemento[indice][0], elemento[indice][1],letras[indice])
                        matriz[elemento[indice][0] - 1][elemento[indice][1] - 1] = caracter_letra
                        visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz)
                        break
                    if letras[indice] != 'B':
                        visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz)
                    # si posicion subsiguiente de particula no iguala limite inferior excluyente ('limite_matriz' = 0)
                    # entonces se procede a siguiente ciclo y, en efecto, particula sigue avanzando en misma direccion
                    if fila - 1 != limite_matriz and columna - 1 != limite_matriz:
                        # se disminuye valor de 'columna' en una unidad, acorde a movimiento respectivo
                        columna -= 1
                    else:
                        #se cierra ciclo, pues particula debio tocar con 'pared'
                        break
                else:
                    # si particula choca con elemento 'F', acaba programa
                    if letras[indice] == 'F':
                        acabar_programa = 1
                        break
                    # si particula choca con elemento 'A', se acaba ciclo para determinar el tipo de rebote a realizar la particula
                    else:
                        break

        # si movimiento de particula es en direccion hacia arriba
        if direccion_movimiento == 2:
            # inicia ciclo, cuya variable itinerable acaba a llegar a fila inicial de matriz (indice = 1)
            for fila in range(fila,limite_matriz, -1):
                # si casilla anterior a casilla actual en orden al movimiento respectivo esta dentro del rango de pseudomatriz
                # tal que se imprima una casilla vacia en la posicion de matriz que estaba la particula(inscrita en ciclo anterior)
                if fila != cantidad_filas - 1:
                    # se define caracteres que seran impresos en matriz
                    casilla_vacia_matriz = definir_caracter(fila + 1, columna, casilla_vacia)
                    matriz[fila+1][columna] = casilla_vacia_matriz
                particula_matriz = definir_caracter(fila, columna, particula)
                matriz[fila][columna] = particula_matriz
                #se imprime matriz
                visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz)

        # si movimiento de particula es en direccion a su esquina derecha superior
        if direccion_movimiento == 3:
            for fila in range(fila,limite_matriz, -1):
                # si casilla anterior a casilla actual en orden al movimiento respectivo esta dentro del rango de pseudomatriz
                # tal que se imprima una casilla vacia en la posicion de matriz que estaba la particula(inscrita en ciclo anterior)
                if fila != cantidad_filas - 1 and columna != limite_matriz + 1:
                    # se define caracteres que seran impresos en matriz
                    casilla_vacia_matriz = definir_caracter(fila + 1, columna - 1, casilla_vacia)
                    matriz[fila+1][columna-1] = casilla_vacia_matriz
                particula_matriz = definir_caracter(fila, columna, particula)
                matriz[fila][columna] = particula_matriz
                # se imprime matriz
                visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz)
                # si la variable columna no ha alcanzado limite superior de matriz
                if fila - 1 != limite_matriz and columna + 1 != cantidad_columnas:
                    # se disminuye en una unidad variable columna, en concordancia con movimiento respectivo 
                    columna += 1
                # si la variable columna ha alcanzado limite superior de matriz
                else:
                    #se cierra ciclo
                    break
        
        # si movimiento de particula es hacia la izquierda
        if direccion_movimiento == 4:
            # ingreso a ciclo, que acaba cuando se llega a primera columna de pseudomatriz (limite inferior de columna)
            for columna in range(columna,limite_matriz, -1):   
                # si casilla anterior a casilla actual en orden al movimiento respectivo esta dentro del rango de pseudomatriz
                # tal que se imprima una casilla vacia en la posicion de matriz que estaba la particula(inscrita en ciclo anterior)
                if columna != cantidad_columnas - 1:
                    # se define caracteres que seran impresos en matriz
                    casilla_vacia_matriz = definir_caracter(fila, columna + 1, casilla_vacia)
                    matriz[fila][columna + 1] = casilla_vacia_matriz
                particula_matriz = definir_caracter(fila, columna, particula)
                matriz[fila][columna] = particula_matriz
                # se imprime matriz
                visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz)

        # si movimiento de particula es hacia la derecha
        if direccion_movimiento == 5:
            # ingreso a ciclo, que acaba cuando se llega a ultima columna de pseudomatriz (limite superior de columna)
            for columna in range(columna,cantidad_columnas):
                # si casilla anterior a casilla actual en orden al movimiento respectivo esta dentro del rango de pseudomatriz
                # tal que se imprima una casilla vacia en la posicion de matriz que estaba la particula(inscrita en ciclo anterior)
                if columna != limite_matriz + 1:
                    # se define caracteres que seran impresos en matriz
                    casilla_vacia_matriz = definir_caracter(fila, columna - 1, casilla_vacia)
                    matriz[fila][columna - 1] = casilla_vacia_matriz
                particula_matriz = definir_caracter(fila, columna, particula)
                matriz[fila][columna] = particula_matriz
                visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz)

        # si movimiento de particula es en direccion a su esquina inferior izquierda
        if direccion_movimiento == 6:
            # ingreso a ciclo, el cual acaba cuando se alcanza el numero de fila maximo permitido en psuedomatriz
            for fila in range(fila,cantidad_filas):
                # si casilla anterior a casilla actual en orden al movimiento respectivo esta dentro del rango de pseudomatriz
                # tal que se imprima una casilla vacia en la posicion de matriz que estaba la particula(inscrita en ciclo anterior)
                if fila != limite_matriz + 1 and columna != cantidad_columnas - 1:
                    casilla_vacia_matriz = definir_caracter(fila - 1, columna + 1, casilla_vacia)
                    matriz[fila-1][columna+1] = casilla_vacia_matriz
                particula_matriz = definir_caracter(fila, columna, particula)
                matriz[fila][columna] = particula_matriz
                visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz)
                if fila + 1 != cantidad_filas and columna - 1 != limite_matriz:
                    columna -= 1
                else:
                    break
        
        # si movimiento de particula es hacia abajo
        if direccion_movimiento == 7:
            for fila in range(fila,cantidad_filas):
                # si casilla anterior a casilla actual en orden al movimiento respectivo esta dentro del rango de pseudomatriz
                # tal que se imprima una casilla vacia en la posicion de matriz que estaba la particula(inscrita en ciclo anterior)
                if fila != limite_matriz + 1:
                    casilla_vacia_matriz = definir_caracter(fila - 1, columna, casilla_vacia)
                    matriz[fila-1][columna] = casilla_vacia_matriz
                particula_matriz = definir_caracter(fila, columna, particula)
                matriz[fila][columna] = particula_matriz
                visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz)
        
        # si movimiento de particula es en direccion a su esquina inferior derecha
        if direccion_movimiento == 8:
            for fila in range(fila,cantidad_filas):
                # si casilla anterior a casilla actual en orden al movimiento respectivo esta dentro del rango de pseudomatriz
                # tal que se imprima una casilla vacia en la posicion de matriz que estaba la particula(inscrita en ciclo anterior)
                if fila != limite_matriz + 1 and columna != limite_matriz + 1:
                    casilla_vacia_matriz = definir_caracter(fila - 1, columna - 1, casilla_vacia)
                    matriz[fila-1][columna-1] = casilla_vacia_matriz
                particula_matriz = definir_caracter(fila, columna, particula)
                matriz[fila][columna] = particula_matriz
                visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz)
                # si posicion siguiente de particula no iguala limites maximos excluyentes ('cantidad_filas' y 'cantidad_columnas')
                # entonces se procede a siguiente ciclo y, en efecto, particula sigue avanzando en misma direccion
                if fila + 1 != cantidad_filas and columna + 1 != cantidad_columnas:
                    # se aumnenta valor de 'columna' en una unidad, acorde a movimiento respectivo
                    columna += 1
                # si fila y/0 columna de particula es siguiente ciclo sobrepasa limite(s) de pseudamatriz
                else:
                    # se cierra ciclo, pues particula alcanzo "pared" de pseudomatriz 
                    break
        print(fila, columna)

        if acabar_programa == 1:
            print("Particula ha reaccionado con elemento 'F'; energia ha sido incontenible por sistema y ha colapsado.")
            break
        else:
            # para que caracteres en linea no se extienda bastante, se registra el movimiento de particula con nombre corto 'dm'
            dm = direccion_movimiento
            direccion_movimiento = direccion_rebote_particula(dm,fila,cantidad_filas,columna,cantidad_columnas,limite_matriz) 


# funcion que define el movimiento que realiza particula al rebotar en paredes (o letra A)
def direccion_rebote_particula(direccion_movimiento,fila,cantidad_filas,columna,cantidad_columnas,limite_matriz):
   

    # se crean listas relacionadas a los posibles 3 movimientos dependientes de la posicion de la particula al rebotar

    # particula puede moverse hacia esquina superior izquierda, arriba o izquierda
    movimiento_rebote_esquina_inf_der = [1,2,4]
    # particula puede moverse hacia esquina superior izquieda, izquierda o esquina inferior izquierda
    movimiento_rebote_columna_der = [1,4,6]
    # particula puede moverse hacia izquerda, esquina inferior izquierda o abajo
    movimiento_rebote_esquina_sup_der = [4,6,7]
    # particula puede moverse hacia esquina inferior izquierda, abajo o esquina inferior derecha
    movimiento_rebote_fila_sup = [6,7,8]
    # particula puede moverse hacia esquina superior izquierda, arriba o esquina superior derecha
    movimiento_rebote_fila_inf = [1,2,3]
    # particula puede moverse hacia arriba, esquina superior derecha o derecha
    movimiento_rebote_esquina_inf_izq = [2,3,5]
    # particula puede moverse hacia esquina superior derecha, derecha o equina inferior derecha
    movimiento_rebote_columna_izq = [3,5,8]
    # particula puede moverse hacia derecha, abajo o esquina inferior derecha
    movimiento_rebote_esquina_sup_izq = [5,7,8]
        
    # se determina valor pseudoaleatorio de rango = [0,3)
    movimiento_rebote = random.randrange(0,3)

    # si particula toca pared inferior de pseudomatriz
    if fila == cantidad_filas - 1:
    # si particula toca en esquina inferior izquierda, tal que posicion de particula es ultima fila con ultima columna
        if columna == cantidad_columnas - 1:
            # se asigna uno de los tres posibles movimentos respectivos al caso, dependientes de 'movimiento_rebote'
            direccion_movimiento = movimiento_rebote_esquina_inf_der[movimiento_rebote]
        # si particula toca en esquina inferior izquierda, tal que posicion de particula es ultima fila y 1ra columna
        elif columna == limite_matriz + 1:
            direccion_movimiento = movimiento_rebote_esquina_inf_izq[movimiento_rebote]
        # si particula no toca en ningua esquina
        else:
            direccion_movimiento = movimiento_rebote_fila_inf[movimiento_rebote]

    # si particula toca pared superior de pseudomatriz
    elif fila == limite_matriz + 1:
        # si particula toca en esquina superior izquierda, tal que posicion de particula es 1ra fila con ultima columna
        if columna == cantidad_columnas - 1:
            direccion_movimiento = movimiento_rebote_esquina_sup_der[movimiento_rebote]
        # si particula toca en esquina superior derecha, tal que posicion de particula es 1ra fila y columna
        elif columna == limite_matriz + 1:
            direccion_movimiento = movimiento_rebote_esquina_sup_izq[movimiento_rebote]
        # si particula no toca en ningua esquina
        else:
            direccion_movimiento = movimiento_rebote_fila_sup[movimiento_rebote]

    # si particula toca en pared izquierda, pero no en esquina
    elif columna == limite_matriz + 1:
        direccion_movimiento = movimiento_rebote_columna_izq[movimiento_rebote]
    # si particula toca en pared derecha, pero no en esquina
    elif columna == cantidad_columnas - 1:
        direccion_movimiento = movimiento_rebote_columna_der[movimiento_rebote]

    else:
        if direccion_movimiento == 1:
            direccion_movimiento = movimiento_rebote_esquina_sup_izq[movimiento_rebote]
        elif direccion_movimiento == 2:
            direccion_movimiento = movimiento_rebote_fila_sup[movimiento_rebote]
        elif direccion_movimiento == 3:
            direccion_movimiento = movimiento_rebote_esquina_sup_der[movimiento_rebote]
        elif direccion_movimiento == 4:
            direccion_movimiento = movimiento_rebote_columna_izq[movimiento_rebote]
        elif direccion_movimiento == 5:
            direccion_movimiento = movimiento_rebote_columna_der[movimiento_rebote]
        elif direccion_movimiento == 6:
            direccion_movimiento = movimiento_rebote_esquina_inf_izq[movimiento_rebote]
        elif direccion_movimiento == 7:
            direccion_movimiento = movimiento_rebote_fila_inf[movimiento_rebote]
        else:
            direccion_movimiento = movimiento_rebote_esquina_inf_der[movimiento_rebote]

    # se retorna valor de 'direccion_movimiento' (movimiento de particula) resultante
    return direccion_movimiento 


# se crea matriz 
def creacion_matriz(filas, columnas, cantidad_filas, cantidad_columnas):

    # se ingresa a sentencia 'for', donde se crea matriz incial en donde se movera particula posteriormente
    # variable 'indice' se relaciona a la fila en matriz
    for indice in range (0,cantidad_filas):
        #lista columna se blanquea por cada ciclo interno cumplido
        columnas = []
        # se entra a ciclo referente a columnas en determinada fila(indice)
        for subindice in range (0, cantidad_columnas):
            # si se esta en fila 1 (indice = 0)
            if indice == 0:
                # si se esta en columna 1 (subindice = 0)
                # punto (0,0) en matriz
                if subindice == 0:
                    casilla = "      "
                # si se esta en columna mayor a 1 (subindice != 0)
                # ej: punto(0,2)
                else:
                    casilla = f"{subindice}   "
            # si se esta en fila mayor a 1 (indice != 0)
            else:
                # se evalua valor de subindice
                # puesto que al imprimir un numero de dos digitos en 1ra fila con columna mayor o igual a 10
                # se agrega un digito mas que en los casos anteriores (numeros relativos a indicadores de columna < 10)
                # para evitrar desfases producto de el caracter añadido (digito) -
                # se agrega un espacio a todas las columnas en posicion menor a 10 (subindice 9)
                if subindice == 0:
                    if indice < 10:
                        casilla = f"  {indice} |"
                    else:
                        casilla = f" {indice} |"
                # si se esta en columna mayor a 1 (subindice != 0)
                #ej: punto(4,5)
                else:
                    if subindice < 10:
                        casilla = "   |"
                    else:
                     casilla = "    |"
            #se agrega casilla a lista 'columnas' 
            columnas.append(casilla)
        #cerrado ciclo interno (relativo de columnas), se agrega lista 'columnas' dentro de lista 'filas'
        filas.append(columnas)

    #se retorna lista 'filas'
    #en funciona principal, el valor retornado sera asignado a variable 'matriz', teniendo la base de la matriz ya creada
    return filas

# funcion en donde se imprime matriz 
def visualizacion_matriz(cantidad_filas,cantidad_columnas, matriz):

    for indice in range(0, cantidad_filas):
        print("\n")
        for subindice in range(0, cantidad_columnas):
            print(matriz[indice][subindice], end="")         
    print("\n")
    # se enlentece la ejecucion de lineas para una mayor apreciacion del movimiento de particula
    sleep(1)

#funcion principal donde se visualiza el orden de ejecucion de programa
def main():

    # se crean listas 'filas' y 'columnas', relativa a las filas y columnas de matriz eventualmente impresa
    # ambas listas son vacias; los elementos son agregados porsteriormente en funcion 'creacion_matriz'
    filas = []
    columnas = []
    #se asigna valor pseudoaleatorio a la cantidad de filas en matriz('cantidad_filas'), el rango es arbitrario entre 4 a 20 filas
    cantidad_filas = random.randrange(4,20)
    cantidad_filas = 10
    #por indicaciones predeterminadas, la cantidad de filas sera igual a la cantida de columnas, tal que matriz sea cuadrada
    #si se desea, se puede modificar esta parte de codigo asignando valor diferente a 'cantidad_columnas'; debiese ejecutar bien
    cantidad_columnas = cantidad_filas
    # se tendra la matriz real y una pseudomatriz
    # la pseudomatriz sera la matriz aparente al imprimir el movimiento de la particula dentro de esta misma
    # los limites inferiores y excluyentes de la psudomatriz seran las columnas y filas de indice cero en matriz real
    # la posicion de la particula nunca sera igual al limite inferior de la matriz (limite_inf_matriz)
    # pues en las columnas y filas de indice 0 en la matriz real se imprimen los numeros indicadores de las filas y columnas-
    # de la pseudomatriz (donde la particula se mueve)
    limite_inf_matriz = 0
    # se asigna caracter a la particula ('particula'), caracter que sera impreso en la matriz
    particula = 'o'
    # 'casilla_vacia' refiere a las casillas o posiciones de la matriz que no son ocupadas por las letras o particulas
    casilla_vacia = ' '
    #se ingresa a funcion que crea matriz, asignandose valor de retorno a 'matriz'
    matriz = creacion_matriz(filas, columnas, cantidad_filas, cantidad_columnas)
    fila, columna = posicion_incial_particula(cantidad_filas,cantidad_columnas)
    # funcion de mayor contenido en donde se determinada el movimiento pseudoaletario de particula y letras (dependiendo del caso)
    movimiento_particula(fila,columna,cantidad_filas,cantidad_columnas,matriz,limite_inf_matriz,particula,casilla_vacia)

if "__main__" == __name__:
    main()