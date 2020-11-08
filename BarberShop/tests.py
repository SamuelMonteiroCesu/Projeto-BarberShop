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


class statusTestcase(APITestCase):
    def test_cadastro_status(self):
        for x in range(10):
            nomes = ["finalizado", "execucao", "a ser feito", "camselado"]
            data = {"name": random.choice(nomes)}
            self.client.post(
                "https://barbershoppi.herokuapp.com/status/", data, format='json')

    def test_status_put_delete_get(self):
        data = {"name": "status"}
        response = self.client.put(
            "https://barbershoppi.herokuapp.com/status/51/", data, format='json')
        if Response.status_code == status.HTTP_200_OK:
            response = self.client.delete(
                "https://barbershoppi.herokuapp.com/status/50/", format='json')
            if Response.status_code == status.HTTP_200_OK:
                response = self.client.get('/status/51/')
                self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)

class statusViewSetTestCase(APITestCase):
    
    list_url = reverse("status-list")
    url = reverse("status-detail", kwargs={"pk": 1})
    def setUp(self):
        self.user = User.objects.create_user(username="davinci",
                                             password="some-very-strong-psw")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        self.username = 'test'
        self.password = 'test' 
        self.email = 'admin@mgmail.com'

        self.admin = User.objects.create_superuser(self.username, self.password, self.email)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

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
            data = {"status_id":20,"name":"teste","active":True}
            Response = self.client.put("https://http://localhost:8000/status/7/",data,format='json')
            self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
            self.assertEqual(json.loads(response.content),{"status_id":20,"nome":"teste","active":True})  

    def test_status_delete(self):
        #-detils fz pater de viewset e kwargs e key arguments equal a primery key
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)
        Response = self.client.delete('/status/10/')
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)

      







class ProcedureViewSetTestCase(APITestCase):
    
    list_url = reverse("procedure-list")

    def setUp(self):
        self.user = User.objects.create_user(username="davinci",
                                             password="some-very-strong-psw")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.username = 'test'
        self.password = 'test' 
        self.email = 'admin@mgmail.com'

        self.admin = User.objects.create_superuser(self.username, self.password, self.email)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

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
        data = {'procedure_id':1,'name':'teste','time':30,'price':15}
        Response = self.client.put("https://barbershoppi.herokuapp.com/payment/5/",data, format='json'  )
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{"procedure_id":1,"name":"teste","time":30,"price":15})


    #-details faz parte de viewset e kwargs = key arguments equal a primery key
    def test_procedure_delete(self):
        url = reverse('procedure-detail', kwargs={'pk': 1})
        self.client = APIClient() 
        self.client.force_authenticate(user=self.admin)
        Response =self.cliente.delete(url)
        self.assertEqual(Response.status_code, status.HTTP_200_OK)

   



class PaymentViewSetTestCase(APITestCase):
        
    list_url = reverse("payment-list")

    def setUp(self):
        self.user = User.objects.create_user(username="davinci",
                                            password="some-very-strong-psw")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.username = 'test'
        self.password = 'test' 
        self.email = 'admin@mgmail.com'

        self.admin = User.objects.create_superuser(self.username, self.password, self.email)
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

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
        data = {"name":"teste","discount":30,"tax":15}
        Response = self.client.patch("https://barbershoppi.herokuapp.com/payment/5/",data, format='json')
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{"Payment_id":1,"name":"teste","discount":30,"tax":15})

#-details faz parte de viewset e kwargs = key arguments equal a primery key
    def test_Payment_delete(self):
        url = reverse('payment-detail', kwargs={'pk': 3})
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)
        Response = self.client.delete(url)
        self.assertEqual(Response.status_code, status.HTTP_200_OK)


class ClientViewSetTestCase(APITestCase):
        
#    list_url = reverse("Client-list")

    def setUp(self):
        self.user = User.objects.create_user(username="davinci",
                                            password="some-very-strong-psw")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.username = 'test'
        self.password = 'test' 
        self.email = 'admin@mgmail.com'

        self.admin = User.objects.create_superuser(self.username, self.password, self.email)
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_client_autorizado(self):
        response = self.client.get("https://barbershoppi.herokuapp.com/client/1/")
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
    
    def test_client_nao_autorizado(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("https://barbershoppi.herokuapp.com/client/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_client_post(self):
        for x in range(10):
            cpf = CPF()
            new_cpf_one = cpf.generate()
            data = {"name": "TesteMask", "birthday": "07/06/90", "email": "teste@teste.com",
                "doc": new_cpf_one, "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}
        response = self.client.post('https://barbershoppi.herokuapp.com/client/',data)
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)

    def test_client_cpf_ja_cadastrado(self):
            for x in range(2):
                data = {"name": "TesteMask", "birthday": "07/06/90", "email": "teste@teste.com",
                    "doc": "459.511.030-88", "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}
            response = self.client.post(self.list_url,data)
            self.assertAlmostEqual(Response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_client_put(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)
        data = {"name":"teste", "birthday": "25/07/90", "email": "teste@teste.com",}
        Response = self.client.patch("https://barbershoppi.herokuapp.com/client/5/",data, format='json')
        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)

#-details faz parte de viewset e kwargs = key arguments equal a primery key
    def test_client_delete(self):
        url = reverse('cliente-detail', kwargs={'pk': 3})
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)
        Response = self.client.delete(url)
        self.assertEqual(Response.status_code, status.HTTP_200_OK)