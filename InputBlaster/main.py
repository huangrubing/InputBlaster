import os
import openai
from utils import *
from module1 import module1
from module2 import module2

ans1, editText_list = module1()
print(ans1)

if ans1 == "no input text component":
    print("There is no input text component on this page. ")
else:
    ans2 = module2(ans1, editText_list)
    print(ans2)
    