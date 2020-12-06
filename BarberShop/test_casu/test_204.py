import json
import random
import requests

#metodo utilizado para obter token de acesso com localhost user=pedro senha=pedro098 
#metodo utilizado para obter token de acesso com heroku user=pedro senha=pedro098 
localdata=[]

print('--------------------texte recuperacao senha---------------------')
url = "https://barbershoppi.herokuapp.com/passrecover/"
print('digite o cpf do usuario para recuperar a senha')
x = input()
print('digite o email do usuario para recuperar a senha')
y = input()
sta =dict(CPF = x,email=y )
pro = requests.post(url,data = sta)
print(pro)