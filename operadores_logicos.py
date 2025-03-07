'''
OPERADORES LOGICOS
Los opoeradores logicos son:
and , or , not
obedecen las tablas de verdad:

'''
op1 = True
op2 = False
op3 = op1 and op2
print(op3)

op4 = op1 or op2
print(op4)

#operador not
op5 = not op1
print(op5)

'''
JERARQUIA DEFINITIVA DE OPERADORES 
        ()
        **
     * , / , %
       + , -
> , < , != , == , <= , >=
NOT
AND
OR
=
'''