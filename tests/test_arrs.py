import unittest
from arrs import get, my_slice


class TestArrs(unittest.TestCase):
    def test_get_existing_index(self):
        arr = [1, 2, 3]
        self.assertEqual(get(arr, 1), 2)

    def test_get_not_existing_index_default(self):
        arr = [1, 2, 3]
        self.assertEqual(get(arr, 3, None), None)

    def test_get_negative_index_default(self):
        arr = [1, 2, 3]
        self.assertEqual(get(arr, -1, None), None)

    def test_my_slice_full_list(self):
        arr = [1, 2, 3]
        self.assertEqual(my_slice(arr), [1, 2, 3])

    def test_my_slice_positive_start_and_end_indices(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(arr, 1, 4), [2, 3, 4])

    def test_my_slice_negative_start_and_end_indices(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(arr, -3, -1), [3, 4])
