import time                     #Import time module               
import paho.mqtt.client as mqtt #Import paho-MQTT module to use this otocol 
import json                     #Import json for formatting the data
import random                   #Import random to get random data

thingsBoardHost = 'demo.thingsboard.io'         #Remote host on which data will be uploaded         
accessToken = 'v51sdJOgGgkYZbda8tIE'            #Accss Token for authentication 

sensorData = {'temperature': 0, 'humidity': 0}  #Set Initial value of data as 0
client = mqtt.Client()#Create a MQTT Client Object

client.username_pw_set(accessToken)             #Set access token

# Connect to Thingsboard using default MQTT port and 60 seconds keepalive interval
client.connect(thingsBoardHost, 1883, 60)       
client.loop_start()                             #It is required to upload the data continuously

try:
    while True:
        temp = random.sample(range(30,38),1)     #Assign temperature one value between 30 to 38
        humid = random.sample(range(13,17),1)    #Assign humidity one value between 13 to 17
        temperature = temp[0]                    #Converting list into an integer value
        humidity = humid[0]                      #Converting list into an integer value
        
        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
        sensorData['temperature'] = temperature  #Fill the dataframe with temperature value
        sensorData['humidity'] = humidity        #Fill the dataframe with humid value
        
        #Sending(publishing) humidity and temperature data to Thingsboard in json format
        client.publish('v1/devices/me/telemetry', json.dumps(sensorData),1)

        time.sleep(2)     #Publish dataframe after every 2 sec

except KeyboardInterrupt: #Upload dataframe continuously until keyboard interrupt is generated
    pass                  #Do nothing

client.loop_stop()
client.disconnect()       #Disconnet from uploading process
