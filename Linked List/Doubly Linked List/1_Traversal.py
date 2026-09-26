## Forward Traversal
def forward_traversal(head):
    curr = head
    while curr is not None:
        
        print(curr.data, end=" ")
        curr = curr.next
    
    print()


## Backward Traversal
def backward_traversal(Tail):
    curr = Tail
    while curr is not None:
        
        print(curr.data, end=" ")
        curr = curr.prev
    
    print()


## Time: O(n)
## Space: O(1)