# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 17:04:42 2021

@author: jairo
"""
# Funcion para seleccionar valores altos y bajos
def sel_valores(lista, altos, bajos):
    m = len(lista)
    lista_altos = lista[m-altos:m]
    lista_bajos = lista[0:bajos]
    resultado = lista_bajos + lista_altos
    print('Valores calculados en formato LISTA: ', resultado)
    print('Valores calculados en formato TUPLA: ',tuple(resultado))
    return

# Funcion para seleccionar y manipular diccionario
def sel_dic(n):
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

aux = 0
dic1 = {'Raul':34,'Paula':19,'Jorge':43,'Richard':10,'Diana':3,'Isabel':76,'Gustavo':12,'Diego':37}
dic2 = {'tplA':(4,-12,56,-34,98,102),'tplB':(9,0,1,10,-3,14),'tlpC':(87,12,56,987,-61)}
dic3 = {'val1':-12.5,'val2':12.5,'val3':83,'val4':2.1,'val5':23,'val6':100,'val7':13.4,'val8':92}
dic4 = {'lst1':[4,6,-12,56,-9,5.7,33,100],'lst2':[9,0,81,-2,-56,],'lst3':[12,31,87,1,0,4,-11]}
diccionario = {'1':dic1, '2':dic2, '3':dic3, '4':dic4}
print('====================================================================================')
while aux == 0:
    print('Elija una opción:')
    print('1) Demostración del cálculo de valores altos y bajos en diccionarios.')
    print('2) Salir.')
    valor = int(input("Ingrese el número de su selección:"))
    if valor == 2:
        print('¡Hasta pronto!')
        print('====================================================================================')
        aux = 1
    elif valor == 1:
        print('Elija un diccionario para la demostración:')
        print('1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}')
        print('2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}')
        print('3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}')
        print('4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}')
        aux2 = 0
        while aux2 == 0:
            dic_sel = int(input("Ingrese el número de su selección para el diccionario:"))
            if dic_sel == 1 or dic_sel == 2 or dic_sel == 3 or dic_sel == 4:
                sel_dic(dic_sel)
                aux2 = 1
            else:
                print('Debe ingresar la opción 1, 2, 3 o 4.')
                print('____________________________________________________________________________________')
    elif valor != 1 or valor != 2:
        print('Debe ingresar la opción 1 o 2.')
        print('____________________________________________________________________________________')