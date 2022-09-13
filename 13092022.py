import json
import sys


# script_args = sys.argv
# print(f"{script_args=}, {type(script_args)=}")
# print(f"Script name is {script_args[0]}")
##########################################################
# print("Start")
# try:
#     sys.exit(1)
# except SystemExit:
#     print("Exception is captured")
#
# sys.exit(128)
# print("END")
##########################################################
# sys.getrecursionlimit()
# sys.setrecursionlimit(100)
# sys.getrecursionlimit()
##########################################################
# fruits = ["apple", "melon", "orange"]
# print(f"{sys.getsizeof(fruits)=}")
##########################################################
# version = sys.version_info
# print(f"{version=}")
#
# if version[0] != 3:
#     print("All rigth")
#     import time
# else:
#     import datetime
#     print("Almost all rigth")
# print(sys.version)
# print(sys.platform)
##########################################################
import time


# print(time.time())
# print(time.time_ns())
# print(time.timezone)
#
# print("Start")
# time.sleep(3)
# print("End")

# print(
#     f"{time.ctime(0)=},\n"
#     f"{time.ctime()=},\n"
# )
##########################################################
# import datetime


# current_datetime = datetime.datetime.now()
# print(
#     f"{current_datetime=}, {type(current_datetime)=}\n"
#     f"{current_datetime.ctime()=},\n"
#     f"{current_datetime.timestamp()=},\n"  # equal to time.time()
#     f"{current_datetime.date()=},\n"
#     f"{current_datetime.year=},\n"
#     f"{current_datetime.month=},\n"
#     f"{current_datetime.weekday()=},\n"  # week starts from 0 (zero)
#     f"{current_datetime.isoweekday()=},\n"  # week starts from 1
#     f"{current_datetime.day=},\n"
#     f"{current_datetime.time()=},\n"
#     f"{current_datetime.hour=},\n"
#     f"{current_datetime.minute=},\n"
#     f"{current_datetime.second=},\n"
#     f"{current_datetime.microsecond=}"
# )
##########################################################
# parsed_dt = datetime.datetime.strptime("31-12-2030 23:59", "%d-%m-%Y %H:%M")
# print(f"{parsed_dt=}, {type(parsed_dt)=}")
##########################################################
# import time
#
#
# current_datetime = datetime.datetime.now()
# time.sleep(3)
# time_difference = datetime.datetime.now() - current_datetime
# print(
#     f"{time_difference=}, {type(time_difference)=},\n"
#     f"{time_difference.microseconds=}, {type(time_difference.microseconds)=},\n"
#     f"{time_difference.days=}, {type(time_difference.days)=},\n"
#     f"{time_difference.seconds=}, {type(time_difference.seconds)=},\n"
#     f"{time_difference.total_seconds()=}, {type(time_difference.total_seconds())=}"
# )
