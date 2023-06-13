from machine import Pin


class BrewLed:

    led = ()

    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()
