import unittest
from .list import SingleLinkList, DoubleLinkList


class TestSingleLinkList(unittest.TestCase):

    def test_append(self):
        lst = SingleLinkList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        self.assertEqual(len(lst), 3)
        self.assertEqual(str(lst), '[1, 2, 3]')

    def test_insert(self):
        lst = SingleLinkList()
        lst.append(1)
        lst.append(3)
        lst.insert(1, 2)  # Insert at index 1
        self.assertEqual(str(lst), '[1, 2, 3]')

    def test_remove(self):
        lst = SingleLinkList()
        lst.append(1)
        lst.append(2)
        lst.remove(1)
        self.assertEqual(len(lst), 1)
        self.assertEqual(str(lst), '[2]')

    def test_reverse(self):
        lst = SingleLinkList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        lst.reverse()
        self.assertEqual(str(lst), '[3, 2, 1]')

    def test_index(self):
        lst = SingleLinkList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        self.assertEqual(lst.index(2), 1)
        with self.assertRaises(ValueError):
            lst.index(4)

    def test_count(self):
        lst = SingleLinkList()
        lst.append(1)
        lst.append(2)
        lst.append(1)
        self.assertEqual(lst.count(1), 2)
        self.assertEqual(lst.count(2), 1)

    def test_pop(self):
        lst = SingleLinkList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        self.assertEqual(lst.pop(), 3)
        self.assertEqual(len(lst), 2)
        self.assertEqual(str(lst), '[1, 2]')

    def test_clear(self):
        lst = SingleLinkList()
        lst.append(1)
        lst.append(2)
        lst.clear()
        self.assertEqual(len(lst), 0)
        self.assertEqual(str(lst), '[]')

    def test_contains(self):
        lst = SingleLinkList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        self.assertIn(2, lst)
        self.assertNotIn(4, lst)


class TestDoubleLinkList(unittest.TestCase):

    def test_append(self):
        lst = DoubleLinkList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        self.assertEqual(len(lst), 3)
        self.assertEqual(str(lst), '[1, 2, 3]')

    def test_insert(self):
        lst = DoubleLinkList()
        lst.append(1)
        lst.append(3)
        lst.insert(1, 2)
        self.assertEqual(str(lst), '[1, 2, 3]')

    def test_remove(self):
        lst = DoubleLinkList()
        lst.append(1)
        lst.append(2)
        lst.remove(1)
        self.assertEqual(len(lst), 1)
        self.assertEqual(str(lst), '[2]')

    def test_reverse(self):
        lst = DoubleLinkList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        lst.reverse()
        self.assertEqual(str(lst), '[3, 2, 1]')

    def test_pop(self):
        lst = DoubleLinkList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        self.assertEqual(lst.pop(), 3)
        self.assertEqual(len(lst), 2)
        self.assertEqual(str(lst), '[1, 2]')

    def test_clear(self):
        lst = DoubleLinkList()
        lst.append(1)
        lst.append(2)
        lst.clear()
        self.assertEqual(len(lst), 0)
        self.assertEqual(str(lst), '[]')

    def test_contains(self):
        lst = DoubleLinkList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        self.assertIn(2, lst)
        self.assertNotIn(4, lst)


if __name__ == '__main__':
    unittest.main()
