dicionario = {}
dicionario['fatec'] = 'Fatec Araras'
dicionario['rafel'] = ['Etec','Fatec']
import json
objeto = json.dumps(dicionario,indent=4)
import requests
URL = 'https://api.disneyapi.dev/character'