import machine


class Button:
    def __init__(self, pin, callback):
        self.button_pin = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.callback = callback

    def check_button(self):
        if self.button_pin.value() == 1:
            self.callback()

    def wait_for_button_press(self):
        while True:
            if self.button_pin.value() == 1:
                self.callback()
                break
