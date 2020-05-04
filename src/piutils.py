import Adafruit_DHT
from RPi import GPIO


class PiUtils(object):
    def __init__(self):
        self.dht_pin = 4
        self.relay_pin = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay_pin, GPIO.OUT)

    def get_ht_data(self, dht_type=11):
        """
        Function to get Humidity and temperature data from the specified DHT sensor
        :param dht_type: DHT 11 or DHT 22
        :return: Humidity & temperature
        """
        humidity, temp = Adafruit_DHT.read_retry(dht_type, self.dht_pin)
        return humidity, temp

    def control_relay_switch(self, enable=False):
        """
        Function to control the relay switch module by turning on or off
        :param enable: True - ON; False - OFF
        :return: None
        """
        if enable:
            GPIO.output(self.relay_pin, GPIO.LOW)
        else:
            GPIO.output(self.relay_pin, GPIO.HIGH)


