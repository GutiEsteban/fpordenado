# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 12:26:53 2021

@author: gutie
"""

# Practicando funciones

def retornar_superficie(lado):
    sup=lado*lado
    return sup


# bloque principal del programa

va=int(input("Ingrese el valor del lado del cuadrado:"))
superficie=retornar_superficie(va)
print("La superficie del cuadrado es",superficie)