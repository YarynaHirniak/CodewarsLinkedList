class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None or head.next is None:
        return head
    
    prev_node = None
    current_node = head
    next_node = None
    
    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    
    return prev_node
