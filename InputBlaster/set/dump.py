from uiautomator import Device
import sys

d = Device(sys.argv[1])

# dump ui xml
d.dump(sys.argv[2])








