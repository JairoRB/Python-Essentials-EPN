# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:10:19 2021

@author: jairo
"""

# Listas para validar contrasena
let_min = ['a','b','c','d','e','f','g','h','i','j']
let_may = ['K','L','M','N','O','P','Q','R','S','T']
numr = ['0','1','2','3','4','5','6','7','8','9']
simb = ['$','%','*','@']

# Ingreso de datos
print('====================================================================================')
print('Debe ingresar su contraseña, con las siguientes condiciones:')
print('Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.')
print('Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.')
print('Debe contener al menos un número entre 0 y 9.')
print('Debe contener un símbolo especial entre: $,%,*,@')
print('Tamaño mínimo de 5 caracteres y máximo de 15.')
      
contr = input('Ingrese su contraseña:')

con_list = list(contr)
n = len(con_list)

aux_lmi = 0
aux_lma = 0
aux_num = 0
aux_sim = 0

if len(con_list) > 4 and len(con_list) < 16:
    for i in range(0,len(con_list)):
        if con_list[i] in let_min:
            aux_lmi = 1
        elif con_list[i] in let_may:
            aux_lma = 1
        elif con_list[i] in numr:
            aux_num = 1
        elif con_list[i] in simb:
            aux_sim = 1
else:
    print('La contraseña ingresada no cumple el tamaño requerido.')
    
if aux_lmi*aux_lma*aux_num*aux_sim != 0:
    print('La contraseña ingresada es válida.')
else:
    print('La contraseña ingresada no es válida.')
print('====================================================================================')