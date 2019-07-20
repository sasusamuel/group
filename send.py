import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")
Connected = False  # global variable for the state of the connection

client = mqtt.Client()
client.on_connect = on_connect
client.connect("104.248.163.70", 1883, 60)
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)

try:
    topic = input("Where are you headed: ")
    while True:
        message = input('Your message: ')
        if message == "quit":
            topic = input("select new chartroom:")
        else:
            client.publish("KTU/ Nana Danso Abeam", message)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
