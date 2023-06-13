import machine
import time


class BrewLed:

    def __init__(self, pin_number):
        self.led_pin = machine.Pin(pin_number, machine.Pin.OUT)

    def on(self):
        self.led_pin.on()

    def off(self):
        self.led_pin.off()
