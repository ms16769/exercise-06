# #!/usr/bin/env python3
# # *-* coding:utf-8 *-*

# # if __name__ == "__main__":
    # # pass
# class BinBinTreeNode:

    # def __init__(self, data):

        # self.left = None
        # self.right = None
        # self.data = data

# # Insert method to create BinBinTreeNodes
    # def insert(self, data):

        # if self.data:
            # if data < self.data:
                # if self.left is None:
                    # self.left = BinBinTreeNode(data)
                # else:
                    # self.left.insert(data)
            # elif data > self.data:
                # if self.right is None:
                    # self.right = BinBinTreeNode(data)
                # else:
                    # self.right.insert(data)
        # else:
            # self.data = data
# # findval method to compare the value with BinBinTreeNodes

    # def findval(self, lkpval):
        # if lkpval < self.data:
            # if self.left is None:
                # return str(lkpval)+" is not Found"
            # return self.left.findval(lkpval)
        # elif lkpval > self.data:
            # if self.right is None:
                # return str(lkpval)+" is not Found"
            # return self.right.findval(lkpval)
        # else:
            # return str(self.data) + " is found"
# # Print the tree

    # def PrintTree(self):
        # if self.left:
            # self.left.PrintTree()
        # print(self.data),
        # if self.right:
            # self.right.PrintTree()

# root = BinBinTreeNode(27)
# root.insert(14)
# root.insert(35)
# root.insert(31)
# root.insert(10)
# root.insert(19)
# print(root.findval(7))
# print(root.findval(14))

# if __name__ == "__main__":
    # main()
	
	
"""
    >>> bst = BinTree()
    >>> for v in [6,2,8,0,4,7,9,3,5]:
    ...     bst.insert(v, v)
    >>> [bst.search(v) for v in [5,0,9,6]]
    [5, 0, 9, 6]
    >>> bst.search(13)
    Traceback (most recent call last):
    ...
    KeyError: '13 is not found'
    >>> bst.get_height()
    4
    >>> bst.delete(5)
    >>> bst.get_height()
    4
    >>> bst.get_max_value()
    9
    >>> bst.get_min_value()
    0
    >>> bst.delete(3)
    >>> bst.delete(7)
    >>> bst.delete(9)
    >>> bst.get_height()
    3
    >>> bst
    BinTree(root=BinTreeNode(key=6, value=6, left=BinTreeNode(key=2, value=2, left=BinTreeNode(key=0, value=0, left=None, right=None), right=BinTreeNode(key=4, value=4, left=None, right=None)), right=BinTreeNode(key=8, value=8, left=None, right=None)))
"""

from dataclasses import dataclass
from typing import Any

@dataclass
class BinTreeNode:
    key: Any
    value: Any
    left: 'BinTreeNode' = None
    right: 'BinTreeNode' = None

class BinTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        """Return the value assiociated with key, or raise a KeyError exception"""
        return _search(self.root, key).value

    def insert(self, key, value):
        """insert node into binary tree based on node's key"""
        self.root = _insert(self.root, key, value)

    def get_min_value(self):
        """return the min value from tree"""
        return _get_min(self.root).value

    def get_max_value(self):
        """return the min value from tree"""
        return _get_max(self.root).value

    def get_max_value(self):
        """return the min value from tree"""
        return _get_max(self.root).value

    def get_height(self):
        """return the height from tree"""
        return _get_height(self.root)

    def delete(self, key):
        """Delete the node having the given key"""
        self.root = _delete(self.root, key)

    def __repr__(self):
        return f"BinTree(root={self.root})"

# standalone function, out of the BinTree class
def _search(node, key):
    """Search a node by key. Raise a KeyError exception if the key is not in the tree

    >>> _search(None, 1)
    Traceback (most recent call last):
    ...
    KeyError: '1 is not found'
    >>> _search(BinTreeNode(0, 0), 1)
    Traceback (most recent call last):
    ...
    KeyError: '1 is not found'
    >>> _search(BinTreeNode(1, 0), 1)
    BinTreeNode(key=1, value=0, left=None, right=None)
    >>> _search(BinTreeNode(0, 0, None, BinTreeNode(1, 1)), 1)
    BinTreeNode(key=1, value=1, left=None, right=None)
    """
    if node is None: # end of recursion
        raise KeyError(f'{key} is not found')

    if key < node.key:
        return _search(node.left, key)
    elif key > node.key:
        return _search(node.right, key)
    else:
        return node


def _insert(node, key, value):
    """Return node extended with a new key/value pair

    >>> node = BinTreeNode(0,0)
    >>> for i in range(2):
    ...     node = _insert(node, i, 2*i+1)
    >>> node
    BinTreeNode(key=0, value=1, left=None, right=BinTreeNode(key=1, value=3, left=None, right=None))
    >>> _insert(node, -1, -2)
    BinTreeNode(key=0, value=1, left=BinTreeNode(key=-1, value=-2, left=None, right=None), right=BinTreeNode(key=1, value=3, left=None, right=None))
    """
    if node is None:
        return BinTreeNode(key, value)

    if key < node.key:
        return BinTreeNode(node.key, node.value, _insert(node.left, key, value), node.right)
    elif key > node.key:
        return BinTreeNode(node.key, node.value, node.left, _insert(node.right, key, value))
    else: # key == node.key
        return BinTreeNode(node.key, value, node.left, node.right)

def _get_min(node):
    """return the min value from tree
    >>> node = BinTreeNode(0,0)
    >>> for i in range(3):
    ...     node = _insert(node, i, 2*i+1)
    >>> _get_min(node).value
    1
    """
    if node.left is None:
        return node

    return _get_min(node.left)

def _get_max(node):
    """return the max value from tree
    >>> node = BinTreeNode(0,0)
    >>> for i in range(3):
    ...     node = _insert(node, i, 2*i+1)
    >>> _get_max(node).value
    5
    """
    if node.right is None:
        return node

    return _get_max(node.right)

def _get_height(node):
    """return tree height of binary search tree
    >>> node = BinTreeNode(0,0)
    >>> for i in range(3):
    ...     node = _insert(node, i, 2*i+1)
    >>> _get_height(node)
    3
    """
    if node is None: # end of the recursion
        return 0
    return 1 + max(_get_height(node.left), _get_height(node.right))

def _delete(node, key):
    """Return the tree without the node having the given key
    >>> node = BinTreeNode(0,0)
    >>> node = _insert(node, 1, 1)
    >>> node = _insert(node, -1, 2)
    >>> _delete(node, 0)
    BinTreeNode(key=1, value=1, left=BinTreeNode(key=-1, value=2, left=None, right=None), right=None)
    """
    if node is None:
        return None
    if key < node.key:
        return BinTreeNode(node.key, node.value, _delete(node.left, key), node.right)
    elif key > node.key:
        return BinTreeNode(node.key, node.value, node.left, _delete(node.right, key))
    else: # key == node.key, end of recursion
        if node.left is None:
            return node.right
        else:
            successor, right = _detach_min(node.right)
            return BinTreeNode(successor.key, successor.value, node.left, right)

def _detach_min(node):
    """return the min value from tree
    >>> node = BinTreeNode(0,0)
    >>> node = _insert(node, 1, 1)
    >>> node = _insert(node, -1, 2)
    >>> node = _insert(node, -2, 4)
    >>> node = _insert(node, -0.5, 2.5)
    >>> _detach_min(node)
    (BinTreeNode(key=-2, value=4, left=None, right=None), BinTreeNode(key=0, value=0, left=BinTreeNode(key=-1, value=2, left=None, right=BinTreeNode(key=-0.5, value=2.5, left=None, right=None)), right=BinTreeNode(key=1, value=1, left=None, right=None)))
    """
    if node.left is None:
        return node, None

    m, r = _detach_min(node.left)
    return m, BinTreeNode(node.key, node.value, r, node.right)

if __name__ == '__main__':
	main()