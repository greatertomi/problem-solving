class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return f"Node({self.value})"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return
        else:
            current = self.root
            while True:
                if value == current.value:
                    return None
                if value < current.value:
                    if current.left is None:
                        current.left = newNode
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = newNode
                        return
                    current = current.right

    def DFSPreOrder(self):
        data = []

        def transverse(node):
            data.append(node.value)
            if node.left:
                transverse(node.left)
            if node.right:
                transverse(node.right)
        transverse(self.root)
        print(*data, end=" ")

    def DFSInOrder(self):
        data = []

        def transverse(node):
            if node.left:
                transverse(node.left)
            data.append(node.value)
            if node.right:
                transverse(node.right)
        transverse(self.root)
        print(*data, end=" ")


# def height(node):
#     if node is None:
#         return 0
#     else:
#         return max(height(node.left), height(node.right)) + 1


tree = BinarySearchTree()
tree.insert(1)
tree.insert(2)
tree.insert(5)
tree.insert(3)
tree.insert(6)
tree.insert(4)

# tree.insert(10)
# tree.insert(15)
# tree.insert(13)
# tree.insert(5)
# tree.insert(9)
# tree.insert(1)
# tree.insert(10)
tree.DFSInOrder()
# height(tree)
