from django.test import TestCase
import unittest
from geradores import cpf
from validate_docbr import CPF
from rest_framework.response import Response

class test_cliente(unittest.TestCase)

   def create(self):
        cpf = CPF()
        client = Client()
        company = Company()
        try:
            company = Company.objects.get(company_id = 1)
            client = Client.objects.get(doc=request.data['doc'])
            return Response({'400: DUPLICATED *DOC* - CHECK PLEASE'})
        except:
                
                if str.isalpha(request.data['name']) == False:
                    return Response({'400: INVALID *NAME* - CHECK PLEASE'})
                if(cpf.validate(request.data['doc'])):
                    client.company_fk = company
                    client.doc = CPF
                    client.name = request.data['name']
                    client.email = request.data['email']
                    client.birthday = request.data['birthday']
                    client.phone = request.data['phone']
                    client.cellphone = request.data['cellphone']
                    client.zipcode = request.data['zipcode']
                    client.adress = request.data['adress']
                    client.number = request.data['number']
                    client.district = request.data['district']
                    client.city = request.data['city']
                    client.state = request.data['state']
                    client.obs = request.data['obs']
                    client.save()
                    return Response({'200: CLIENT CREATED'})
                else:
                    return Response({'400: INVALID *DOC* - CHECK PLEASE'})

    def cadastro(self)
        create(client_id = 1,company_fk = 1,name="teste",email = "xxx@XXX.com",)
     self.assertEqual(self.ClientViewSet,'200: CLIENT CREATED')