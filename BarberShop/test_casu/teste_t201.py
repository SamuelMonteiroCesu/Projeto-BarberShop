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




print('####################texte status########################')
print('--------------------texte status post---------------------')
try:
    endpoint_status = "https://barbershoppi.herokuapp.com/status/"
    nomes = ["finalizado", "em andamento", "cancelado", "reagendado"]
    for x in nomes:
        sta = dict(name=x)
        res = requests.post(endpoint_status,data = sta,headers=headers)
        statsdata.append(res.json())
        print(res)
except:
    print('erro')


print('--------------------texte status put---------------------')
try:
    url = "https://barbershoppi.herokuapp.com/status/"
    sta =dict(name = "--update--")
    for i in statsdata:
        resposta = requests.put(url +str(i["status_id"])+'/',data = sta,headers=headers)
        print(resposta)
except:
    print('erro')


















print('####################texte Procedure########################')
print('--------------------texte Procedure post---------------------')
try:
    url = "https://barbershoppi.herokuapp.com/procedure/"
    nomes = ["cortar", "barbear", "lavar", "pentear"]
    for x in nomes:
        sta =dict(name=x,time = random.randint(1, 100),price=random.randint(0,50) )
        pro = requests.post(url,data = sta,headers=headers)
        procedata.append(pro.json())
        print(str(pro.json()))
        print(pro)
except:
    print('erro')

print('--------------------texte Procedure put---------------------')
try:
    url  = "https://barbershoppi.herokuapp.com/procedure/"
    sta =dict(name = "--update--")
    for i in procedata:
        resposta = requests.put(url +str(i["procedure_id"])+'/',data = sta ,headers=headers)
        print(resposta)
except:
    print('erro')



















print('####################texte Payment########################')
print('--------------------texte Payment post---------------------')
try:
    url = "https://barbershoppi.herokuapp.com/payment/"
    nomes = ["debito", "credito", "dinheiro"]
    for x in nomes:
        sta =dict(name = x,discount=random.randint(0,35),tax=random.randint(10,45),active=True )
        pay = requests.post(url,data = sta,headers=headers)
        paydata.append (pay.json())
        print(str(pay.json()))
        print(pay)
except:
    print('erro')

print('--------------------texte Payment put---------------------')
try:
    url = "https://barbershoppi.herokuapp.com/payment/"
    sta =dict(name = "--update--")
    for k in paydata:
        resposta = requests.put(url +str(k["payment_id"])+'/',data = sta,headers=headers)
        k['name'] = 'cancelado'
        print(pay)
except:
    print('erro')
print('####################finalizando teste########################')
print('')
try:
    print('--------------------texte status delete---------------------')
    url = "https://barbershoppi.herokuapp.com/status/"
    for t in statsdata:
        print(str(t))
        d = requests.delete(url +str(t["status_id"])+'/',headers=headers)
except:
    print('erro')
try:
    print('--------------------texte Payment delete---------------------')
    url = "https://barbershoppi.herokuapp.com/payment/"
    for de in paydata:
        print(str(de))
        d = requests.delete(url +str(de["payment_id"])+'/',headers=headers)
except:
    print('erro')
try:
    print('--------------------texte procedure delete---------------------')
    url = "https://barbershoppi.herokuapp.com/procedure/"
    for k in procedata:
        print(str(k))
        d = requests.delete(url +str(k["procedure_id"])+'/',headers=headers)
except:
    print('erro')