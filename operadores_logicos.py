'''
OPERADORES LOGICOS
Los opoeradores logicos son:
and , or , not
obedecen las tablas de verdad:
JERARQUIA DEFINITIVA DE OPERADORES 
1.         ()
2.         **
3.      * , / , %
4.        + , -
5. > , < , != , == , <= , >=
6.         NOT
7.         AND
8.         OR
9.         =
NOTA: Si hay operaciones en el mismo nivel
de jerarquia, se resuelven de izquierda a derecha
'''
op1 = False
op2 = True
op3 = False
op4 = True
resultado = not op1 (op2 or op3 and not op1) and not op4
print(resultado)
a=6
b=3
c=7
d=4
e=5
resultado = not (a+b>c/d) or e*2!=d+c and not (a<b)
