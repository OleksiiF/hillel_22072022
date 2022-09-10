# import os
# import unittest
# import doctest
import logging


# assert 1 == 1
# assert "t" in "text"
# assert bool("digits")
#
# try:
#     assert 1 < 0
# except AssertionError:
#     print("Isn't right!")
#############################################
# def get_sum(a, b):
#     """
#     >>> get_sum(10, 3)
#     13
#     >>> get_sum(10, 3) * 2 - get_sum(-11, 0)
#     37
#     """
#
#     return a + b
#
# doctest.testmod()
#############################################
# class TestBuiltins(unittest.TestCase):
#     def setUp(self):
#         self.digit = 404 - 500 + 200
#
#     def test_sorted(self):
#         self.assertEqual(sorted([3, 2, 1]), [1, 2, 3])
#         self.assertEqual(sorted([-13, 0, -27]), [-27, -13, 0])
#
#     def test_str(self):
#         self.assertEqual(str(self.digit), "104")
#         self.assertEqual(str(None), "None")
#
#     def test_int(self):
#         self.assertEqual(int("0"), 0)
#         self.assertEqual(int(True), 1)
#
#         with self.assertRaises(ValueError):
#             int("1.0")
#             # int("1")
#
#     @unittest.skip("bcs test is not correct")  # .skipIf(), .skipUnless()
#     # @unittest.skipIf(os.name=="nt", "just bcs")  # .skipIf(), .skipUnless()
#     # @unittest.skipUnless(os.name=="unix", "just bcs")  # .skipIf(), .skipUnless()
#     def test_float(self):
#         self.assertIsNone(self.digit)
#
#
# if __name__ == '__main__':
#     # python -m unittest tests/test_module.py
#     # python -m unittest tests/test_module.py -v
#     # python -m unittest test_module
#     # python -m unittest test_module.TestBuiltins
#     # python -m unittest test_module.TestBuiltins.test_int
#     unittest.main()
#############################################
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
#     datefmt="%m-%d %H:%M"
# )
#
# my_logger = logging.getLogger()
#
# for iteration in range(3):
#     my_logger.log(level=logging.INFO, msg=f"Iteration {iteration} done")
#############################################
# from logging.handlers import TimedRotatingFileHandler
#
#
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
#     datefmt="%m-%d %H:%M"
# )
# file_handler = TimedRotatingFileHandler(
#     filename="work_log",
#     when="H",
#     interval=24,
#     backupCount=7,
# )
#
# file_handler.setFormatter(
#     logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
# )
# file_handler.suffix = '%Y-%m-%d_%H_%M_%S'
#
#
# my_multi_logger = logging.getLogger()
# my_multi_logger.addHandler(file_handler)
#
#
# for iteration in range(3):
#     my_multi_logger.info(f"This message will end up in the file as well")

#############################################
logging.basicConfig(filename="my_standalone_log_file")
my_only_file_logger = logging.getLogger()


for iteration in range(3):
    my_only_file_logger.warning(f"This message will end up only in the file")

