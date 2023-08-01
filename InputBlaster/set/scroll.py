from uiautomator import Device
import sys

d = Device(sys.argv[1])

if sys.argv[2] == 'up':
    d(scrollable=True).scroll.vert.backward()
elif sys.argv[2] == 'down':
    d(scrollable=True).scroll.vert.forward()
else:
    print("error direction?")

