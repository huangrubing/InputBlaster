from uiautomator import Device
import sys


d = Device(sys.argv[1])

# click  
if d(className=sys.argv[2]).count > int(sys.argv[3]):
    d(className=sys.argv[2], instance=int(sys.argv[3])).click()
