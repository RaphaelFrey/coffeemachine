import machine
import utime


class LedOn:
    def __init__(self, pin):
        self.led_pin = machine.Pin(pin, machine.Pin.OUT)
        self.timer = machine.Timer()

    def timer_interrupt_handler(self, timer):
        self.led_pin.toggle()  # LED-Zustand umkehren

    def blink(self, count, interval, callback=None):
        self.timer.init(period=interval, mode=machine.Timer.PERIODIC, callback=self.timer_interrupt_handler)
        utime.sleep_ms(interval * count)
        self.turn_off()
        if callback is not None:
            callback()

    def turn_off(self):
        self.timer.deinit()
        self.led_pin.off()

    def on(self):
        self.led_pin.on()
