class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


def create_linked_list(input_list):
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
            tail.prev = head
    return head


def print_list(head):
    if head:
        print(head.data, end=' <-> ')
        print_list(head.next)


def sortedInsert(head, data):
    node = Node(data, None, None)
    if head is None:
        return node
    elif data < head.data:
        node.next = head
        head.prev = node
        return node
    else:
        node = sortedInsert(head.next, data)
        head.next = node
        node.prev = head
        return head


def reverse(head):
    if not head:
        return head
    head.next, head.prev = head.prev, head.next
    if not head.prev:
        return head
    return reverse(head.prev)


def reverse2(head):
    curr = None
    while head:
        nxt = head.next
        curr = head
        head.next = head.prev
        head.prev = nxt
        head = nxt
    return curr


inputs = [1, 3, 4, 7, 10]
test_head = create_linked_list(inputs)
# print_list(test_head)

# print_list(sortedInsert(test_head, 5))
print_list(reverse2(test_head))
