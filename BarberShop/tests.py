import json
import random
from django.test import RequestFactory
from django.test import Client,TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import (APIClient, APIRequestFactory, APITestCase,
                                 force_authenticate)
from rest_framework_simplejwt import authentication
from validate_docbr import CPF

from .models import *
from .views import *


class statusViewSetTestCase(APITestCase):
    
    list_url = reverse("status-list")
    def setUp(self):

        self.username = 'test'
        self.password = 'test' 
        self.email = 'admin@mgmail.com'

        self.admin = User.objects.create_superuser(self.username, self.password, self.email)



    def test_status_autorizado(self):
        response = self.client.get(self.list_url)
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
    
    def test_status_nao_autorizado(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_status_post(self):
        for x in range(10):
            nomes = ["finalizado", "em andamento", "a ser feito", "cancelado"]
            data = {"name": random.choice(nomes)}
        response = self.client.post(self.list_url,data)
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)

    def test_status_put(self):
            self.client = APIClient()
            self.client.force_authenticate(user=self.admin)
            factory = APIRequestFactory()
            request = factory.put('/status/10/', {"status_id":20,"nome":"teste","active":True},format = 'json')
            response = self.client.get('/status/10/',format='json')
            #self.assertEqual(response.data, {'id': 4, 'username': 'lauren'})
            self.assertEqual(len(response.data), 1)

    def test_status_delete(self):
        #-detils faz pater de viewset e kwargs e key arguments equal a primery key
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)
        factory = APIRequestFactory()
        request = factory.delete('/status/10/')
        Response = self.client.get('/status/10/')
        self.assertAlmostEqual(Response.status_code, status.HTTP_404_NOT_FOUND)


class ProcedureViewSetTestCase(APITestCase):
    
    list_url = reverse("procedure-list")

    def setUp(self):
        self.username = 'test'
        self.password = 'test' 
        self.email = 'admin@mgmail.com'
        self.admin = User.objects.create_superuser(self.username, self.password, self.email)

    def test_procedure_autorizado(self):
        response = self.client.get(self.list_url)
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
    
    def test_procedure_nao_autorizado(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_procedure_post(self):
        for x in range(10):
            nomes = ["corte", "barba", "lavar", "pentear"]
            time = random.randint(0,50)
            price = random.uniform(1, 10)
            data = {"name": random.choice(nomes),"time":time,"price":price}
        response = self.client.post(self.list_url,data)
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
    
    def test_procedure_put(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)
        factory = APIRequestFactory()
        request = factory.put('/procedure/10/', {"procedure_id":1,"name":"teste","time":30,"price":15})
        response= self.client.get('/procedure/10/',format='json')
        self.assertEqual(len(response.data), 1)


    #-details faz parte de viewset e kwargs = key arguments equal a primery key
    def test_procedure_delete(self):
        self.client = APIClient() 
        self.client.force_authenticate(user=self.admin)
        factory = APIRequestFactory()
        request = factory.delete('/procedure/10/')
        Response = self.client.get('/procedure/10/')
        self.assertAlmostEqual(Response.status_code, status.HTTP_404_NOT_FOUND)

   


class PaymentViewSetTestCase(APITestCase):
        
    list_url = reverse("payment-list")

    def setUp(self):
        self.username = 'test'
        self.password = 'test' 
        self.email = 'admin@mgmail.com'
        self.admin = User.objects.create_superuser(self.username, self.password, self.email)

    def test_Payment_autorizado(self):
        response = self.client.get(self.list_url)
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
    
    def test_Payment_nao_autorizado(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_Payment_post(self):
        for x in range(10):
            nomes = ["debito", "credito", "dinheiro"]
            disconto = random.randint(0,35)
            data = {"name": random.choice(nomes),"discount":disconto,"tax":disconto}
        response = self.client.post(self.list_url,data)
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)

    def test_Payment_put(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)
        factory = APIRequestFactory()
        request = factory.put('/payment/10/', {"Payment_id":1,"name":"teste","discount":30,"tax":15})
        response= self.client.get('/payment/10/',format='json')
        self.assertEqual(len(response.data), 1)
        #self.assertEqual(json.loads(response.content),{"Payment_id":1,"name":"teste","discount":30,"tax":15})

#-details faz parte de viewset e kwargs = key arguments equal a primery key
    def test_Payment_delete(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)
        factory = APIRequestFactory()
        request = factory.delete('/payment/10/')
        Response = self.client.get('/payment/10/')
        self.assertAlmostEqual(Response.status_code, status.HTTP_404_NOT_FOUND)

class ClientViewSetTestCase(APITestCase):
        
   # list_url = reverse("client-list")
    def setUp(self):
        self.username = 'test'
        self.password = 'test' 
        self.email = 'admin@mgmail.com'
        self.admin = User.objects.create_superuser(self.username, self.password, self.email)

    def test_client_autorizado(self):
        response = self.client.get("/client/1/")
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
    
    def test_client_nao_autorizado(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/client/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_client_post(self):
        for x in range(10):
            cpf = CPF()
            new_cpf_one = cpf.generate()
            data = {"name": "TesteMask", "birthday": "07/06/90", "email": "teste@teste.com",
                "doc": new_cpf_one, "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}
        response = self.client.post('/client/',data)
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)

    def test_client_put(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)
        factory = APIRequestFactory()
        request = factory.put('/client/10/', {"name":"teste", "birthday": "25/07/90", "email": "teste@teste.com",})
        response= self.client.get('/client/10/',format='json')
        self.assertEqual(len(response.data), 1)

    def test_client_delete(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)
        factory = APIRequestFactory()
        request = factory.delete('/client/10/')
        Response = self.client.get('/client/10/')
        self.assertAlmostEqual(Response.status_code, status.HTTP_404_NOT_FOUND)

    #-details faz parte de viewset e kwargs = key arguments equal a primery key
'''
    def test_client_cpf_ja_cadastrado(self):
            for x in range(2):
                data = {"name": "TesteMask", "birthday": "07/06/90", "email": "teste@teste.com",
                    "doc": "459.511.030-88", "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}
            response = self.client.post('/client/',data)
            self.assertAlmostEqual(Response.status_code, status.HTTP_400_BAD_REQUEST)
'''