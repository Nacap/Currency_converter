#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

with open("inputfile.txt", 'r') as input_file:
    values = input_file.read()

resp = requests.get('http://api.fixer.io/latest').json()
print resp
output_values = list()
for value in values.split(','):
    result = resp['rates']['USD'] * int(value)
    output_values.append(str(result))

with open("outputfile.txt","w") as output_file:
    output_file.write('\n'.join(output_values))
	



