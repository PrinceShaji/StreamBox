
import threading, time
from random import randint


def flashLed(e, t):
    """flash the specified led every 2 second"""
    while not e.isSet():
        print('leds on')
        time.sleep(0.5)
        event_is_set = e.wait(t)
        if event_is_set:
            print('stop led from flashing')
            break
        else:
            print('leds off')
            time.sleep(1.5)

#colour = "red"
e = threading.Event()
t = threading.Thread(name='non-block', target=flashLed, args=(e, 1))
t.start()

print('recording started')
for i in range(0, 10):
    print('recording ...')
    time.sleep(10)
print('recording finished')
e.set()
exit()
