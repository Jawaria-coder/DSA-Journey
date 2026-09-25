### 1. Insert at start
def insertAtFront(head, x):
    newNode = Node(x)
    newNode.next = head
    return newNode

### 2. Insert at end
def insertAtEnd(head, x):
    newNode = Node(x)

    if head is None:
        return newNode

    last = head

    while last.next is not None:
        last = last.next
    last.next = newNode

    return head

### 3. Insert after a given Node
def insertAfter(head, target, x):
    curr = head

    while curr is not None:
        if curr.data == target:
            newNode = Node(x)
            newNode.next = curr.next
            curr.next = newNode
            break

        curr = curr.next

    return head

### 4. Insert before a given Node
def insertBefore(head, target, x):
    if head is None:
        return head

    if head.data == target:
        newNode = Node(x)
        newNode.next = head
        return newNode

    curr = head

    while curr.next is not None:
        if curr.next.data == target:
            newNode = Node(x)
            newNode.next = curr.next
            curr.next = newNode
            break

        curr = curr.next

    return head

### 5. Insert at specific Pos
def insertPos(head, pos, val):

    if pos < 1:
        return head

    if pos == 1:
        newNode = Node(val)
        newNode.next = head
        return newNode

    curr = head

    for i in range(1, pos - 1):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head

    newNode = Node(val)
    newNode.next = curr.next
    curr.next = newNode

    return head