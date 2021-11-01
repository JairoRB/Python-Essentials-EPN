# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 11:32:48 2021

@author: jairo
"""

def sel_valores(lista, altos, bajos):
    """ Funcion para seleccionar valores altos y bajos """
    m = len(lista)
    lista_altos = lista[m-altos:m]
    lista_bajos = lista[0:bajos]
    resultado = lista_bajos + lista_altos
    print('Valores calculados en formato LISTA: ', resultado)
    print('Valores calculados en formato TUPLA: ',tuple(resultado))
    return