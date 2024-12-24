# https://www.programiz.com/dsa/huffman-coding
from collections import Counter


class Node:
    def __init__(self, data):
        self.data = data
        self._left = None
        self._right = None

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, node):
        self._left = node

    @right.setter
    def right(self, node):
        self._right = node

    def __repr__(self):
        return f"Node({self.data})"

def min_node(nodes):
    min_node = nodes[0]
    min_index = 0
    for i in range(1, len(nodes)):
        if nodes[i].data["freq"] < min_node.data["freq"]:
            min_node = nodes[i]
            min_index = i
    return min_index


# https://www.educative.io/answers/how-is-the-frequency-table-created-for-huffman-coding
def create_frequency_tree(content):
    ...



def preorder(node, codes, prefix=""):
    if node == None:
        return
    if len(node.data["char"]) == 1:
        codes.append((node.data["char"], prefix))

    preorder(node.left, codes, prefix + "0")
    preorder(node.right, codes, prefix + "1")

def get_codes(root):
    codes = []
    preorder(root, codes)
    return codes
