# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def shouter():
    print('This is linked list class')


def print_list(head):
    if head:
        print(head.data, end=' ')
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


def printInReverse(head):
    if head is None:
        return

    printInReverse(head.next)
    print(head.data)


def reverse_iterative(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    head = prev
    return head


def compare_lists(list1, list2):
    if list1 is None and list2 is None:
        return 1
    elif list1 is None or list2 is None:
        return 0

    outcome = 0
    while list1 and list2:
        if list1.data != list2.data:
            outcome = 0
            break
        else:
            outcome = 1
        list1 = list1.next
        list2 = list2.next
    return outcome


def mergeLists(list1, list2):
    combinedArray = []
    while list1:
        combinedArray.append(list1.data)
        list1 = list1.next

    while list2:
        combinedArray.append(list2.data)
        list2 = list2.next
    newHead = create_linked_list(sorted(combinedArray))
    return newHead


def getListLength(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def getNodeFromTail(head, pos):
    headLength = getListLength(head) - 1
    adjustedPos = headLength - pos
    count = 0
    while head:
        if count == adjustedPos:
            return head.data
        count += 1
        head = head.next


def detectCycle(head):
    s = set()
    temp = head
    while temp:
        if temp in s:
            return 1
        s.add(temp)
        temp = temp.next
    return 0


def removeDuplicates(head):
    unique = set()
    while head:
        if head.data not in unique:
            unique.add(head.data)
        head = head.next
    print(unique)


inputs = [1, 2, 3, 3, 5, 6, 6, 7]
inputs2 = [1, 2, 10]
test_head = create_linked_list(inputs)
removeDuplicates()

