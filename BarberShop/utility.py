from datetime import *
import smtplib
from email.mime.text import MIMEText


class Time:

    def convertehora(self, hora):
        return  (timedelta(hours=int(hora[0:2]), minutes=int(hora[3:])))

    #schedule = dict(begin='08:00', end='18:00', interval='60')    #busy = ['15:00', '09:00', '18:00']
    #schedule espera um dict com begin end e interval e busy espera uma lista
    def FreeSchedule(self, schedule, busy):
        busylist = list(busy)
        begin = timedelta(hours=int(schedule['begin'].split(':')[0]),minutes=int(schedule['begin'].split(':')[1]))
        end = timedelta(hours=int(schedule['end'].split(':')[0]),minutes=int(schedule['end'].split(':')[1]))
        interval = timedelta(minutes=int(schedule['interval']))
        free = []

        for i in range(len(busy)):
            busy[i] = timedelta(hours=int(busy[i][0:2]), minutes=int(busy[i][4:6]))

        while begin <= end:
            if begin not in busy:
                aux = str(begin).split(':')[0]+":"+str(begin).split(':')[1]
                if len(aux) == 4:
                    aux = "0"+aux
                free.append(aux)
            begin+=interval
        busy = list(busylist)
        return (free)

class Emails:
    #3 strings email assunto e conteudo
    def sendmails(self, receiver, subject, content):
        fromx = 'barbeariaebenezerlondrina@gmail.com'
        pwd = 'barbershop'
        to  = receiver
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = fromx
        msg['To'] = to
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        try:
            server.login(fromx, pwd)
            server.sendmail(fromx, to, msg.as_string())
            server.quit()
            return(True)
        except:
            return (False)


class Users:
    def selfuser(self,id):
        pass
