"""
*********************************************************************************************
*                                                                                           *
*                                   NOTA IMPORTANTE                                         *
*   Me disculpo por la forma de mi presentación, solo espero que mi script sea evaluado     *
*   y de ser posible considerado para la resolución del problema.                           *
*                                                                                           *
*********************************************************************************************
Sample Input 1
5 3
4 3
5 5
4 2
2 3
Sample Output 1 ====   10

Explanation 1::: The queen is standing at position (4, 3) on a 5x5 chessboard with k = 3 obstacles:
The number of squares she can attack from that position is 10.
"""
posiciones=0
listaVertical=[]
listaHorizontal=[]
diagonalIzqDer=[]
diagonalDerIzq=[]
def queensAttack(n, k, rq, cq, obstacles):
    """print("ENTRADA::")
    print(n, k, rq, cq, obstacles)
    print("obstaculos::")
    print(obstacles) """
    global posiciones
    for i in range(0,len(obstacles),2):
        if obstacles[i]==rq:
            tuplaObs=(obstacles[i],obstacles[i+1])
            if listaHorizontal:
                for i in listaHorizontal:
                    if i == tuplaObs:
                        break
                    else:
                        posiciones=posiciones+1
            else:
                buscarHorizontal(n,rq,cq,tuplaObs)
        elif obstacles[i+1]==cq:
            tuplaObs=(obstacles[i],obstacles[i+1])
            if listaVertical:
                for i in listaVertical:
                    if i == tuplaObs:
                        break
                    else:
                        posiciones=posiciones+1
            else:
                buscarVertical(n,rq,cq,tuplaObs)
        elif ((obstacles[i] > rq and obstacles[i+1] > cq) or 
        ( obstacles[i] < rq and obstacles[i+1] < cq)):            
            tuplaObs=(obstacles[i],obstacles[i+1])
            if diagonalDerIzq:
                for i in diagonalDerIzq:
                    if i == tuplaObs:
                        break
                    else:
                        posiciones=posiciones+1
            else:
                buscarDerIzq(n,rq,cq,tuplaObs)
        else:           
            tuplaObs=(obstacles[i],obstacles[i+1])
            if diagonalIzqDer:
                for i in diagonalIzqDer:
                    if i == tuplaObs:
                        break
                    else:
                        posiciones=posiciones+1
            else:
                buscarIzqDer(n,rq,cq,tuplaObs)
    if not listaHorizontal:
        buscarHorizontal(n,rq,cq,(None,None))
    if not listaVertical:
        buscarVertical(n,rq,cq,(None,None))
    if not diagonalDerIzq:
        buscarDerIzq(n,rq,cq,(None,None))
    if not diagonalIzqDer:
        buscarIzqDer(n,rq,cq,(None,None))
    print("resultado:: "+str(posiciones)+" posibles movimientos de la reina.")

def buscarVertical(n,rq,cq,tuplaObs):    
    global posiciones
    #verticales
    start=rq+1
    stop=n+1
    for i in range(start,stop,1):
        if i > n:
            if not listaVertical:
                listaVertical.append((None,None))
            break
        if (i,cq)==tuplaObs:
            if not listaVertical:
                listaVertical.append((None,None))
            break
        else:
            posiciones=posiciones+1
            listaVertical.append((i,cq))
    start=rq-1
    stop=0
    for i in range(start,stop,-1):
        if i < 1:
            if not listaVertical:
                listaVertical.append((None,None))
            break
        if (i,cq)==tuplaObs:
            if not listaVertical:
                listaVertical.append((None,None))
            break
        else:
            posiciones=posiciones+1
            listaVertical.append((i,cq))
    # print("vertical::")
    # print(listaVertical)

def buscarHorizontal(n,rq,cq,tuplaObs):    
    global posiciones
    #horizontales
    start=cq+1
    stop=n+1
    for i in range(start,stop,1):
        if i > n:
            if not listaHorizontal:
                listaHorizontal.append((None,None))
            break
        if (rq,i)==tuplaObs:
            if not listaHorizontal:
                listaHorizontal.append((None,None))
            break
        else:
            posiciones=posiciones+1
            listaHorizontal.append((rq,i))
    start=cq-1
    stop=0
    for i in range(start,stop,-1):
        if i < 1:
            if not listaHorizontal:
                listaHorizontal.append((None,None))
            break
        if (rq,i)==tuplaObs:
            if not listaHorizontal:
                listaHorizontal.append((None,None))
            break
        else:
            posiciones=posiciones+1
        listaHorizontal.append((rq,i))
    # print("horizontal::")
    # print(listaHorizontal)

def buscarDerIzq(n,rq,cq,tuplaObs):
    global posiciones
    #derizq
    start=cq-1
    stop=0
    row=rq-1
    for i in range(start,stop,-1):
        if row < 1 or i < 1:
            if not diagonalDerIzq:
                diagonalDerIzq.append((None,None))
            break
        if (row,i)==tuplaObs:
            if not diagonalDerIzq:
                diagonalDerIzq.append((None,None))
            break
        else:
            posiciones=posiciones+1
            diagonalDerIzq.append((row,i))
        row=row-1
    start=cq+1
    stop=n+1
    row=rq+1
    for i in range(start,stop,1):
        if row > n or i > n:
            if not diagonalDerIzq:
                diagonalDerIzq.append((None,None))
            break
        if (row,i)==tuplaObs:
            if not diagonalDerIzq:
                diagonalDerIzq.append((None,None))
            break
        else:
            posiciones=posiciones+1
            diagonalDerIzq.append((row,i))
        row=row+1
    # print("der izq::")
    # print(diagonalDerIzq)
    
def buscarIzqDer(n,rq,cq,tuplaObs):
    global posiciones
    #izqder
    start=cq-1
    stop=0
    row=rq+1
    for i in range(start,stop,-1):
        if row > n or i < 1:
            if not diagonalIzqDer:
                diagonalIzqDer.append((None,None))
            break
        if (row,i)==tuplaObs:
            if not diagonalIzqDer:
                diagonalIzqDer.append((None,None))
            break
        else:
            posiciones=posiciones+1
            diagonalIzqDer.append((row,i))
        row=row+1
    start=cq+1
    stop=n+1
    row=rq-1
    for i in range(start,stop,1):
        if row < 1 or i > n:
            if not diagonalIzqDer:
                diagonalIzqDer.append((None,None))
            break
        if (row,i)==tuplaObs:
            if not diagonalIzqDer:
                diagonalIzqDer.append((None,None))
            break
        else:
            posiciones=posiciones+1
            diagonalIzqDer.append((row,i))
        row=row-1
    # print("izq der::")
    # print(diagonalIzqDer)
#=================================================
datos = """
5 3
4 3
5 5
4 2
2 3
"""
datos=datos.strip().replace("\n"," ")
datos=datos.replace("\n"," ")
datos=datos.split()
datos= [int(x) for x in datos]
queensAttack(datos[0],datos[1],datos[2],datos[3],
datos[4:])