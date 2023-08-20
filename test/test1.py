import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        json_data = {
            "name": {
                "first": "John",
                "last": "Doe"
            }
        }
        for value in json_data.values():
            value["first"] = "Jason"
        print(json_data)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
