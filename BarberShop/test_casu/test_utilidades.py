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
class acessoTestCase():

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



class statusViewSetTestCase():

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
            



class ProcedureViewSetTestCase():

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

class PaymentViewSetTestCase():

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

      
'''
class ClientViewSetTestCase(APITestCase):

    def test_Client_apost(self):
        Token = requests.post('https://barbershoppi.herokuapp.com/login/',{'username':'38044418822','password':'11051991'})
        te = Token.json()
        headers={'Authorization': 'Bearer '+ te['access']}
        print('--------------------texte client post---------------------')
        endpoint_client = "https://barbershoppi.herokuapp.com/client/"

        cpf = CPF()
        new_cpf_one = cpf.generate()
        data = {"name": "TesteMask", "birthday": "13/11/20", "email": "teste@teste.com",
        "doc": new_cpf_one, "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}

        for x in range (20):
            res = requests.post(endpoint_client,data = data,headers=headers)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        #print(res.text)
        #print(res.status_code)

    def test_Client_bput(self):
        print('--------------------texte client put---------------------')
        endpoint_client = "https://barbershoppi.herokuapp.com/client/"
            
        cpf = CPF()
        new_cpf_one = cpf.generate()
        data = {"name": "Teste", "birthday": "01/01/20", "email": "teste@teste.com",
        "doc": new_cpf_one, "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}
        tamanho = requests.get(endpoint_client,headers=headers)
        tama = tamanho.json()
        t = len(tama) - 15
        rev_tama = range(t,len(tama))
        for x in rev_tama:
            cpf = CPF()
            new_cpf_one = cpf.generate()
            data = {"first_name": "Teste", "last_name": "01/01/20", "email": "teste@teste.com",
            "username": new_cpf_one, "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}

            resposta = requests.put(endpoint_client  +str(x)+'/' ,data = data,headers=headers)
            
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        #print(resposta.text)
        #print(resposta.status_code)

    def test_Client_delete(self):
        print('--------------------texte client delete---------------------')
        tamanho = requests.get(endpoint_client)
        tama = tamanho.json()
        t = len(tama) - 15
        rev_tama = range(t,len(tama))
        for x in rev_tama:
            r = requests.delete(endpoint_client +str(x)+'/',headers=headers)
          
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT) 
'''