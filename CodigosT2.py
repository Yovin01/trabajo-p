from cProfile import label
import matplotlib.pyplot as plt
import numpy as mat


#Graficas    
def cod_4 (n):
    # Funcion m1
    return 9 + 7*n

def cod_4_5 (n):
    # Funcion 2
    return 7*n*n +11*n +9

n = range(1 , 100)
plt.plot(n, [cod_4(i) for i in n], label= 'Funcion 1')
plt.plot(n, [cod_4_5(i) for i in n],label= 'Funcion 2')
plt.axhline(1, color="black")
plt.axvline(1, color="black")
plt.xlim(1, 30)
plt.ylim(1, 200)
plt.legend(loc='lower right')
plt.show() 