pi = 3.141592

def factorial_super(n):
    
    #defining variable
    f=1

    #definimos el conjunto en que va a correr mi indice.
    conjunto = range(2,n+1)

    #empezamos nuestro ciclo
    for i in conjunto:
        f=f*i
    return f
    #OBS: dentro del ciclo estamos escribiendo dos veces f, una adentro del ciclo for para
    #ver cada iteracion de mi ciclo, la segunda para obtener el resultado final.


def mi_seno2(x,orden):
    
    #Es util trabajar en modulo 2pi porque mi serie de taylor 
    #pierde precision conforme mis numeros son mas grandes.
    x = x%(2*pi)
    y = 0.0
    print ("El valor original es equivalente a: "+str(x)+" modulo 2pi")
    
    #Tambien queremos que nos diga en que intervalo de pi medios 
    #esta el numero del que quiero calcular el seno.
    if x<=(pi/2):
        print (str(x)+" esta en el intervalo 1")
    elif (pi/2)<x<=pi:
        print (str(x)+" esta en el intervalo 2")
        x=pi-x
    elif pi<x<=(3*pi/2):
        print (str(x)+" esta en el intervalo 3")
        x=-(x-pi)
    else:
        print (str(x)+" esta en el intervalo 4")
        x=x-2*pi
    
    #Usaremos un for para hacer la serie de Taylor
    for n in range(orden):
        p = 2*n+1
        y += (((-1)**n)*(x**(p))/(factorial_super(p)))
        #y += significa y = y + ....
        
    return y
