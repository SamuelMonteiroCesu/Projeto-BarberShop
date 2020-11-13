import requests
#GET SEM TOKEN -----------------------------------------------------------------------------------
apis = ['procedure','payment','status','client']
print('------ TESTE GET SEM TOKEN -------')
for j in apis:
    url = 'http://barbershoppi.herokuapp.com/' + j + "/"
    r = requests.get(url)  #request para pegar todos os dados
    if r.status_code == 200:
        print(j + " -- OK -- " + str(r.json()))
    else:
        print(j + " -- ERRO -- " + str(r.json()))
print()

#GET COM TOKEN -----------------------------------------------------------------------------------

user = dict(username='38044418822', password='11051991') # objeto no formato dict para passar login e senha
r = requests.post('http://barbershoppi.herokuapp.com/login/', data=user) #com o usuario criado para pegar o token
x = r.json() #recebendo os dados da request
access = "Bearer "+x['access'] # salvando o token em uma variavel com o nome "bearer"
refresh = x['refresh'] #Salvando o token refresh em uma variavel
headers = dict(Authorization=access) #Colocando o token no header.authorization
print('------ TESTE GET COM TOKEN -------')
for j in apis:
    url = 'http://barbershoppi.herokuapp.com/' + j + "/"
    r = requests.get(url,headers=headers)  #request para pegar todos os dados
    if r.status_code == 200:
        print("\n" + j + " -- OK -- " + str(r.json()))
    else:
        print("\n" + j + " -- ERRO -- " + str(r.json()))
print()

#LOGINS -----------------------------------------------------------------------------------

print('------ TESTE LOGIN USUARIO INVALIDO -------')
user = dict(username='38044418822', password='11051990') # objeto no formato dict para passar login e senha
r = requests.post('http://barbershoppi.herokuapp.com/login/', data=user) #com o usuario criado para pegar o token
if r.status_code == 200:
    print(str(user) + " -- OK -- " + str(r.json()))
else:
    print(str(user) + " -- ERRO -- " + str(r.json()))
print()
print('------ TESTE LOGIN USUARIO VALIDO -------')
user = dict(username='38044418822', password='11051991') # objeto no formato dict para passar login e senha
r = requests.post('http://barbershoppi.herokuapp.com/login/', data=user) #com o usuario criado para pegar o token
if r.status_code == 200:
    print(str(user) + " -- OK -- " + str(r.json()))
else:
    print(str(user) + " -- ERRO -- " + str(r.json()))
print()
input('PRESIONE ENTER PARA CONTINUAR. =========== POSTS ===========')
# POST SEM TOKEN -----------------------------------------------------------------------------------
print('------ TESTE POST SEM TOKEN -------')
apis = ['procedure','payment','status']
nomes = ['-testAUTO-01','-testAUTO-02']
for j in apis:
    url = 'http://barbershoppi.herokuapp.com/' + j + "/"
    for i in nomes:
        data = dict(name = j+i)
        r = requests.post(url,data = data)  #request para pegar todos os dados
        if r.status_code == 201:
            print(j+ " " +str(data) + " -- OK -- " + str(r.json()))
        else:
            print(j+ " " +str(data) + " -- ERRO -- " + str(r.json()))
print()

# POST SEM TOKEN -----------------------------------------------------------------------------------
apis = ['procedure','payment','status']
nomes = ['-testAUTO-01','-testAUTO-02']
for j in apis:
    localdata = []
    print('------ TESTE POST COM TOKEN ------- ' + j + ' ------- ')
    url = 'http://barbershoppi.herokuapp.com/' + j + "/"
    for i in nomes:
        if j == "procedure":
            data = dict(name = j+i,time = 10, price = 20)
        if j == "status":
            data = dict(name = j+i)
        if j == "payment":
            data = dict(name=j + i, discount=10, tax=20)
        r = requests.post(url,data = data, headers = headers)  #request para pegar todos os dados
        if r.status_code == 201:
            print(j+ " " +str(data) + " -- OK -- " + str(r.json()))
            localdata.append(r.json())
        else:
            print(j+ " " +str(data) + " -- ERRO -- " + str(r.json()))

# PUT COM TOKEN -----------------------------------------------------------------------------------
    input('\nPRESIONE ENTER PARA CONTINUAR. =========== PUT ===========\n')
    for k in localdata:
        url = 'http://barbershoppi.herokuapp.com/' + j + '/' + str(k[str(j + "_id")]) + "/"  # concatenação de valores.
        k['name'] += "--UPDATED--"
        r = requests.put(url, headers=headers, data=k)
        if r.status_code == 200:
            print(j+ " " +str(data) + " -- UPDATED -- " + str(r.json()))
        else:
            print(j+ " " +str(data) + " -- ERRO -- " + str(r.json()))

# DELETE COM TOKEN -----------------------------------------------------------------------------------
    input('\nPRESIONE ENTER PARA CONTINUAR. =========== DELETE ===========')
    for l in localdata:
        url = 'http://barbershoppi.herokuapp.com/' + j + '/' + str(l[str(j + "_id")]) + "/"  # concatenação de valores.
        r = requests.delete(url, headers=headers)
        if r.status_code == 204:
            print(j+ " -- DELETED -- " + str(l))
        else:
            print(j+ " -- ERRO -- " + str(l))
    input('\nPRESIONE ENTER PARA OS PRÓXIMO POST.')


input("\n                            FIM PRESSIONE ENTER PARA SAIR!!!!")







'''
import json
import random
import requests
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import (APIClient, APIRequestFactory, APITestCase,
                                 force_authenticate)
from rest_framework_simplejwt import authentication
from validate_docbr import CPF

from .models import *
from .views import *
#metodo utilizado para obter token de acesso com localhost user=pedro senha=pedro098 
#metodo utilizado para obter token de acesso com heroku user=pedro senha=pedro098 
Token = requests.post('http://localhost:8000/login/',{'username':'pedro','password':'pedro098'})
te = Token.json()
headers={'Authorization': 'Bearer '+ te["access"]}

localdata=[]

#username=pedrao password=2306star
class acessoTestCase(APITestCase):

    def test_acesso_permitido(self):
        print('--------------------texte acesso permitido---------------------')
        print (Token.text)
        endpoint_status = "http://localhost:8000/status/95/"
        
        res = requests.get(endpoint_status,headers=headers)
        print(res.text)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_acesso_negado(self):
        print('--------------------texte acesso negado---------------------')
        endpoint_status = "http://localhost:8000/status/"
        res = requests.get(endpoint_status)
        print(res.text)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)



class statusViewSetTestCase(APITestCase):

    def test_status_apost(self):
        print('--------------------texte status post---------------------')
        endpoint_status = "http://localhost:8000/status/"
        nomes = ["finalizado", "em andamento", "cancelado", "reagendado"]
        for x in nomes:
            sta =dict(name=x)
            res = requests.post(endpoint_status,data = sta,headers=headers)
            localdata.append(res.json())
            print(str(res.json()))
        #print(resposta.text)
        #print(resposta.status_code)


    def test_status_bput(self):
        print('--------------------texte status put---------------------')
        url = "http://localhost:8000/status/"
        nomes = ["finalizado", "em andamento", "cancelado", "reagendado"]
        sta = {'name': random.choice(nomes)}
        for i in localdata:
            resposta = requests.put(url +str(i["status_id"])+'/',headers=headers)
            i['name'] = 'refeito'
            print(str(i))
        #print(resposta.status_code)


    def test_status_delete(self):
        print('--------------------texte status delete---------------------')
        url = "http://localhost:8000/status/"
        for t in localdata:
            print(str(t))
            d = requests.delete(url +str(t["status_id"])+'/',headers=headers)
            



class ProcedureViewSetTestCase(APITestCase):

    def test_Procedure_apost(self):

        print('--------------------texte Procedure post---------------------')
        url = "http://localhost:8000/procedure/"
        nomes = ["cortar", "barbear", "lavar", "pentear"]
        for x in nomes:
            sta =dict(name=x,time = random.randint(1, 100),price=random.randint(0,50) )
            pro = requests.post(url,data = sta,headers=headers)
            localdata.append(pro.json())
            print(str(pro.json()))


    def test_procedure_bput(self):

        print('--------------------texte Procedure put---------------------')
        url  = "http://localhost:8000/procedure/"
        for k in localdata:
            resposta = requests.put(url +str(k["procedure_id"])+'/',headers=headers)
            k['name'] = 'cancelado'
            print(str(k))


    def test_procedure_delete(self):
        print('--------------------texte procedure delete---------------------')
        url = "http://localhost:8000/procedure/"
        for k in localdata:
            print(str(k))
            d = requests.delete(url +str(k["procedure_id"])+'/',headers=headers)

class PaymentViewSetTestCase(APITestCase):

    def test_Payment_apost(self):
        print('--------------------texte Payment post---------------------')
        url = "http://localhost:8000/payment/"
        nomes = ["debito", "credito", "dinheiro"]
        for x in nomes:
            sta =dict(name = x,discount=random.randint(0,35),tax=random.randint(10,45) )
            pay = requests.post(url,data = sta,headers=headers)
            localdata.append (pay.json())
            print(str(pay.json()))
            
 
    def test_Payment_bput(self):
        print('--------------------texte Payment put---------------------')
        url = "http://localhost:8000/payment/"
        for k in localdata:
            resposta = requests.put(url +str(k["payment_id"])+'/',headers=headers)
            k['name'] = 'cancelado'
            print(str(k))

    def test_payment_delete(self):

        print('--------------------texte Payment delete---------------------')
        url = "http://localhost:8000/payment/"
        for de in localdata:
            print(str(de))
            d = requests.delete(url +str(de["payment_id"])+'/',headers=headers)

  
class ClientViewSetTestCase(APITestCase):

    def test_Client_apost(self):
        print('--------------------texte client post---------------------')
        endpoint_client = "http://localhost:8000/client/"
        nomes = ["pedro", "felipe", "lucas", "chaves"]
        cpf = CPF()
        new_cpf_one = cpf.generate()
        for x in nomes:
            sta =dict(name=x, birthday = "13/11/20", email= "teste@teste.com",
            doc= new_cpf_one, password = "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak=")
            res = requests.post(endpoint_client,data = sta,headers=headers)
            localdata.append(res.json())
            print(str(res.json()))

        #print(res.text)
        #print(res.status_code)

    def test_Client_bput(self):
        print('--------------------texte client put---------------------')
        endpoint_client = "http://localhost:8000/client/"
        for k in localdata:
            resposta = requests.put(url +str(k["client_id"])+'/',headers=headers)
            k['name'] = 'cancelado'
            print(str(k))
        cpf = CPF()
        new_cpf_one = cpf.generate()
        data = {"name": "Teste", "birthday": "01/01/20", "email": "teste@teste.com",
        "doc": new_cpf_one, "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}
        for k in localdata:
            resposta = requests.put(url +str(k["payment_id"])+'/',headers=headers)
            k['name'] = 'federico'
            print(str(k))

    def test_Client_delete(self):
        print('--------------------texte client delete---------------------')
        url = "http://localhost:8000/client/"
        for de in localdata:
            print(str(de))
            d = requests.delete(url +str(de["client_id"])+'/',headers=headers)
'''
