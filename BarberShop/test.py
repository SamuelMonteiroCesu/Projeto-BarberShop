import json,requests
import random
from validate_docbr import CPF
#metodo utilizado para obter token de acesso com localhost user=pedro senha=pedro098 
#metodo utilizado para obter token de acesso com heroku user=pedro senha=pedro098 
Token = requests.post('http://localhost:8000/login/',{'username':'pedro','password':'pedro098'})
te = Token.json()
headers={'Authorization': 'Bearer '+ te["access"]}

statsdata=[]
procedata=[]
paydata=[]
clientdata=[]


'''
print('--------------------texte status post---------------------')
endpoint_status = "http://localhost:8000/status/"
nomes = ["finalizado", "em andamento", "cancelado", "reagendado"]
for x in nomes:
    sta = dict(name=x)
    res = requests.post(endpoint_status,data = sta,headers=headers)
    statsdata.append(res.json())
    print(str(res.json()))
#print(resposta.text)
#print(resposta.status_code)


print('--------------------texte status put---------------------')
url = "http://localhost:8000/status/"
nomes = ["finalizado", "em andamento", "cancelado", "reagendado"]
sta = {'name': random.choice(nomes)}
for i in statsdata:
    resposta = requests.put(url +str(i["status_id"])+'/',headers=headers)
    i['name'] = 'refeito'
    print(str(i))
#print(resposta.status_code)

print('--------------------texte status delete---------------------')
url = "http://localhost:8000/status/"
for t in statsdata:
    print(str(t))
    d = requests.delete(url +str(t["status_id"])+'/',headers=headers)

print('--------------------texte Procedure post---------------------')
url = "http://localhost:8000/procedure/"
nomes = ["cortar", "barbear", "lavar", "pentear"]
for x in nomes:
    sta =dict(name=x,time = random.randint(1, 100),price=random.randint(0,50) )
    pro = requests.post(url,data = sta,headers=headers)
    procedata.append(pro.json())
    print(str(pro.json()))

print('--------------------texte Procedure put---------------------')
url  = "http://localhost:8000/procedure/"
for i in procedata:
    resposta = requests.put(url +str(i["procedure_id"])+'/',headers=headers)
    i['name'] = 'cancelado'
    print(str(i))

print('--------------------texte procedure delete---------------------')
url = "http://localhost:8000/procedure/"
for k in procedata:
    print(str(k))
    d = requests.delete(url +str(k["procedure_id"])+'/',headers=headers)

print('--------------------texte Payment post---------------------')
url = "http://localhost:8000/payment/"
nomes = ["debito", "credito", "dinheiro"]
for x in nomes:
    sta =dict(name = x,discount=random.randint(0,35),tax=random.randint(10,45) )
    pay = requests.post(url,data = sta,headers=headers)
    paydata.append (pay.json())
    print(str(pay.json()))
    
print('--------------------texte Payment put---------------------')
url = "http://localhost:8000/payment/"
for k in paydata:
    resposta = requests.put(url +str(k["payment_id"])+'/',headers=headers)
    k['name'] = 'cancelado'
    print(str(k))

print('--------------------texte Payment delete---------------------')
url = "http://localhost:8000/payment/"
for de in paydata:
    print(str(de))
    d = requests.delete(url +str(de["payment_id"])+'/',headers=headers)

'''
print('--------------------texte Client post---------------------')
url = "http://localhost:8000/client/"
cpf = CPF()
new_cpf_one = cpf.generate()
sta =dict(name="teste", birthday = "13/11/20", email= "teste@teste.com",
username= "88442624368", password = "pbkdf2_sha256$216000$ZcvhOJYkbZOs$Oc0wUmZRtaVNl0/G/n7hqEqQJnRGzNuwtp3aB+NUHak=")
res = requests.post(url,data = sta)
clientdata.append(res.json())
print(str(res))


print('--------------------texte client put---------------------')
url = "http://localhost:8000/client/"
for k in clientdata:
    resposta = requests.put(url +str(k["id"])+'/',headers=headers)
    k['is_staff'] = True
    print(str(k))

print('--------------------texte client delete---------------------')
url = "http://localhost:8000/client/"
for de in clientdata:
    print(str(de))
    d = requests.delete(url +str(de["id"])+'/',headers=headers)



