# -*- coding: utf-8 -*-

##############################################################################################################
### Authors: Smit Mehta
### Python:  Version 3.7.3
### Details: script to download citibike real-time data
### Notes:   Check documentation here: http://gbfs.citibikenyc.com/gbfs/gbfs.json
###                                    https://github.com/NABSA/gbfs/blob/master/gbfs.md
###          
##############################################################################################################

import os
import requests
import time
from influxdb import InfluxDBClient


def getdata(url):
    data = requests.get(url).json()
    return data


def parsedata(data):
    records = data['data']['stations']
    return records

station_info_url = 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json'
station_status_url = 'https://gbfs.citibikenyc.com/gbfs/en/station_status.json'


data_dump = getdata(station_status_url)
station_data = parsedata(data_dump)

for each_station in station_data:
    station_id = each_station['station_id']
    station_status = each_station['station_status']
    num_docks_available = each_station['num_docks_available']
    num_bikes_available = each_station['num_bikes_available']
    num_ebikes_available = each_station['num_ebikes_available']
    total_bikes_available = num_bikes_available + num_ebikes_available
    num_docks_disabled = each_station['num_docks_disabled']
    num_bikes_disabled = each_station['num_bikes_disabled']
    is_installed = each_station['is_installed']
    is_returning = each_station['is_returning']
    is_renting = each_station['is_renting']
    

