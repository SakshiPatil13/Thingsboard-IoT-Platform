import os
import time
import sys
import requests
import json
import random   



url= 'http://demo.thingsboard.io:80/api/v1/GOiMiNByAFjT0f404ORz/telemetry'

headers= {
    'Content-Type': 'application/json'
}

while True:
    
    temperature = random.sample(range(30,38),1)     #Assign temperature one value between 30 to 38
    humidity = random.sample(range(13,17),1)    #Assign humidity one value between 13 to 17
   
    data= {

            "humidity": str(humidity[0]),
            "temperature": str(temperature[0])

        }
    
    response = requests.post(url, headers=headers, json=data)
    print response.status_code
    if response.status_code == 200:
        print('Data uploaded successfully')
    else:
        print('Failed to upload!')
    time.sleep(30)
