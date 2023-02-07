from unittest import TestCase
import quiz05


class Test(TestCase):
    def test_list_of_duplicates(self):
        test_list = [1, 1, 1, 1, 1]
        self.assertTrue(quiz05.is_sorted(test_list))

    def test_list_of_one(self):
        test_list = [1]
        self.assertTrue(quiz05.is_sorted(test_list))

    def test_list_of_zero(self):
        test_list = []
        self.assertTrue(quiz05.is_sorted(test_list))

    def test_sorted_list(self):
        test_list = [1, 2, 3, 4, 5]
        self.assertTrue(quiz05.is_sorted(test_list))

    def test_unsorted(self):
        test_list = [3, 2, 6, 7, 5]
        self.assertFalse(quiz05.is_sorted(test_list))

    def test_descending_order(self):
        test_list = [5, 4, 3, 2, 1]
        self.assertFalse(quiz05.is_sorted(test_list))
