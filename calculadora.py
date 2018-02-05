#!/usr/bin/python3

import sys

num1 = float(sys.argv[2])
operando = sys.argv[1]
num2 = float(sys.argv[3])
ok = 1

if operando == "suma":
    resultado = num1+num2
    ok = 0  
elif operando == "resta":
    resultado = num1-num2
    ok = 0
elif operando == "multiplicacion":
    resultado = num1*num2
    ok = 0
elif operando == "division":
    try:
        resultado = num1/num2
    except ZeroDivisonError:
        print("Has intentado dividir por cero melon")
        ok = 1
else:
    print("Prueba:'operador'(suma,resta,multiplicacion y division) 'operando 1' 'operando 2'")
if ok == 0:
    print(resultado)
