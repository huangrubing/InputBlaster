from uiautomator import Device
import sys

d = Device(sys.argv[1])

# check whether the resourceId exists
if d(resourceId=sys.argv[2]).exists:
	d(resourceId=sys.argv[2]).click()





