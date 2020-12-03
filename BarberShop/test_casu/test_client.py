import json
import random
import requests

#metodo utilizado para obter token de acesso com localhost user=pedro senha=pedro098 
#metodo utilizado para obter token de acesso com heroku user=pedro senha=pedro098 
Token = requests.post('http://localhost:8000/login/',{'username':'pedro','password':'pedro098'})
te = Token.json()
headers={'Authorization': 'Bearer '+ te["access"]}

localdata=[]

class ClientViewSetTestCase():

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
