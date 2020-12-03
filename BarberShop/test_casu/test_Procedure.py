import json
import random
import requests

#metodo utilizado para obter token de acesso com localhost user=pedro senha=pedro098 
#metodo utilizado para obter token de acesso com heroku user=pedro senha=pedro098 
Token = requests.post('http://localhost:8000/login/',{'username':'pedro','password':'pedro098'})
te = Token.json()
headers={'Authorization': 'Bearer '+ te["access"]}

localdata=[]

        print('--------------------texte Procedure post---------------------')
        url = "http://localhost:8000/procedure/"
        nomes = ["cortar", "barbear", "lavar", "pentear"]
        for x in nomes:
            sta =dict(name=x,time = random.randint(1, 100),price=random.randint(0,50) )
            pro = requests.post(url,data = sta,headers=headers)
            localdata.append(pro.json())
            print(str(pro.json()))

        print('--------------------texte Procedure put---------------------')
        url  = "http://localhost:8000/procedure/"
        for k in localdata:
            resposta = requests.put(url +str(k["procedure_id"])+'/',headers=headers)
            k['name'] = 'cancelado'
            print(str(k))

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
