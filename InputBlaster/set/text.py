from uiautomator import Device
import sys

d = Device(sys.argv[1])

# check whether the text exists
if d(text=sys.argv[2]).exists:
	d(text=sys.argv[2]).click()






