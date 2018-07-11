import os
import time
import sys
import requests
import Adafruit_DHT
import json




url= 'http://demo.thingsboard.io:80/api/v1/ocnPO72ZrTtWXdwJT76A/telemetry'

headers= {
    'Content-Type': 'application/json'
}

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    data= {

            "humidity": str(humidity),
            "temperature": str(temperature)

        }
    response = requests.post(url, headers=headers, json=data)
    print response.status_code
    if response.status_code == 200:
        print('Data uploaded successfully')
    else:
        print('Failed to upload!')
