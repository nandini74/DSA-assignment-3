class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        # find(key) : returns true if key is present else false
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None:
            return False
        if key < node.key:
            return self._find(node.left, key)
        elif key > node.key:
            return self._find(node.right, key)
        else:
            return True

    def insert(self, key):
        # insert(key) : insert a new key
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def remove(self, key):
        # remove(key) : remove an existing key
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._remove(node.right, temp.key)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def order_of_key(self, key):
        # order_of_key(key) : returns the order of the key compared to the existing elements i.e., how many elements are smaller than key
        return self._order_of_key(self.root, key)

    def _order_of_key(self, node, key):
        if node is None:
            return 0
        if key < node.key:
            return self._order_of_key(node.left, key)
        elif key > node.key:
            return 1 + self._get_size(node.left) + self._order_of_key(node.right, key)
        else:
            return self._get_size(node.left)

    def get_by_order(self, k):
        # get_by_order(k) : returns the  k’th element among the existing keys
        return self._get_by_order(self.root, k)

    def _get_by_order(self, node, k):
        if node is None:
            return None
        size = self._get_size(node.left)
        if k < size:
            return self._get_by_order(node.left, k)
        elif k > size:
            return self._get_by_order(node.right, k - size - 1)
        else:
            return node.key

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left)