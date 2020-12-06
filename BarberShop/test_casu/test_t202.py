import json,requests
import random
from validate_docbr import CPF
from datetime import date
#metodo utilizado para obter token de acesso com localhost user=pedro senha=pedro098 
#metodo utilizado para obter token de acesso com heroku user=pedro senha=pedro098 
Token = requests.post('http://localhost:8000/login/',{'username':'nota','password':'2306'})
te = Token.json()
headers={'Authorization': 'Bearer '+ te["access"]}

statsdata=[]
procedata=[]
paydata=[]
clientdata=[]
funcdata=[]
daydata=[]
squedata =[]


print('####################texte Client########################')
try:
    print('--------------------texte Client post---------------------')
    url = "http://localhost:8000/client/"
    cpf = CPF()
    new_cpf_one = cpf.generate()
    sta =dict(first_name="teste",last_name="teste",birthday = "13/11/20", email= "pepe.pedro3@gmail.com",
    username= new_cpf_one, password = "pedro",is_staff= False)
    res = requests.post(url,data = sta)
    clientdata.append (res.json())
    print(str(res))
except:
    print('erro a cadastrar cliente')

try:
    print('--------------------texte client atualizar dados---------------------')
    url = "http://localhost:8000/client/"
    for k in clientdata:
        resposta = requests.patch(url +str(k["id"])+'/',data= {'first_name' :'--update--'},headers=headers)
        print(resposta)
except:
    print('erro a atualizar o cliente cliente')

try:
    print('--------------------texte client delete---------------------')
    url = "http://localhost:8000/client/"
    for de in clientdata:
        print(str(de))
        d = requests.delete(url +str(de["id"])+'/',headers=headers)
except:
    print('erro a deletar o cliente cliente')



print('####################texte cadastro funcionario########################')
try:
    print('--------------------texte funcionario post---------------------')
    url = "http://localhost:8000/client/"
    cpf = CPF()
    new_cpf_one = cpf.generate()
    sta =dict(first_name="teste",last_name="teste", email= "pepe.pedro3@gmail.com",
    username= new_cpf_one, password = "pedro",is_staff= True)
    res = requests.post(url,data = sta,headers=headers)
    funcdata.append (res.json())
    print(str(res))
except:
    print('erro a cadastrar funcionario')

try:
    print('--------------------texte funcionario atualizar dados---------------------')
    url = "http://localhost:8000/client/"
    for k in funcdata:
        resposta = requests.patch(url +str(k["id"])+'/',data= {'first_name' :'--update--'},headers=headers)
        print(str(k))
except:
    print('erro a atualizar o cliente cliente')

try:
    print('--------------------texte funcionario delete---------------------')
    url = "http://localhost:8000/client/"
    for de in funcdata:
        print(str(de))
        d = requests.delete(url +str(de["id"])+'/',headers=headers)
except:
    print('erro a deletar o funcionario ')
