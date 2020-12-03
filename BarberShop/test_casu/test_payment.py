import json
import random
import requests

#metodo utilizado para obter token de acesso com localhost user=pedro senha=pedro098 
#metodo utilizado para obter token de acesso com heroku user=pedro senha=pedro098 
Token = requests.post('http://localhost:8000/login/',{'username':'pedro','password':'pedro098'})
te = Token.json()
headers={'Authorization': 'Bearer '+ te["access"]}

localdata=[]


        print('--------------------texte Payment post---------------------')
        url = "http://localhost:8000/payment/"
        nomes = ["debito", "credito", "dinheiro"]
        for x in nomes:
            sta =dict(name = x,discount=random.randint(0,35),tax=random.randint(10,45) )
            pay = requests.post(url,data = sta,headers=headers)
            localdata.append (pay.json())
            print(str(pay.json()))
            
        print('--------------------texte Payment put---------------------')
        url = "http://localhost:8000/payment/"
        for k in localdata:
            resposta = requests.put(url +str(k["payment_id"])+'/',headers=headers)
            k['name'] = 'cancelado'
            print(str(k))

        print('--------------------texte Payment delete---------------------')
        url = "http://localhost:8000/payment/"
        for de in localdata:
            print(str(de))
            d = requests.delete(url +str(de["payment_id"])+'/',headers=headers)
