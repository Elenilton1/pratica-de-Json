'''print("     VOTAÇÃO GLOBO PE      ")
print("Escolha o melhor time de pernambuco:\n1=SPORT\n2=NAUTICO\n3=SANTACRUZ")
a=input("Digite o número da votação:")
if int(a)==1:
    print("Você votou no SPORT e seu voto foi contabilizado.")
elif int(a)==2:
    print("Você votou no NAUTICO e seu voto foi contabilizado. ")
elif int(a)==3:
    print("Você votou no SANTACRUZ e seu voto foi contabilizado.")
else:
    print("VOTO INVÁLIDO,TENTE NOVAMENTE!")
'''
'''print("VERDADEIRO OU FALSO")
numeros=input("Escolha um número de 1 a 10:")
if int(numeros) >= int(5):
    verdadeiro = True
    print("Verdadeiro é,",verdadeiro)
elif int(numeros) < int(5):
    falso = False
   print("Falso é,",falso)'''

'''a = input("Digite um valor:")
b = input("Digite um valor:")
if (a>b):
    print(a,"é maior que",b)
else:
    print(b,"é maior que",a)'''
print("            FICHA CADASTRAL             ")
print("-----APTO OU INAPTO PARA O EXERCITO-----")
nome  = input("Qual o seu nome:")
idade = input("Qual a sua Idade?")
alt   = input("Qual a sua altura?")
peso  = input("Qual o seu peso?")
if (idade>"18") and (peso>"60") and (alt>"1.70"):
    print(nome,"\nVocê está apto a servir. ")
else:
    print(nome,"\nVocê está inapto.")


