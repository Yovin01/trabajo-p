import matplotlib.pyplot as plt
import numpy as mat

array1= [1,4,2,7,30,12]

def obtenerMayor(array):
    count = array[0]
    for i in range(1,len(array)):
        if(count < array[i]):
            count = array[i]
    print(count)
    return count


def transpuesta(m):
    a = []
    for i in range(len(m[0])):
        a.append([])
        for j in range(len(m)):
            a[i].append(m[j][i])
   
    return a

def fibonacci(n):
    if(n<2):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
obtenerMayor(array1)

