# class Fetus:
#     def __init__(self, name):
#         self.name = name
#
#     def get_fetus_name(self):
#         return self.name
#
#
# fetus_obj = Fetus("apple")
# print(f"{fetus_obj.name=}")
# print(f"{fetus_obj.get_fetus_name()=}")
###################################################
# class Fetus:
#     def __init__(self, name):
#         self._name = name
#
#     def get_fetus_name(self):
#         return list(self._name.capitalize())
#
# class Fruit(Fetus):
#     pass
#
#
# fruit_obj = Fruit("apple")
# print(f"{fruit_obj._name=}")  # not recommended
# print(f"{fruit_obj.get_fetus_name()=}")
###################################################
# class Fetus:
#     def __init__(self, name):
#         self.__name = name
#
#     def __get_fetus_name(self):
#         return self.__name
#
#     def get_fetus_name(self):
#         return self.__get_fetus_name()
#
#
# class Fruit(Fetus):
#     def get_fruit_name(self):
#         return self.__name
#
# fruit_obj = Fruit("apple")
# try:
#     fruit_obj.get_fetus_name()
# except AttributeError as error:
#     print(f"{error=}")
#
# try:
#     fruit_obj.get_fruit_name()
# except AttributeError as error:
#     print(f"{error=}")
#
#
# try:
#     fruit_obj.__name
# except AttributeError as error:
#     print(f"{error=}")
###################################################
# class Bank:
#     def __init__(self):
#         self.__count = 1000000
#
#     @property
#     def count(self):
#         return self.__count
#
#     @property
#     def count_info(self):
#         return f"You have {self.__count}$"
#
#
# bank = Bank()
# print(f"{bank.count=}")
# print(f"{bank.count_info=}")
#
# try:
#     bank.count = 10**10
# except AttributeError as error:
#     print(f"{error=}")
###################################################
# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @staticmethod
#     def get_help():
#         return "Provide 2 digits"
#
#
# calc = Calculator(1, 2)
# print(f"{calc.get_help()=}")
# print(f"{Calculator.get_help()=}")
###################################################
# class MarineVehicle:
#     def __init__(self, displacement):
#         self.displacement = displacement
#
#
# class Vehicle:
#     def __init__(self, speed, is_passenger, fuel):
#         self.speed = speed
#         self.is_passenger = is_passenger
#         self.fuel = fuel
#
#     def get_distance_by_hours(self, hours):
#         return self.speed * hours
#
#
# class Plane(Vehicle):
#     pass
#
#
# class Car(Vehicle):
#     def __init__(self, speed, is_passenger, wheels, fuel):
#         self.wheels = wheels
#         super().__init__(speed, is_passenger, fuel)
#
#
# class Bus(Car):
#     def __init__(self, speed, is_passenger, wheels, passengers, fuel):
#         self.passengers = passengers
#         self.speed_reduce_cooef = 0.05
#         super().__init__(speed, is_passenger, wheels, fuel)
#
#     def get_distance_by_hours(self, hours):
#         return (self.speed - self.passengers * self.speed_reduce_cooef) * hours
#
#
# class Boat(MarineVehicle, Vehicle):
#     def __init__(self, speed, is_passenger, displacement, fuel, rum_barrels):
#         self.rum_barrels = rum_barrels
#         Vehicle.__init__(self, speed, is_passenger, fuel)
#         MarineVehicle.__init__(self, displacement)
#
#
# private_plane = Plane(speed=240, is_passenger=True, fuel='gasoline')
# print(f"{private_plane.get_distance_by_hours(2)=}")
#
# minibus = Bus(
#     speed=70,
#     is_passenger=True,
#     wheels=8,
#     passengers=37,
#     fuel='electricity'
# )
# print(f"{minibus.get_distance_by_hours(4)=}")
#
# private_boat = Boat(
#     speed=90,
#     is_passenger=False,
#     displacement=15,
#     fuel='electricity',
#     rum_barrels=13
# )
# print(f"{private_boat.get_distance_by_hours(4)=}")
# print(f"{private_boat.rum_barrels=}")
# print(f"{Boat.__mro__=}")
###################################################
# class Animal:
#     def voice(self):
#         raise NotImplementedError("You must implement voice method")
#
#
# class Cat(Animal):
#     pass
#
#
# cat = Cat()
# cat.voice()