from led_on import LedOn
from brew_led import BrewLed
from button import Button

on_led = LedOn(1)
brew_led = BrewLed(0)

def finished_brewing():
    brew_led.off()
    on_led.on()

def start_brewing():
    brew_led.on()
    on_led.blink(90, 500, callback=brew_led.off)


start_brewing()
