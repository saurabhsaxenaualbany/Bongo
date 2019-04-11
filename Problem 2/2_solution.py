import unittest


class Tree:
    def __init__(self, node):
        self.node = node


class Node:
    def __init__(self, value, parent=None):
        self.value: value
        self.parent: parent


def lca(node1, node2):
    path_to_root = []
    while node1:
        path_to_root.append(node1.value)
        node1 = node1.parent

    path_2_root = []
    while node2:
        path_2_root.append(node2)
        node2 = node2.parent
    path_2_root = path_2_root[:-1]
    path_to_root  = path_to_root[:-1]
    for x in path_2_root:
        for y in path_to_root:
            if y == x:
                return x

    return None


class TestLCA(unittest.TestCase):

    def setUp(self):
        print('tldr')
