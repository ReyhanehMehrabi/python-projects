from ast import Num
import My_module

import My_module as demo # demo is an aliase for my_module
# what if i want to be sellective of what i will import
from My_module import greeting # only greeting
from My_module import greeting, name,my_list,say_hi # only greeting

print(My_module.name)


print(My_module.my_list[1])

My_module.say_hi()

demo.say_hi()

greeting()
   