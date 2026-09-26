### 1. Insert At Front
def insert_at_front(head, new_data):
    new_node = Node(new_data)

    new_node.next = head

    if head is not None:
        head.prev = new_node

    return new_node

### 2. Insert At End
def insertEnd(head, new_data):
    new_node = Node(new_data)
    
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr
    
    return head

### 3. Insert after the pos (index)
def insertAtPos(head, p, x):
    newnode = Node(x)
    cur = head

    for i in range(p):
        cur = cur.next

    if cur.next is None:
        cur.next = newnode
        newnode.prev = cur
    else:
        newnode.next = cur.next
        cur.next = newnode
        newnode.next.prev = newnode
        newnode.prev = cur
    return head
