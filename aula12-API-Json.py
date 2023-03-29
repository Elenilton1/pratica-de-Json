import requests
import json
def dados(personagem1):
 print("Nome:",personagem1["name"],"\nIdade:",personagem1["id"],
       "\nStatus:",personagem1["status"],"\nEspecie:",personagem1["species"],"\nFoto:",personagem1["image"])
personagem=None
resposta=False
print("Dados Sobre os Personagens de Rick and Morty")
print("--------------------------------------------")
print("        Tabela de numeração                 ")
print("|01- rick sanchez| |02- Morty| |03- Summer| |04-Beth Smith| |05-Jerry Smith|\n"
"|06-Abadango Cluster Princess| |07-bradolf Lincler| |08-Adjudicator Rick|\n"
"|09-Agency Director| |10-Alan Rails| |11-Albert Einstein| |12-Alexander| |13-Alien Googah |14-Alien Morty| |15-Alien Rick| \n"
"|16-Amish Cyborg| |17-Annie|  |18-Antenna Morty|  |19-Antenna Rick|  |20-Ants in my Eyes Johnson| |21-Aqua Morty| |22-Aqua Rick|\n"
"|23-Arcade Alien| |24-Armagheadon| |25-Armothy|  |26-Arthricia| |27-Artist Morty| |28-Attila Starwar| |29-Baby Legs| |30-Baby Poopybutthole")
print()
print("------------------------------------------------------------------")
while resposta==False:
 x=input("infomando o número de indentificação, qual personagem você gostaria de ter mais informações?")
 try:
     personagem= requests.get("https://rickandmortyapi.com/api/character/"+x)
     dicionario = json.loads(personagem.text)
     informações = dados(dicionario)
     print(informações)
 except Exception as erro:
    print("personagem não encontrado,erro:",erro)
    exit()
 resposta1=input("Gostaria de continuar com a pesquisa?")
 if resposta1=="Não":
    break
 else:
     resposta=False













