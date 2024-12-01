from .node import TreeNode


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, x):
        if self.root is None:
            self.root = TreeNode(x)
            return
        current = self.root
        while True:
            if x < current.val:
                if current.left is None:
                    current.left = TreeNode(x)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(x)
                    return
                current = current.right

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node is None:
            return
        result.append(node.val)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node is None:
            return
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.val)

    def levelorder(self):
        result = []
        if self.root is None:
            return result
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height, right_height)

    def is_balanced(self):
        return self._is_balanced(self.root)[0]

    def _is_balanced(self, node):
        if node is None:
            return True, 0
        left_balanced, left_height = self._is_balanced(node.left)
        right_balanced, right_height = self._is_balanced(node.right)
        return left_balanced and right_balanced and abs(left_height - right_height) <= 1, 1 + max(left_height, right_height)


    def is_same_tree(self, other):
        return self._is_same_tree(self.root, other.root)

    def _is_same_tree(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return node1.val == node2.val and self._is_same_tree(node1.left, node2.left) and self._is_same_tree(node1.right, node2.right)

    def is_subtree(self, other):
        return self._is_subtree(self.root, other.root)

    def _is_subtree(self, node1, node2):
        if node1 is None:
            return False
        return self._is_same_tree(node1, node2) or self._is_subtree(node1.left, node2) or self._is_subtree(node1.right, node2)

