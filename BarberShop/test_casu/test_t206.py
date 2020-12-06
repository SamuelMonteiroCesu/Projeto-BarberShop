import json,requests
import random
from validate_docbr import CPF
#nota 2306
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
appodata = []




print('####################texte status########################')
print('--------------------texte status post---------------------')
try:
    endpoint_status = "http://localhost:8000/status/"
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
    url = "http://localhost:8000/status/"
    for i in statsdata:
        resposta = requests.patch(url +str(i["status_id"])+'/',sta = {'name': '--update--'},headers=headers)
        print(resposta)
        print(i)
except:
    print('erro')


















print('####################texte Procedure########################')
print('--------------------texte Procedure post---------------------')
try:
    url = "http://localhost:8000/procedure/"
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
    url  = "http://localhost:8000/procedure/"
    for i in procedata:
        resposta = requests.put(url +str(i["procedure_id"])+'/',sta = {'name': '--update--'},headers=headers)
        print(str(i))
        print(resposta)
except:
    print('erro')



















print('####################texte Payment########################')
print('--------------------texte Payment post---------------------')
try:
    url = "http://localhost:8000/payment/"
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
    url = "http://localhost:8000/payment/"
    for k in paydata:
        resposta = requests.put(url +str(k["payment_id"])+'/',sta = {'name': '--update--'},headers=headers)
        k['name'] = 'cancelado'
        print(str(k))
        print(pay)
except:
    print('erro')

















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
    print(res)
except:
    print('erro a cadastrar cliente')

try:
    print('--------------------texte client put---------------------')
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
    print(res)
except:
    print('erro a cadastrar funcionario')

try:
    print('--------------------texte funcionario put---------------------')
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















print('####################texte dayoff########################')
try:
    print('--------------------texte dayoff post---------------------')
    url = "http://localhost:8000/dayoff/"
    sta =dict(daydate='20/03/2000',reason='teste' ,active=True , professional=1)
    pay = requests.post(url,data = sta,headers=headers)
    daydata.append (pay.json())
    print(str(pay))
except:
    print('erro a fazer post dayoff')


print('--------------------texte dayoff put---------------------')
try:
    url = "http://localhost:8000/dayoff/"
    sta =dict(daydate='30/12/2020',reason='--update--' ,active=True , professional=1)
    for k in daydata:
        resposta = requests.put(url +str(k["id"])+'/', data = sta,headers=headers)
        print(str(k))
        print(resposta)
except:
    print('erro a fazer put dayoff')














print('####################texte Schedule########################')
print('--------------------texte Schedule post---------------------')
try:
    url = "http://localhost:8000/schedule/"
    sta =dict(begin= '10:00',end='18:00', interval= random.randint(10,50),weekday=random.randint(0,6),active=True , professional=1)
    pay = requests.post(url,data = sta,headers=headers)
    squedata.append (pay.json())
    print(pay)
except:
    print('erro a fazer post Schedule')

print('--------------------texte Schedule put---------------------')
try:
    url = "http://localhost:8000/schedule/"
    sta =dict(begin= '12:00',end='16:00', interval= 20,weekday=5,active=True , professional=1)
    for k in squedata:
        resposta = requests.put(url +str(k["id"])+'/', data= sta,headers=headers)
        print(str(k))
        print(resposta)
except:
    print('erro a fazer put Schedule')

print('--------------------texte Schedule delete---------------------')
try:
    url = "http://localhost:8000/Schedule/"
    for t in squedata:
        d = requests.delete(url +str(t["id"])+'/',headers=headers)
        print(d)
except:
    print('erro a fazer post Schedule')
    print(d)




print('####################texte Appointment########################')
print('--------------------texte Appointment post---------------------')
try:
    #appdate = '10/12/2000',
    #apphour = '10:00'
    url = "http://localhost:8000/appointment/"
    sta =dict( client = 25,professional = 1,status = 95,procedure = 1,payment = 1,
    appdate = '10/12/2000',apphour = '10:00' )
    pay = requests.post(url,data = sta,headers=headers)
    appodata.append (pay.json())
    print(str(pay.json()))
    print(pay)
except:
    print('erro a fazer post Appointment')

print('--------------------texte Appointment put---------------------')
try:
    url = "http://localhost:8000/appointment/"
    sta = dict(appdate= '12/12/2001')
    for k in appodata:
        resposta = requests.patch(url +str(k["id"])+'/',data= sta ,headers=headers)
        print(resposta)
except:
    print('erro a fazer put Appointment')

print('--------------------texte Appointment delete---------------------')
try:
    url = "http://localhost:8000/appointment/"
    for t in appodata:
        print(str(t))
        d = requests.delete(url +str(t["id"])+'/',headers=headers)
        print(d)
except:
    print('erro a fazer post Appointment')
    print(d)











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

print('--------------------texte dayoff delete---------------------')
try:
    url = "http://localhost:8000/dayoff/"
    for t in daydata:
        d = requests.delete(url +str(t["id"])+'/',headers=headers)
        print(str(t))
        print(d)
except:
    print('erro a fazer delete dayoff')

print('--------------------texte Appointment delete---------------------')
try:
    url = "http://localhost:8000/appointment/"
    for t in appodata:
        print(str(t))
        d = requests.delete(url +str(t["id"])+'/',headers=headers)
        print(d)
except:
    print('erro a fazer post Appointment')
    print(d)
