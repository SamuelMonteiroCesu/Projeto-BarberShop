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

#username=pedrao password=2306star
class acessoTestCase(APITestCase):

    def test_acesso_permitido(self):

        Token = requests.post('http://localhost:8000/login/',{'username':'pedrao','password':'2306star'})
        te = Token.json()
        endpoint_status = "http://localhost:8000/status/"
        headers={'Authorization': 'Bearer '+ te["access"]}

        res = requests.get(endpoint_status,headers=headers)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_acesso_negado(self):
        Token = requests.post('http://localhost:8000/login/',{'username':'','password':'2306star'})
        te = Token.json()
        endpoint_status = "http://localhost:8000/status/"
        headers={'Authorization': 'Bearer '+ te["access"]}
        res = requests.get(endpoint_status,headers=headers)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)



class statusViewSetTestCase(APITestCase):

    def test_status_apost(self):
        Token = requests.post('http://localhost:8000/login/',{'username':'pedrao','password':'2306star'})
        te = Token.json()
        print('--------------------texte status post---------------------')
        endpoint_status = "http://localhost:8000/status/"
        headers={'Authorization': 'Bearer '+ te["access"]}
        
        nomes = ["finalizado", "em andamento", "cancelado", "reagendado"]
        sta = {'name': random.choice(nomes),'active':random.getrandbits(1)}
        for x in range (20):
            res = requests.post(endpoint_status,data = sta,headers=headers)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        #print(resposta.text)
        #print(resposta.status_code)


    def test_status_bput(self):
        Token = requests.post('http://localhost:8000/login/',{'username':'pedrao','password':'2306star'})
        te = Token.json()
        print('--------------------texte status put---------------------')
        endpoint_status = "http://localhost:8000/status/"
        headers={'Authorization': 'Bearer '+ te["access"]}
        nomes = ["finalizado", "em andamento", "cancelado", "reagendado"]
        sta = {'name': random.choice(nomes),'active':random.getrandbits(1)}
        tamanho = requests.get(endpoint_status,headers=headers)
        tama = tamanho.json()
        t = len(tama) - 15
        rev_tama = range(t,len(tama))
        for x in rev_tama:
            resposta = requests.put(endpoint_status +str(x)+'/' ,data = sta,headers=headers)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        #print(resposta.text)
        #print(resposta.status_code)

    def test_status_delete(self):
        Token = requests.post('http://localhost:8000/login/',{'username':'pedrao','password':'2306star'})
        te = Token.json()
        print('--------------------texte status delete---------------------')
        endpoint_status = "http://localhost:8000/status/"
        headers={'Authorization': 'Bearer '+ te["access"]}
        tamanho = requests.get(endpoint_status,headers=headers)
        tama = tamanho.json()
        t = len(tama) - 15
        rev_tama = range(t,len(tama))
        for x in rev_tama:
            r = requests.delete(endpoint_status +str(x)+'/',headers=headers)
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)





class ProcedureViewSetTestCase(APITestCase):

    def test_Procedure_apost(self):
        Token = requests.post('http://localhost:8000/login/',{'username':'pedrao','password':'2306star'})
        te = Token.json()
        print('--------------------texte Procedure post---------------------')
        endpoint_procedure = "http://localhost:8000/procedure/"
        headers={'Authorization': 'Bearer '+ te["access"]}
        
        nomes = ["corte", "barba", "lavar", "pentear"]
        data = {"name": random.choice(nomes),"time":random.randint(1, 100),"price":random.randint(0,50)}
        for x in range (20):
            res = requests.post(endpoint_procedure ,data = data,headers=headers)
            
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        #print(res.text)
        #print(res.status_code)

    def test_procedure_bput(self):
        Token = requests.post('http://localhost:8000/login/',{'username':'pedrao','password':'2306star'})
        te = Token.json()
        print('--------------------texte Procedure put---------------------')
        endpoint_procedure  = "http://localhost:8000/procedure/"
        headers={'Authorization': 'Bearer '+ te["access"]}

        nomes = ["corte", "barba", "lavar", "pentear"]
        data = {"name": random.choice(nomes),"time":random.randint(1, 100),"price":random.randint(0,50)}

        tamanho = requests.get(endpoint_procedure,headers=headers)
        tama = tamanho.json()
        t = len(tama) - 15
        rev_tama = range(t,len(tama)) 
        for x in rev_tama:
            resposta = requests.put(endpoint_procedure+str(x)+'/' ,data = data,headers=headers)

        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        print(resposta.text)
        print(resposta.status_code)

        
    def test_procedure_delete(self):
        Token = requests.post('http://localhost:8000/login/',{'username':'pedrao','password':'2306star'})
        te = Token.json()
        print('--------------------texte procedure delete---------------------')
        endpoint_procedure = "http://localhost:8000/procedure/"
        headers={'Authorization': 'Bearer '+ te["access"]}
        tamanho = requests.get(endpoint_procedure,headers=headers)
        tama = tamanho.json()
        t = len(tama) - 15
        rev_tama = range(t,len(tama))
        for x in rev_tama:
            r = requests.delete(endpoint_procedure +str(x)+'/',headers=headers)
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)

class PaymentViewSetTestCase(APITestCase):

    def test_status_apost(self):
        Token = requests.post('http://localhost:8000/login/',{'username':'pedrao','password':'2306star'})
        te = Token.json()

        print('--------------------texte Payment post---------------------')
        endpoint_Payment = "http://localhost:8000/payment/"
        headers={'Authorization': 'Bearer '+ te["access"]}

        nomes = ["debito", "credito", "dinheiro"]
        disconto = random.randint(0,35)
        data = {"name": random.choice(nomes),"discount":disconto,"tax":disconto}

        for x in range (20):
            res = requests.post(endpoint_Payment,data = data,headers=headers)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        #print(res.text)
        #print(res.status_code)


    def test_Payment_bput(self):
        Token = requests.post('http://localhost:8000/login/',{'username':'pedrao','password':'2306star'})
        te = Token.json()

        print('--------------------texte Payment put---------------------')
        endpoint_Payment = "http://localhost:8000/payment/"
        headers={'Authorization': 'Bearer '+ te["access"]}

        nomes = ["debito", "credito", "dinheiro"]
        disconto = random.randint(0,35)
        data = {"name": random.choice(nomes),"discount":disconto,"tax":disconto}

        tamanho = requests.get(endpoint_Payment,headers=headers)
        tama = tamanho.json()
        t = len(tama) - 15
        rev_tama = range(t,len(tama))
        for x in rev_tama:
            resposta = requests.put(endpoint_Payment  +str(x)+'/' ,data = data,headers=headers)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        #print(resposta.text)
        #print(resposta.status_code)

    def test_status_delete(self):
        Token = requests.post('http://localhost:8000/login/',{'username':'pedrao','password':'2306star'})
        te = Token.json()

        print('--------------------texte Payment delete---------------------')
        endpoint_Payment = "http://localhost:8000/payment/"
        headers={'Authorization': 'Bearer '+ te["access"]}

        tamanho = requests.get(endpoint_Payment,headers=headers)
        tama = tamanho.json()
        t = len(tama) - 15
        rev_tama = range(t,len(tama))
        for x in rev_tama:
            r = requests.delete(endpoint_Payment +str(x)+'/',headers=headers)
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)

class ClintViewSetTestCase(APITestCase):

    def test_status_apost(self):

        print('--------------------texte client post---------------------')
        endpoint_client = "http://localhost:8000/client/"

        cpf = CPF()
        new_cpf_one = cpf.generate()
        data = {"name": "TesteMask", "birthday": "07/06/90", "email": "teste@teste.com",
        "doc": new_cpf_one, "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}

        for x in range (20):
            res = requests.post(endpoint_client,data = data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        #print(res.text)
        #print(res.status_code)


    def test_Payment_bput(self):
        print('--------------------texte client put---------------------')
        endpoint_client = "http://localhost:8000/client/"
            
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
            data = {"name": "Teste", "birthday": "01/01/20", "email": "teste@teste.com",
            "doc": new_cpf_one, "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}

            resposta = requests.put(endpoint_client  +str(x)+'/' ,data = data,headers=headers)
        self.assertEqual(resposta.status_code, status.HTTP_200_OK)
        #print(resposta.text)
        #print(resposta.status_code)

    def test_status_delete(self):
        print('--------------------texte client delete---------------------')
        endpoint_client = "http://localhost:8000/client/"
            
        tamanho = requests.get(endpoint_client)
        tama = tamanho.json()
        t = len(tama) - 15
        rev_tama = range(t,len(tama))
        for x in rev_tama:
            r = requests.delete(endpoint_client +str(x)+'/')
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)