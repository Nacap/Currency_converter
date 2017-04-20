import requests
import json

response=requests.get ('http://api.fixer.io/latest').json()
print response
value = float(raw_input("Please enter a value in EUR that you whant to convert to USD: \n"))
result= response['rates']['USD']*value
print 'That is %f USD' % result

