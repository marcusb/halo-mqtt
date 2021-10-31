import paho.mqtt.client as mqtt
from playsound import playsound
import time

MIN_WAIT = 15
last_play = 0


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("hallomotion/motion")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  global last_play
  # print(msg.topic + " " + str(msg.payload))
  if msg.payload.decode() == "ON":
    print("motion detected")
    now = time.time()
    if now - last_play > MIN_WAIT:
      last_play = now
      playsound('/usr/share/sounds/Oxygen-Window-Shade-Up.ogg')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("user", "pw")
client.connect("habpi", 1883, 60)
client.loop_forever()
