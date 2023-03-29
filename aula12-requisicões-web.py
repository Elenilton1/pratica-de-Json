import requests

cabecalho={"User-Agent":"Windows 15"}
meus_cookies={"ultima-visita":"27/03/2023"}
login_senha={"username":"junior",
             "password":"987654321"}
requisicao=requests.get("https://putsreq.com/r6rldhvsL5q7yuUNQcZe",
                        headers=cabecalho,
                        cookies=meus_cookies,
                        data=login_senha)
'''print(type(requisicao))'''
print(requisicao.text)
