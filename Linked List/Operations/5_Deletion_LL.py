### 1. Deletion at Start
def deleteHead(head):

    if head is None:
        return None

    temp = head
    head = head.next
    temp = None

    return head

### 2. Deletion at End
def removeLastNode(head):
    if head is None:
        return None

    if head.next is None:
        return None

    secondLast = head
    while secondLast.next.next is not None:
        secondLast = secondLast.next

    secondLast.next = None

    return head

### 3. Deletion at given pos
def deleteAtPosition(head, pos):
    if head is None or pos < 1:
        return None

    if pos == 1:
        head = head.next
        return head

    curr = head

    for i in range(1, pos):
        prev = curr
        curr = curr.next

        if curr is None:
            return head

    prev.next = curr.next

    return head

### 4. Delete a Linked List
def deleteLinkedList(head):
    head = None
    return head