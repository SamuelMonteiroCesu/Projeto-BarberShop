import json,requests
import random

#metodo utilizado para obter token de acesso com localhost user=pedro senha=pedro098 
#metodo utilizado para obter token de acesso com heroku user=pedro senha=pedro098 
Token = requests.post('http://localhost:8000/login/',{'username':'pedro','password':'pedro098'})
te = Token.json()
headers={'Authorization': 'Bearer '+ te["access"]}

localdata=[]

print('--------------------texte status post---------------------')
endpoint_status = "http://localhost:8000/status/"
nomes = ["finalizado", "em andamento", "cancelado", "reagendado"]
for x in nomes:
    sta = dict(name=x)
    res = requests.post(endpoint_status,data = sta,headers=headers)
    localdata.append(res.json())
    print(str(res.json()))
#print(resposta.text)
#print(resposta.status_code)


print('--------------------texte status put---------------------')
url = "http://localhost:8000/status/"
nomes = ["finalizado", "em andamento", "cancelado", "reagendado"]
sta = {'name': random.choice(nomes)}
for i in localdata:
    resposta = requests.put(url +str(i["status_id"])+'/',headers=headers)
    i['name'] = 'refeito'
    print(str(i))
#print(resposta.status_code)

print('--------------------texte status delete---------------------')
url = "http://localhost:8000/status/"
for t in localdata:
    print(str(t))
    d = requests.delete(url +str(t["status_id"])+'/',headers=headers)
            