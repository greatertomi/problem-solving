def compareLists(headA, headB):
    while True:
        # both nodes are None
        if (not headA) and (not headB): return 1
        # only one node is None or node data differs
        if (bool(headA) != bool(headB)) or (headA.data != headB.data): return 0
        headA = headA.next
        headB = headB.next
