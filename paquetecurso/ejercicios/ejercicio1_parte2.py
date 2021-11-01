# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:42:53 2021

@author: jairo
"""

print('Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:')

lista = ['Primera Interacción, ingrese un valor cualquiera:',
         'Segunda Interacción, ingrese un valor cualquiera:',
         'Tercera Interacción, ingrese un valor cualquiera:',
         'Cuarta Interacción, ingrese un valor cualquiera:',
         'Quinta Interacción, ingrese un valor cualquiera:']
for i in range(0, len(lista)):
    print(lista[i])
    var1 = input()
    print('Este tipo de dato en Python es:')
    try:
        if complex(var1).imag != 0:
            print('complex.')
        elif float(var1)%int(float(var1)) == 0:
            print('int.')
        else:
            print('float.')
    except ValueError:
            print('string.')
print('¡YA NO SE HARÁN MÁS INTERACCIONES!')