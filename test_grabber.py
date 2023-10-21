import unittest
import grabber

testUrl = 'https://hitparadeitalia.it/hp_yends/hpe1947.htm'

class MyTest(unittest.TestCase):
    def test_list_not_tempty(self):
        self.assertIsNotNone(grabber.grab_songs(testUrl))

    def test_list_more_than_one(self):
        print(len(grabber.grab_songs(testUrl)))
        self.assertGreaterEqual(len(grabber.grab_songs(testUrl)),1)

    def test_string_in_list(self):
        value_to_look_for = {'track': 'Serenata serena', 'artist': 'Franco Ricci'}
        if value_to_look_for in grabber.grab_songs(testUrl):
            print('good')
        else:
            self.fail('no string found')

class StringTests(unittest.TestCase):
    def test_string_cleaning(self):
        self.assertEqual(grabber.clean_string('this is a test song [23, 23]'),'this is a test song')
