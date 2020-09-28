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

    def DFSPostOrder(self):
        data = []

        def transverse(node):
            if node.left:
                transverse(node.left)
            if node.right:
                transverse(node.right)
            data.append(node.value)
        transverse(self.root)
        print(*data, end=" ")

    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def BFS(self):
        queue = [self.root]

        while len(queue) > 0:
            node = queue.pop(0)
            print(node.value, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def topView(root):
    this_level = [(root, 0)]
    scores = {}
    while this_level:
        for _ in range(len(this_level)):
            node, score = this_level.pop(0)
            if not node:
                continue
            if score not in scores:
                scores[score] = node.value
            this_level.extend(
                [(node.left, score - 1),
                 (node.right, score + 1)])
    for _, value in sorted(list(scores.items())):
        print(value, end=' ')


def lowestCommonAncestor(root, v1, v2):
    currentNode = None
    while root is not None:
        currentNode = root.root
        if currentNode.value > v1 and currentNode.value > v2:
            currentNode = currentNode.left
        elif currentNode.value < v1 and currentNode.value < v2:
            currentNode = currentNode.right
        else:
            break
    return currentNode


tree = BinarySearchTree()
tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(1)
tree.insert(7)
tree.insert(6)

# tree.DFSPreOrder()
print(lowestCommonAncestor(tree, 1, 7))
# print(tree.height(tree.root))
