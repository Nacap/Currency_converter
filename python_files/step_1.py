import requests
import json
import datetime

resp = requests.get('http://api.fixer.io/latest').json()
print resp
#v= resp['rates']['USD']
today = datetime.date.today()
with open("currency_converter.csv", "w") as text_file:
    text_file.write('"id","on_date","from_currency","to_currency","rate"\n')
    for key,value in resp["rates"].iteritems():
         text_file.write('"null","%s","EUR","%s","%f"\n' % (today,key,value))
with open("currency_converter.csv","r") as text_file: 
    f=open("backup_file.csv", "a")
    f.write(text_file.read())


