'''import time
try:
   dkjaks

except ZeroDivisionError :
    x=ZeroDivisionError
    print("divisão inrregular",x)
except NameError:
    x=NameError
    print("Nome foi digitado incorretamente",x,
          time.sleep(5),"se passaram 5 segundos, desde o resultado")
if x==ZeroDivisionError:
     print("divisão irregular",x)
elif x==NameError:
        print("Nome foi digitado incorretamente",x)
else:
        print("Erro sem idenficação")'''
import time


def abrir_arquivo():
    try:
        open("arquivodoido.txt")
        print("Conseguimos!!")
        return True
    except Exception as erro:
        print("Aconteceu algum erro:",erro)
        return False
while not abrir_arquivo():
    print("Tentando abrir arquivo")
    time.sleep(3)
print("arquivo aberto")
