import requests
import os
import time


url = 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json'

data = requests.get(url).json()


for d in data.keys():
    print(d)
    
    
temp = data['data']['stations']

temp[1]
