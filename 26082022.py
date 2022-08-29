# import random

# print(random.randint(0, 100))
# print(random.random())

###############################################
# import time as new_time_name
#
# from random import random, randint as custom_randint
#
#
# print(f"{random()=}")
# print(f"{custom_randint(0, 100)=}")
# print(f"{new_time_name.time()=}")
###############################################
# from my_module import MY_VAR, my_func
#
#
# print(MY_VAR)
# print(my_func())
###############################################
# # OPTION 1
# import my_module
# my_module.get_name()
# print(my_module.MY_VAR)

# # OPTION 2
# from my_module import get_name
# get_name()

# # OPTION 3 # Just don't do it!!!
# from my_module import *


# if __name__ == '__main__':
#     print(f"I'm your Father, bcs my {__name__=}")
#     get_name()
###############################################
# import os


# list_dir = os.listdir()
# print(f"{list_dir=}")
#
# list_dir = os.listdir("../")
# print(f"{list_dir=}")
###############################################
# first_folder = "first_folder"
# second_folder = "second_folder"
# third_folder = ""
# filename = "filename.txt"
#
# list_dir = os.path.join(first_folder, second_folder, third_folder, filename)
# print(f"{list_dir=}")
#
# # # example of f-string disadvantages
# separator = "/" or "\\"
#
# formated_path = (
#     f"{first_folder}{separator}"
#     f"{second_folder}{separator}"
#     f"{third_folder}{separator}{filename}"
# )
# print(f"{formated_path=}")
#
# print(f"{os.name=}")
#
# print(f"{os.system('dir')=}")
###############################################
# import os
# import json
#
#
# obj = {"os": os.name}
#
# with open("os_report.json", "w") as fh:
#     json.dump(obj, fh)

