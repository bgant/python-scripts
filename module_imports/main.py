from first import first_function
from module_b.second import second_function
from random.sleep import sleep
from sys import path as sys_path
from os import path as os_path

first_function()
second_function()
sleep()

print()
print('Where is Python looking for modules:')
for dir in sys_path:
    print(dir)

print()
print('What if I want to add the current directory just while this script is running:')
CURR_DIR = os_path.dirname(os_path.abspath(__file__))
print(CURR_DIR)
sys_path.append(CURR_DIR)
for dir in sys_path:
    print(dir)
