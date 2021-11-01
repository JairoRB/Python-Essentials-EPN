# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 11:33:34 2021

@author: jairo
"""

from paquetecurso.funciones.sel_valor import sel_valores

def sel_dic(n,diccionario):
    """ Funcion para seleccionar y manipular diccionario """
    aux_altos = 0
    aux_bajos = 0
    aux_dic = diccionario[str(n)]
    valores_list = list(aux_dic.values())
    valores_list = sorted(valores_list)
    n = len(valores_list)
    if type(valores_list[0]) == tuple or type(valores_list[0]) == list:
        aux_list = list(valores_list[0])
    else:
        aux_list = [valores_list[0]]
    for i in range(1, n):
        if type(valores_list[i]) == tuple or type(valores_list[i]) == list:
            aux_list = aux_list + list(valores_list[i])
        else:
            aux_list.append(valores_list[i])
    aux_list = sorted(aux_list)
    print('El diccionario cuenta con ', len(aux_list), 'valores distintos.')
    while aux_altos == 0:
        altos = int(input('Digite el número de valores altos que desea mostrar:'))
        if altos > len(aux_list):
            print('El valor ingresado supera al tamaño del diccionario, vuelva a ingresar su selección.')
        else:
            while aux_bajos == 0:
                bajos = int(input('Digite el número de valores bajos que desea mostrar:'))
                if bajos > len(aux_list):
                    print('El valor ingresado supera al tamaño del diccionario, vuelva a ingresar su selección.')
                else:
                    sel_valores(aux_list, altos, bajos)
                    print('____________________________________________________________________________________')
                    aux_bajos = 1
                    aux_altos = 1
    return