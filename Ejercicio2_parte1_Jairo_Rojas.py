# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:38:09 2021

@author: jairo
"""

# Datos
Datos_2021 = [15, 20, 3,91,4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]
# Transformacion a tupla
datos_tup = tuple(Datos_2021)
datos_tup = sorted(datos_tup)
# Tamano de la tupla
n = len(datos_tup)

# Determinacion de Q1
k1 = int(n/4)
Q1 = datos_tup[k1]
# Determinacion de Q3
k3 = int(3*n/4)
Q3 = datos_tup[k3]
# Determinacion del rango intercuantil
IQR = Q3 - Q1 

# Listas para resultados
par = []
impar = []
atipico = []

# Bucle para resultados
for i in range(0, n):
    if datos_tup[i] % 2 == 0:
        par.append(datos_tup[i])
    else:
        impar.append(datos_tup[i])
    if datos_tup[i] > Q3 + 1.5*IQR or datos_tup[i] < Q1 - 1.5*IQR:
        atipico.append(datos_tup[i])
        
# Resultados
print('====================================================================================')
print('Las respuestas se muestran ordenadas de menor a mayor.')
print('Los valores pares en "Datos_2021" son:', sorted(par))
print('Los valores impares en "Datos_2021" son:', sorted(impar))
print('Criterio de selección de valores atípicos.')
print('q es un valor atipico si: \n q > Q3 + 1.5*IQR o q < Q1 - 1.5*IQR')
print('donde:')
print('Q1 es una estimacion del primer cuantil')
print('Q3 es una estimacion del tercer cuantil')
print('IQR es una estimacion del rango intercuantil')
print('Los valores atípicos en "Datos_2021" son:', sorted(atipico))
print('====================================================================================')