import unittest


class Person:
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


OUTPUT = ''


def process_external_class(person, depth):
    """
    This funciton is called whenever a Person object is encountered.

    :param person: Object of the person class
    :param depth: Depth where this object was found
    :return: Depth reached
    """
    global OUTPUT
    for (key, value) in person.__dict__.items():
        OUTPUT += f'{key} {depth}'
        print(key, depth)
        if isinstance(value, Person):
            process_external_class(value, depth + 1)
    return depth


def compute_depth(data, depth=1):
    """
    A recursive function prints key and depth of the key
    whenever data passed to it is a dict. If a Person
    class object is passed it will call process_external_class()

    :param data: dict input data
    :param depth: defaults to 1, unless otherwise mentioned
    :return: depth
    """
    global OUTPUT

    if isinstance(data, Person) and data:
        return process_external_class(data, depth)

    if not (isinstance(data, dict) and data):
        return depth

    for key in data:
        print(key, depth)
        OUTPUT += f'{key} {depth}'
        compute_depth(data[key], depth + 1)


def print_depth(data):
    compute_depth(data)
    return OUTPUT


class TestDictDepth(unittest.TestCase):

    def setUp(self):
        first_person = Person('John', 'Doe', 'Guido van Rossum')
        second_person= Person('foo', 'bar', first_person)
        self.data = {
                "key1": 1,
                "key2": {
                    "key3": second_person,
                    "Key4": {
                        "Key5": 4,
                        "key6": {
                            "key7": 2,
                            "user": 100
                        }
                    }
                }
            }

    def test_1_dot_1(self):
        self.assertIn('key1 1', print_depth(self.data))

    def test_1_dot_2(self):
        self.assertIn('first_name 3', print_depth(self.data))


if __name__ == '__main__':
    unittest.main(verbosity=2)
