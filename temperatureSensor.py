import Adafruit_DHT

tempSensor = Adafruit_DHT.DHT22
inputPin = 4

humidity, temperature = Adafruit_DHT.read_retry(tempSensor, inputPin)
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')