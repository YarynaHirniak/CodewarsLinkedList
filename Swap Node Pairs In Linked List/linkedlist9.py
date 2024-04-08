from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    
    node1 = Node(0)
    node1.next = head
    prev = node1

    while prev.next and prev.next.next:
        first_node = prev.next
        second_node = first_node.next

        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        prev = first_node

    return node1.next
