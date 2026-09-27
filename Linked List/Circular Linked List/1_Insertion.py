### 1. At Front

# Last
def insertAtBeginning(last, key):
    newNode = Node(key)

    if last is None:
        newNode.next = newNode
        return newNode

    newNode.next = last.next
    last.next = newNode

    return last

# Head
def insertAtBeginning(head, key):
    newNode = Node(key)

    # Empty list
    if head is None:
        newNode.next = newNode
        return newNode

    # Find the last node
    curr = head
    while curr.next != head:
        curr = curr.next

    # Insert new node before head
    newNode.next = head
    curr.next = newNode

    # New node becomes the head
    head = newNode

    return head

### 2. At end

# Last
def insertAtEnd(tail, key):

    newNode = Node(key)

    if tail is None:
        newNode.next = newNode
        return newNode

    newNode.next = tail.next
    tail.next = newNode

    return newNode

# Head
def insertAtEnd(head, key):
    newNode = Node(key)

    # Empty list
    if head is None:
        newNode.next = newNode
        return newNode

    # Find the last node
    curr = head
    while curr.next != head:
        curr = curr.next

    # Insert new node after last
    curr.next = newNode
    newNode.next = head

    return head

### 3. Insert after Specific Pos

# Last
def insertAtPosition(last, pos, key):
    newNode = Node(key)

    # Empty list
    if last is None:
        if pos == 1:
            newNode.next = newNode
            return newNode
        return last

    # Insert at beginning
    if pos == 1:
        newNode.next = last.next
        last.next = newNode
        return last

    # Find node before the required position
    curr = last.next

    for i in range(1, pos - 1):
        curr = curr.next

        # We have gone around the circular list
        if curr == last.next:
            return last

    newNode.next = curr.next
    curr.next = newNode

    return last

# Head
def insertAtPosition(head, pos, key):
    newNode = Node(key)

    # Empty list
    if head is None:
        if pos == 1:
            newNode.next = newNode
            return newNode
        return head

    # Insert at beginning
    if pos == 1:
        curr = head

        # Find last node
        while curr.next != head:
            curr = curr.next

        newNode.next = head
        curr.next = newNode

        return newNode

    # Find node before the required position
    curr = head

    for i in range(1, pos - 1):
        curr = curr.next

        # We have gone around the list
        if curr == head:
            return head

    newNode.next = curr.next
    curr.next = newNode

    return head
