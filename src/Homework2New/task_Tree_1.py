def tree_by_levels(node):
    """Collect all values of children from tree

    :param node: class Node(left, right, value)
    :return: list of all children from tree
    """
    list_of_roots = recursion(node, [], 0) or []
    return [root for level in list_of_roots for root in level if root]


def recursion(node, list_of_cildren, tree_level):
    """Tree traversal recursion

    Function collecting values of all children from class Node
    with recursion
    """
    if not node:
        return
    list_of_cildren.append([])
    list_of_cildren[tree_level].append(node.value)
    recursion(node.left, list_of_cildren, tree_level + 1)
    recursion(node.right, list_of_cildren, tree_level + 1)
    return list_of_cildren


class Node:

    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


assert tree_by_levels(None) == []
assert tree_by_levels(Node((
    Node(Node(None, None, 10), Node(None, None, 4), 2)),
    Node(Node(None, None, 5), Node(None, None, 6), 3), 1)
) == [1, 2, 3, 10, 4, 5, 6]
