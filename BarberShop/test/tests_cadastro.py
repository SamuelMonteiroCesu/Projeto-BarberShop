from django.test import TestCase
import unittest
from geradores import cpf
from validate_docbr import CPF
from rest_framework.response import Response
from models import Client
class test_cliente(unittest.TestCase):
    def geracpf():
        def calcula_digito(digs):
            s = 0
            n = 0
            qtd = len(digs)
            for i in xrange(qtd):
                s += n[i] * (1+qtd-i)
                res = 11 - s % 11
            if res >= 10: return 0
            return res                                                                              
        n = [random.randrange(10) for i in xrange(9)]
        n.append(calcula_digito(n))
        n.append(calcula_digito(n))
        return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)

   def create(self):
        cpf = geracpf()
        client = Client()
        company = Company()
        x = datetime.datetime.now()
        try:
            company = Company.objects.get(company_id = 1)
            client = Client.objects.get(doc=request.data['doc'])
            return Response({'400: DUPLICATED *DOC* - CHECK PLEASE'})
        except:
                
                if str.isalpha(request.data['name']) == False:
                    return Response({'400: INVALID *NAME* - CHECK PLEASE'})
                if(cpf.validate(request.data['doc'])):

                    client.company_fk = company
                    client.doc = cpf
                    client.name ="pedro"
                    client.email = "xxx@xxx"
                    client.birthday = x
                    client.phone = "99999999"
                    client.cellphone = "439999999"
                    client.zipcode = "80555555"
                    client.adress ="98"
                    client.number = "23"
                    client.district = "parana"
                    client.city = "londrina"
                    client.state = "parana"
                    client.obs = "caralho"
                    client.save()
            return Response({'200: CLIENT CREATED'})
        else:
            return Response({'400: INVALID *DOC* - CHECK PLEASE'})

   def cadastro(self)
        
    self.assertEqual(self.create,'200: CLIENT CREATED')

