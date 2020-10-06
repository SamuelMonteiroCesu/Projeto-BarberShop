   from validate_docbr import CPF
from rest_framework.response import Response
from models import Client

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
                    client.doc = request.data['doc']
                    client.name = request.data['name']
                    client.email = request.data['email']
                    client.birthday = request.data['birthday']
                    client.phone = request.data['phone']
                    client.cellphone = request.data['cellphone']
                    client.zipcode = request.data['zipcode']
                    client.adress = request.data['adress']
                    client.number = request.data['number']
                    client.district = request.data['district']
                    client.complement = request.data['complement']
                    client.city = request.data['city']
                    client.state = request.data['state']
                    client.obs = request.data['obs']
                    client.save()
                    return Response({'200: CLIENT CREATED'})
                else:
                    return Response({'400: INVALID *DOC* - CHECK PLEASE'})
