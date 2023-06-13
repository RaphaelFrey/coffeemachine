from machine import Pin


class Button:

    button = ()
    callback = ()

    def __init__(self, pin, callback):
        self.button = Pin(pin, Pin.IN, Pin.PULL_DOWN)
        self.callback = callback

    def listen_for_input(self):
        if self.button.value():
            self.callback()
