import json,requests
import random
from validate_docbr import CPF
#nota 2306
#metodo utilizado para obter token de acesso com localhost user=pedro senha=pedro098 
#metodo utilizado para obter token de acesso com heroku user=julio senha=95460368 
Token = requests.post('https://barbershoppi.herokuapp.com/login/',{'username':'julio','password':'95460368'})
te = Token.json()
headers={'Authorization': 'Bearer '+ te["access"]}

statsdata=[]
procedata=[]
paydata=[]
clientdata=[]
funcdata=[]
daydata=[]
squedata =[]
appodata = []

print('####################texte Client########################')
try:
    print('--------------------texte Client post---------------------')
    url = "https://barbershoppi.herokuapp.com/client/"
    cpf = CPF()
    new_cpf_one = cpf.generate()
    sta =dict(first_name="teste",last_name="teste",birthday = "13/11/20", email= "pepe.pedro3@gmail.com",
    username= new_cpf_one, password = "pedro",is_staff= False)
    res = requests.post(url,data = sta)
    clientdata.append (res.json())
    print(str(res))
    print(res)
except:
    print('erro a cadastrar cliente')

try:
    print('--------------------texte client put---------------------')
    url = "https://barbershoppi.herokuapp.com/client/"
    for k in clientdata:
        resposta = requests.patch(url +str(k["id"])+'/',data= {'first_name' :'--update--'},headers=headers)
        print(str(t))
        print(resposta)
except:
    print('erro a atualizar o cliente cliente')

try:
    print('--------------------texte client delete---------------------')
    url = "https://barbershoppi.herokuapp.com/client/"
    for de in clientdata:
        print(str(de))
        d = requests.delete(url +str(de["id"])+'/',headers=headers)
except:
    print('erro a deletar o cliente cliente')













print('####################texte cadastro funcionario########################')

print('--------------------texte funcionario post---------------------')
url = "https://barbershoppi.herokuapp.com/client/"
cpf = CPF()
new_cpf_one = cpf.generate()
try:
    sta =dict(first_name="teste",last_name="teste", email= "pepe.pedro3@gmail.com",
    username= new_cpf_one, password = "pedro",is_staff= True)
    res = requests.post(url,data = sta,headers=headers)
    funcdata.append (res.json())
    print(str(res))
    print(res)
except:
    print('erro a cadastrar funcionario')

try:
    print('--------------------texte funcionario put---------------------')
    url = "https://barbershoppi.herokuapp.com/client/"
    for k in funcdata:
        resposta = requests.patch(url +str(k["id"])+'/',data= {'first_name' :'--update--'},headers=headers)
        print(str(k))
except:
    print('erro a atualizar o cliente cliente')

try:
    print('--------------------texte funcionario delete---------------------')
    url = "https://barbershoppi.herokuapp.com/client/"
    for de in funcdata:
        print(str(de))
        d = requests.delete(url +str(de["id"])+'/',headers=headers)
except:
    print('erro a deletar o funcionario ')