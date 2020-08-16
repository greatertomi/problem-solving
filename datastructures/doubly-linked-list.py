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
            tail.prev = head
            tail = tail.next
    return head


def print_list(head):
    if head:
        print(head.data, end=' <=> ')
        print_list(head.next)


def sortedInsert(head):
    while head:
        if head.next.data is None:
            print(head.data, 'prev ->', head.prev.data, 'next ->', 'None')
        elif head.prev.data is None:
            print(head.data, 'prev ->', 'None', 'next ->', head.next.data)
        else:
            print(head.data, 'prev ->', head.prev.data, 'next ->', head.next.data)
        head = head.next


inputs = [1, 3, 4, 7, 10]
test_head = create_linked_list(inputs)
# print_list(test_head)

sortedInsert(test_head)
