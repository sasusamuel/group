import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("connected with result code "+str(rc))
	# Here you can subscribe to whatever topics you like
	# use '#' for a 'wildcard' - subscribe to any messages
	client.subscribe("glblcd/sam")

def on_message(client, userdata, msg):
	print(msg.topic + " \n " + msg.playload.decode("utf-8") + " \n ")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("104.248.163.70", 1883, 60)

client.loop_forever()

