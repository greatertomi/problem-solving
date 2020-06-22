# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def print_list(head):
    if head:
        print(head.data)
        print_list(head.next)
