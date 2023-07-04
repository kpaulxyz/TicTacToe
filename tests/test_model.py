import unittest
from model import Model
import os.path


class TestModel(unittest.TestCase):
    def setUp(self) -> None:
        # self.model = model.Model()
        self.field = [[" ", "|", " ", "|", " "],
                      ["—", "+", "—", "+", "—"],
                      [" ", "|", " ", "|", " "],
                      ["—", "+", "—", "+", "—"],
                      [" ", "|", " ", "|", " "]]
        self.field2 = [["X", "|", " ", "|", " "],
                       ["—", "+", "—", "+", "—"],
                       [" ", "|", " ", "|", " "],
                       ["—", "+", "—", "+", "—"],
                       [" ", "|", " ", "|", " "]]
        self.model = Model()  # Create an instance of your Model class

    def tearDown(self):
        if os.path.isfile('./savestate.py'):
            os.remove("savestate.py")  # Remove the savestate file if it exists

    def test_loadsavestate(self):
        f = open("savestate.py", "w")  # Create a savestate file
        f.write('save = [["X", "|", " ", "|", " "],'
                '["—", "+", "—", "+", "—"],'
                '[" ", "|", " ", "|", " "],'
                '["—", "+", "—", "+", "—"],'
                '[" ", "|", " ", "|", " "]]')
        f.close()

        self.model.loadsavestate()  # Call the loadsavestate method
        expected_field = [["X", "|", " ", "|", " "],
                          ["—", "+", "—", "+", "—"],
                          [" ", "|", " ", "|", " "],
                          ["—", "+", "—", "+", "—"],
                          [" ", "|", " ", "|", " "]]
        self.assertEqual(self.model.field, expected_field)  # Check if the field matches the expected state

    def test_checksavestate(self):
        self.assertFalse(self.model.checksavestate())  # Check if savestate does not exist

        f = open("savestate.py", "w")  # Create a savestate file
        f.write('save = [["X", "|", " ", "|", " "],'
                '["—", "+", "—", "+", "—"],'
                '[" ", "|", " ", "|", " "],'
                '["—", "+", "—", "+", "—"],'
                '[" ", "|", " ", "|", " "]]')
        f.close()

        self.assertTrue(self.model.checksavestate())  # Check if savestate exists

    def test_savetosavestate(self):
        self.model.field = [["X", "|", " ", "|", " "],
                            ["—", "+", "—", "+", "—"],
                            [" ", "|", " ", "|", " "],
                            ["—", "+", "—", "+", "—"],
                            [" ", "|", " ", "|", " "]]  # Set the field to a specific state

        self.model.savetosavestate()  # Call the savetosavestate method

        f = open("savestate.py", "r")  # Read the content of the savestate file
        content = f.read()
        f.close()

        expected_content = "save = [['X', '|', ' ', '|', ' ']," \
                           " ['—', '+', '—', '+', '—'], [' ', '|', ' ', '|', ' ']," \
                           " ['—', '+', '—', '+', '—'], [' ', '|', ' ', '|', ' ']]"
        self.assertEqual(content, expected_content)  # Check if the content matches the expected value

    def test_deletesavestate(self):
        f = open("savestate.py", "w")  # Create a savestate file
        f.close()

        self.model.deletesavestate()  # Call the deletesavestate method

        self.assertFalse(os.path.isfile('./savestate.py'))  # Check if the savestate file does not exist

    def test_check_move(self):
        model = Model()  # Create an instance of your Model class
        self.assertEqual(model.check_move(0, 0, True), True)

    def test_do_move(self):
        model = Model()  # Create an instance of your Model class
        model.do_move(0, 0, True, "X", "O")  # Call the do_move method
        expected_field = [["X", "|", " ", "|", " "],
                          ["—", "+", "—", "+", "—"],
                          [" ", "|", " ", "|", " "],
                          ["—", "+", "—", "+", "—"],
                          [" ", "|", " ", "|", " "]]
        self.assertEqual(model.field, expected_field)


if __name__ == '__main__':
    unittest.main()
