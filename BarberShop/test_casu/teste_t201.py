import json,requests
import random
from validate_docbr import CPF
#nota 2306
#metodo utilizado para obter token de acesso com localhost user=pedro senha=pedro098 
#metodo utilizado para obter token de acesso com heroku user=pedro senha=pedro098 
Token = requests.post('http://localhost:8000/login/',{'username':'pedro','password':'pedro098'})
te = Token.json()
headers={'Authorization': 'Bearer '+ te["access"]}

statsdata=[]
procedata=[]
paydata=[]
clientdata=[]
funcdata=[]
daydata=[]
squedata =[]
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)















print('####################texte status########################')
print('--------------------texte status post---------------------')
try:
    endpoint_status = "http://localhost:8000/status/"
    nomes = ["finalizado", "em andamento", "cancelado", "reagendado"]
    for x in nomes:
        sta = dict(name=x)
        res = requests.post(endpoint_status,data = sta,headers=headers)
        statsdata.append(res.json())
        print(str(res.json()))
except:
    print('erro')


print('--------------------texte status put---------------------')
try:
    url = "http://localhost:8000/status/"
    for i in statsdata:
        resposta = requests.put(url +str(i["status_id"])+'/',sta = {'name': '--update--'},headers=headers)
        i['name'] = 'refeito'
        print(str(i))
    #print(resposta.status_code)
except:
    print('erro')



print('')
print('####################texte Procedure########################')
print('')
print('--------------------texte Procedure post---------------------')
try:
    url = "http://localhost:8000/procedure/"
    nomes = ["cortar", "barbear", "lavar", "pentear"]
    for x in nomes:
        sta =dict(name=x,time = random.randint(1, 100),price=random.randint(0,50) )
        pro = requests.post(url,data = sta,headers=headers)
        procedata.append(pro.json())
        print(str(pro.json()))
except:
    print('erro')
print('')
print('--------------------texte Procedure put---------------------')
try:
    url  = "http://localhost:8000/procedure/"
    for i in procedata:
        resposta = requests.put(url +str(i["procedure_id"])+'/',sta = {'name': 'cancelado'},headers=headers)
        print(str(i))
except:
    print('erro')
print('')


print('####################texte Payment########################')
print('')
print('--------------------texte Payment post---------------------')
try:
    url = "http://localhost:8000/payment/"
    nomes = ["debito", "credito", "dinheiro"]
    for x in nomes:
        sta =dict(name = x,discount=random.randint(0,35),tax=random.randint(10,45),active=True )
        pay = requests.post(url,data = sta,headers=headers)
        paydata.append (pay.json())
        print(str(pay.json()))
except:
    print('erro')

print('--------------------texte Payment put---------------------')
try:
    url = "http://localhost:8000/payment/"
    for k in paydata:
        resposta = requests.put(url +str(k["payment_id"])+'/',sta = {'name': 'cancelado'},headers=headers)
        print(str(k))
except:
    print('erro')
print('')

print('####################finalizando teste########################')
print('')
try:
    print('--------------------texte status delete---------------------')
    url = "http://localhost:8000/status/"
    for t in statsdata:
        print(str(t))
        d = requests.delete(url +str(t["status_id"])+'/',headers=headers)
except:
    print('erro')
try:
    print('--------------------texte Payment delete---------------------')
    url = "http://localhost:8000/payment/"
    for de in paydata:
        print(str(de))
        d = requests.delete(url +str(de["payment_id"])+'/',headers=headers)
except:
    print('erro')
try:
    print('--------------------texte procedure delete---------------------')
    url = "http://localhost:8000/procedure/"
    for k in procedata:
        print(str(k))
        d = requests.delete(url +str(k["procedure_id"])+'/',headers=headers)
except:
    print('erro')