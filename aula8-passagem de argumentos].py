import sys

argumentos= sys.argv
def soma (n1,n2):
    return n1 + n2
def sub (n1,n2):
    return  n1 - n2
if argumentos[1]=="soma":
   resul= soma (int(argumentos[2]),int(argumentos[3]))
elif argumentos[1]=="sub":
    resul= sub (int(argumentos[2]),int(argumentos[3]))
print(resul)
print(len(argumentos))



#print(argumentos)