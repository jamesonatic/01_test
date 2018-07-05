from gpiozero import Button, LED

led = LED(18)
but = Button(21)

but.when_pressed = led.on()