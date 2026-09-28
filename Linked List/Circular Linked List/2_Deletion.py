### 1. At Front

# Last
def deleteAtBeginning(tail):

    if tail is None:
        return None

    head = tail.next

    if head == tail:
        return None

    tail.next = head.next

    return tail

# Head
def deleteAtBeginning(head):

    if head is None:
        return None

    if head.next == head:
        return None

    tail = head

    while tail.next != head:
        tail = tail.next

    head = head.next
    tail.next = head

    return head


### 2. At End

# Last
def deleteAtEnd(tail):

    if tail is None:
        return None

    head = tail.next

    if head == tail:
        return None

    curr = head

    while curr.next != tail:
        curr = curr.next

    curr.next = head
    tail = curr

    return tail

# Head
def deleteAtEnd(head):

    if head is None:
        return None

    if head.next == head:
        return None

    curr = head

    while curr.next.next != head:
        curr = curr.next
    curr.next = head

    return head

### 3. At a Pos

# Last
def deleteAtPosition(tail, pos):

    if tail is None:
        return None

    head = tail.next

    if pos < 1:
        return tail

    if pos == 1:
        return deleteAtBeginning(tail)

    curr = head

    for i in range(1, pos - 1):
        curr = curr.next
        if curr == head:
            return tail

    nodeToDelete = curr.next

    if nodeToDelete == head:
        return tail

    curr.next = nodeToDelete.next

    if nodeToDelete == tail:
        tail = curr

    return tail


# Head 
def deleteAtPosition(head, pos):

    if head is None:
        return None

    if pos < 1:
        return head

    if pos == 1:
        return deleteAtBeginning(head)

    curr = head

    for i in range(1, pos - 1):
        curr = curr.next

        if curr == head:
            return head

    nodeToDelete = curr.next

    if nodeToDelete == head:
        return head

    curr.next = nodeToDelete.next

    return head