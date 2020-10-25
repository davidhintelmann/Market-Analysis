import quandl
import json
import matplotlib.pyplot as plt

with open('../quandl.json') as file:
    json = json.load(file)
    api_key = json['api_key']

quandl.ApiConfig.api_key = api_key

quandl.get('LBMA/GOLD', start_date='2010-01-01')
