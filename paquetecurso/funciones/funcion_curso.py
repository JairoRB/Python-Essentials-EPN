# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 11:40:14 2021

@author: jairo
"""

def curso():
    """ Función para desplegar los ejercicios vistos en clase """
    aux = 1
    while aux != 0:
        print('===================================================================')
        print('Seleccione el ejercicio de clase que desea ejecutar:')
        print('1): Ejercicio 1 parte 1')
        print('2): Ejercicio 1 parte 2')
        print('3): Ejercicio 2 parte 1')
        print('4): Ejercicio 2 parte 2')
        print('5): Ejercicio 3')
        print('0): Salir')
        
        try:
            n = int(input('Ingrese su selección: '))
            if n == 1:
                print('*******************************************************************')
                print('Usted ha seleccionado al ejercicio 1 parte 1.')
                print('*******************************************************************')
                import paquetecurso.ejercicios.ejercicio1_parte1 as ej1p1
            elif n == 2:
                print('*******************************************************************')
                print('Usted ha seleccionado al ejercicio 1 parte 2.')
                print('*******************************************************************')
                import paquetecurso.ejercicios.ejercicio1_parte2 as ej1p2
            elif n == 3:
                print('*******************************************************************')
                print('Usted ha seleccionado al ejercicio 2 parte 1.')
                print('*******************************************************************')
                import paquetecurso.ejercicios.ejercicio2_parte1 as ej2p1
            elif n == 4:
                print('*******************************************************************')
                print('Usted ha seleccionado al ejercicio 2 parte 2.')
                print('*******************************************************************')
                import paquetecurso.ejercicios.ejercicio2_parte2 as ej2p2
            elif n == 5:
                print('*******************************************************************')
                print('Usted ha seleccionado al ejercicio 3.')
                print('*******************************************************************')
                import paquetecurso.ejercicios.ejercicio3 as ej3
            elif n == 0:
                print('Usted ha seleccionado salir.')
                print('¡Hasta pronto!' )
                print('===================================================================')
                aux = 0
            else:
                print('*******************************************************************')
                print('Debe seleccionar una de las opciones indicadas.')
                print('*******************************************************************')            
        except ValueError:
            print('*******************************************************************')
            print('Ingrese su selección como un número entero.')
            print('*******************************************************************')
    return