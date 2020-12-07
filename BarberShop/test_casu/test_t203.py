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


print('####################texte dayoff########################')
try:
    print('--------------------texte dayoff post---------------------')
    url = "https://barbershoppi.herokuapp.com/dayoff/"
    sta =dict(daydate='20/03/2000',reason='teste' ,active=True , professional=1)
    pay = requests.post(url,data = sta,headers=headers)
    daydata.append (pay.json())
    print(str(pay))
except:
    print('erro a fazer post dayoff')


print('--------------------texte dayoff put---------------------')
try:
    url = "https://barbershoppi.herokuapp.com/dayoff/"
    sta =dict(daydate='30/12/2020',reason='--update--' ,active=True , professional=1)
    for k in daydata:
        resposta = requests.put(url +str(k["id"])+'/', data = sta,headers=headers)
        print(str(k))
        print(resposta)
except:
    print('erro a fazer put dayoff')

print('--------------------texte dayoff delete---------------------')
try:
    url = "https://barbershoppi.herokuapp.com/dayoff/"
    for t in daydata:
        d = requests.delete(url +str(t["id"])+'/',headers=headers)
        print(str(t))
        print(d)
except:
    print('erro a fazer delete dayoff')













print('####################texte Schedule########################')
print('--------------------texte Schedule post---------------------')
try:
    url = "https://barbershoppi.herokuapp.com/schedule/"
    sta =dict(begin= '10:00',end='18:00', interval= random.randint(10,50),weekday=random.randint(0,6),active=True , professional=1)
    pay = requests.post(url,data = sta,headers=headers)
    squedata.append (pay.json())
    print(pay)
except:
    print('erro a fazer post Schedule')

print('--------------------texte Schedule put---------------------')
try:
    url = "https://barbershoppi.herokuapp.com/schedule/"
    sta =dict(begin= '12:00',end='16:00', interval= 20,weekday=5,active=True , professional=1)
    for k in squedata:
        resposta = requests.put(url +str(k["id"])+'/', data= sta,headers=headers)
        print(str(k))
        print(resposta)
except:
    print('erro a fazer put Schedule')

print('--------------------texte Schedule delete---------------------')
try:
    url = "https://barbershoppi.herokuapp.com/Schedule/"
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
    url = "https://barbershoppi.herokuapp.com/appointment/"
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
    url = "https://barbershoppi.herokuapp.com/appointment/"
    sta = dict(appdate= '12/12/2001')
    for k in appodata:
        resposta = requests.patch(url +str(k["id"])+'/',data= sta ,headers=headers)
        print(resposta)
except:
    print('erro a fazer put Appointment')

print('--------------------texte Appointment delete---------------------')
try:
    url = "https://barbershoppi.herokuapp.com/appointment/"
    for t in appodata:
        print(str(t))
        d = requests.delete(url +str(t["id"])+'/',headers=headers)
        print(d)
except:
    print('erro a fazer post Appointment')
    print(d)       