# Brian Campbell
# campbeb3@oregonstate.edu
# CS362-W24-A2
# Password Checker Assignment
# Contains the tests you wrote during the TDD process (main function)


import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        """Must contain a minumum length of 8 characters,
        Returns False if not a minimum of 8"""
        too_short = "1234abcd"
        self.assertFalse(check_pwd(too_short))


if __name__ == '__main__':
    unittest.main()
