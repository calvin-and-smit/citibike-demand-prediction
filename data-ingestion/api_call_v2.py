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


station_info_url = 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json'
station_status_url = 'https://gbfs.citibikenyc.com/gbfs/en/station_status.json'
data = requests.get(url).json()
