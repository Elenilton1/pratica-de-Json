'nomes=["joão","joaquim","josé","fernando","lucas"]'
'''for x in nomes:
    print(x)
#print(type(x))
lista_de_numeros= range(0, 101 , 10)
for i in lista_de_numeros:
    print(i)
for x in range(len(nomes)):
    print(nomes[x])'''
'''for x in range(len(nomes)):
    print(nomes[x])
    nomes.append("piroca")
print(nomes)'''
'''palavra=('Elenilton Ferreira')
for x in palavra:
    print(x)'''
'''i =0
while i < 10:
    print(i)
    i = i+1
print("acabou o while",i)'''

'''lopp = True
while lopp ==True :
    print("     VOTAÇÃO GLOBO PE      ")
    print("Escolha o melhor time de pernambuco:\n1=SPORT\n2=NAUTICO\n3=SANTACRUZ")
    a=input("Digite o número da votação:")
    if int(a)==1:
      print("Você votou no SPORT e seu voto foi contabilizado.")
      lopp = False
    elif int(a)==2:
       print("Você votou no NAUTICO e seu voto foi contabilizado. ")
       lopp = False
    elif int(a)==3:
       print("Você votou no SANTACRUZ e seu voto foi contabilizado.")
       lopp = False
    else:
      print("VOTO INVÁLIDO,TENTE NOVAMENTE!")
      lopp = True'''


'''contador=0
lista_frutas=['maça','caju','acerola','manga','goiaba']
for x in lista_frutas:
    contador+=1
print(contador)
print(len(lista_frutas))'''

'''contador = 0

while True:
    print(contador)
    contador+=1
    if contador==20:
      break

print(contador)'''

#Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa, após isso o programa irá
#perguntar o nome de todas as pessoas e colocar numa lista de convidados, após isso, imprimir todos os nomes da lista.
lista=1
lista_de_convidados=[]
print(      "ORGANIZAÇÃO DE CONVIDADOS PARA A FESTA"       )
convidados=input("Quantas pessoas serão convidadas?")
while lista <= int(convidados):
   nomes=input('Qual o nome do convidado '+str(lista)+ '?')
   lista_de_convidados.append(nomes)
   lista+=1
print('-------LISTA DE CONVIDADOS-------')
for x in lista_de_convidados:
   print(x)









