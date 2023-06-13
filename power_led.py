from machine import Pin, Timer
import utime


class PowerLed:

    led = ()

    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)
        self.timer = Timer()

    def on(self):
        self.led.on()

    def blink_callback(self, timer):
        self.led.toggle()

    def on_blink_finished(self):
        self.led.off()
        self.timer.deinit()

    def blink(self, count, interval, callback=None):
        self.timer.init(period=interval, mode=Timer.PERIODIC, callback=self.blink_callback)
        self.led.on()
        utime.sleep_ms(interval * count)
        self.on_blink_finished()
        if callback is not None:
            callback()

