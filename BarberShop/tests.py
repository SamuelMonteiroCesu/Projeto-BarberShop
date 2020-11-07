import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .models import *
from .views import *
import random


class statusTestcase(APITestCase):
    def test_cadastro_status(self):
        for x in range(10):
            nomes = ["finalizado", "execucao", "a ser feito", "camselado"]
            data = {"name": random.choice(nomes)}
            response = self.client.post(
                "https://barbershoppi.herokuapp.com/status/", data, format='json')
            if Response.status_code == status.HTTP_200_OK:
                data = {"name": "status"}
                response = self.client.put(
                    "https://barbershoppi.herokuapp.com/status/51/", data, format='json')
                if Response.status_code == status.HTTP_200_OK:
                    response = self.client.delete(
                        "https://barbershoppi.herokuapp.com/status/50/", format='json')
                    if Response.status_code == status.HTTP_200_OK:
                        response = self.client.get('/status/51/')
                        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
    

class ProcedureTestcase(APITestCase):
    def test_cadastro_Procedure_CORRETO(self):
        for x in range(100):
            nomes =["corte","barbar","etc"]
            data = {"name": random.choice(nomes), "time": random.randint(0,100), "tax": random.randint(0,50)}
            response = self.client.post(
                "https://barbershoppi.herokuapp.com/procedure/", data, format='json')
            if Response.status_code == status.HTTP_200_OK:
                data = {"name": "teste procedimento"}
                response = self.client.put(
                    "https://barbershoppi.herokuapp.com/status/51/", data, format='json')
                if Response.status_code == status.HTTP_200_OK:
                    response = self.client.delete(
                        "https://barbershoppi.herokuapp.com/status/50/", format='json')
                    if Response.status_code == status.HTTP_200_OK:
                        response = self.client.get('/status/51/')
                        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)

#    def test_cadastro_Procedure_INCORRETO(self):
#        for x in range(100):
#            data = {"name":"testep rocedimento","time":"OLA","tax":"TESTE"}
#            response =self.client.post("https://barbershoppi.herokuapp.com/procedure/",data, format='json')
#            self.assertAlmostEqual(Response.status_code, status.HTTP_400_BAD_REQUEST)


#class PaymentTestcase(APITestCase):
 #   def test_cadastro_Payment(self):
  #      for x in range(100):
   #         data = {"name": "testep debito", "dscount": 15, "tax": 15}
    #        response = self.client.post(
     #           "https://barbershoppi.herokuapp.com/procedure/", data, format='json')
      #      self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)


#class clienteTestcase(APITestCase):
#
#    def test_cadastro_cliente(self):
#        #cpf = cpf_generate()
#        data = {"name": "TesteMask", "birthday": "07/06/90", "email": "teste@teste.com",
#                "doc": "459.511.030-88", "password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}
#        response = self.client.post(
#            "https://barbershoppi.herokuapp.com/client/", data, format='json')
#        self.assertAlmostEqual(Response.status_code, status.HTTP_200_OK)
#
    def test_cadastro_cliente_doc_existente(self):
        cpf = cpf_generate()
        data = {"name": "TesteMask","birthday": "07/06/90","email": "teste@teste.com",
        "doc":"cpf","password": "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak="}
        self.client.post("https://barbershoppi.herokuapp.com/client/",data, format='json')
        response =self.client.post("https://barbershoppi.herokuapp.com/client/",data, format='json')
        self.assertAlmostEqual(Response.status_code, status.HTTP_400_BAD_REQUEST)

    def cpf_generate():
        while True:
            cpf = [randint(0, 9) for i in range(9)]
            if cpf != cpf[::-1]:
                break
        for i in range(9, 11):
            value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            cpf.append(digit)
        result = ''.join(map(str, cpf))
        return result
