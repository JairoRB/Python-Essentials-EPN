# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 17:04:42 2021

@author: jairo
"""

from paquetecurso.funciones.sel_dicc import sel_dic

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
                sel_dic(dic_sel,diccionario)
                aux2 = 1
            else:
                print('Debe ingresar la opción 1, 2, 3 o 4.')
                print('____________________________________________________________________________________')
    elif valor != 1 or valor != 2:
        print('Debe ingresar la opción 1 o 2.')
        print('____________________________________________________________________________________')