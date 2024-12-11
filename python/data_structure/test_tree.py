import unittest
from .tree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def test_insert(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        self.assertEqual(tree.root.val, 10)
        self.assertEqual(tree.root.left.val, 5)
        self.assertEqual(tree.root.right.val, 15)

    def test_inorder(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        self.assertEqual(tree.inorder(), [5, 10, 15])

    def test_preorder(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        self.assertEqual(tree.preorder(), [10, 5, 15])

    def test_postorder(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        self.assertEqual(tree.postorder(), [5, 15, 10])

    def test_levelorder(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        self.assertEqual(tree.levelorder(), [10, 5, 15])

    def test_height(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        self.assertEqual(tree.height(), 2)

    def test_is_balanced(self):
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        self.assertTrue(tree.is_balanced())

        tree.insert(3)
        tree.insert(4)
        tree.insert(2)
        self.assertFalse(tree.is_balanced())


    def test_is_same_tree(self):
        tree1 = BinaryTree()
        tree1.insert(10)
        tree1.insert(5)
        tree1.insert(15)

        tree2 = BinaryTree()
        tree2.insert(10)
        tree2.insert(5)
        tree2.insert(15)

        tree3 = BinaryTree()
        tree3.insert(10)
        tree3.insert(5)

        self.assertTrue(tree1.is_same_tree(tree2))
        self.assertFalse(tree1.is_same_tree(tree3))

    def test_is_subtree(self):
        tree1 = BinaryTree()
        tree1.insert(10)
        tree1.insert(5)
        tree1.insert(15)

        tree2 = BinaryTree()
        tree2.insert(5)

        tree3 = BinaryTree()
        tree3.insert(20)

        tree4 = BinaryTree()
        tree4.insert(10)
        tree4.insert(5)
        tree4.insert(15)
        tree4.insert(3)
        tree4.insert(4)

        tree5 = BinaryTree()
        tree5.insert(5)
        tree5.insert(3)
        tree5.insert(4)

        self.assertTrue(tree1.is_subtree(tree2))
        self.assertFalse(tree1.is_subtree(tree3))
        self.assertTrue(tree4.is_subtree(tree5))


if __name__ == '__main__':
    unittest.main()
