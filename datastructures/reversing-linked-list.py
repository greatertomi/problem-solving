def reverseRecursive(head):
    if head is None or head.next is None:
        return head

    reverseRecursive(head.next)
    tailNode = head.next
    tailNode.next = head

    head.next.next = head
    head.next = None


def reverseIterative(head):
    if head is None or head.next is None:
        return head

    alreadyReversed, current = head, head.next
    alreadyReversed.next = None

    while current is not None:
        storePtr = current
        current.next = alreadyReversed

        alreadyReversed = current
        current = storePtr

    return alreadyReversed
