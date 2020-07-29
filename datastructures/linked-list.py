# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def print_list(head):
    if head:
        print(head.data)
        print_list(head.next)


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
    return head


def insertNodeAtTail(head, value):
    if head is None:
        return Node(value)

    temp = head
    prevNode = None
    while temp is not None:
        prevNode = temp
        temp = temp.next
    prevNode.next = Node(value)
    return head


def insertNodeAtHead(head, value):
    if head is None:
        head = Node(value, None)
        return head
    newNode = Node(value, head)
    head = newNode
    return head


def insertNodeAtPosition(head, value, position):
    position += 1
    position_tail_continuity = None
    position_tail = head

    if position == 0:
        position_tail_continuity = head
        head = Node(value)
        head.next = position_tail_continuity
        return head
    else:
        for _ in range(1, position - 1):
            if position_tail.next is None:
                position_tail.next = Node(value)
                return head
            position_tail = position_tail.next
        position_tail_continuity = position_tail.next
        position_tail.next = Node(value)
        position_tail = position_tail.next
        position_tail.next = position_tail_continuity
        return head


def deleteNode(head, position):
    pass


inputs = [1, 2, 3, 4, 5, 6]
# inputs = [1, 2, 3]
test_head = create_linked_list(inputs)
# insertNodeAtPosition(test_head, 43, 2)
# test_head2 = insertNodeAtTail(test_head, 16)
print_list(test_head)

# while test_head is not None:
#     print(test_head.data)
#     test_head = test_head.next
