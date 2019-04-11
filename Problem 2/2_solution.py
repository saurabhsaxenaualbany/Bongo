import unittest


class Tree:
    def __init__(self, node):
        self.node = node


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent


def lca(n1, n2):
    """
    The idea is for node1 find the route till the node and store in a list.
    Similarly do the same thing for the node2.
    After eliminating the last element as it will be the root,
    Find the common element in both the list.
    Run Time complexity: O(n)
    :param n1:
    :param n2:
    :return:
    """
    path_to_root = []

    while n1:
        path_to_root.append(n1.value)
        n1 = n1.parent

    path_2_root = []
    while n2:
        path_2_root.append(n2.value)
        n2 = n2.parent
    path_2_root = path_2_root[:-1]
    path_to_root = path_to_root[:-1]
    result = list(set(path_2_root).intersection(path_to_root))
    return result[-1] if result else None


class TestLCA(unittest.TestCase):

    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2, self.node1)
        self.node3 = Node(3, self.node1)
        self.node4 = Node(4, self.node2)
        self.node5 = Node(5, self.node2)
        self.node6 = Node(6, self.node3)
        self.node7 = Node(7, self.node3)
        self.node8 = Node(8, self.node4)
        self.node9 = Node(9, self.node4)

    def test_01(self):
        self.assertEqual(lca(self.node8, self.node9), 4)

    def test_02(self):
        self.assertEqual(lca(self.node3, self.node7), 3)

    def test_03(self):
        self.assertEqual(lca(self.node8, self.node7), None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
