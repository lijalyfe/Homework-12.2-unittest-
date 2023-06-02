import unittest
from arrs import get, my_slice


class TestArrs(unittest.TestCase):
    def test_get_existing_index(self):
        arr = [1, 2, 3]
        self.assertEqual(get(arr, 1), 2)
def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 3
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
