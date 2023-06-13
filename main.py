from power_led import PowerLed
from brew_led import BrewLed
from button import Button

power_led = PowerLed(1)
brew_led = BrewLed(0)
interval_in_ms = 500
count = 90


def on_blink_finished():
    power_led.on()
    brew_led.off()


def start_brewing():
    brew_led.on()
    power_led.blink(count, interval_in_ms, on_blink_finished)


button = Button(2, start_brewing)
power_led.on()
brew_led.off()

while True:
    button.list_for_input()
