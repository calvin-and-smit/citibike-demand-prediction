import requests
import os
import time


url = 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json'

data = requests.get(url).json()


for d in data.keys():
    print(d)
    
    
temp = data['data']['stations']

print(temp[1])




# plan:
# create a single ingestion script - execute it multiple times throughout the day using some form of scheduler
# Host everything on AWS!!!
#


##
## script struct:
## functions : request data, 
##             modify the struct of data,
##             push into mongodb (/Redshift????)
