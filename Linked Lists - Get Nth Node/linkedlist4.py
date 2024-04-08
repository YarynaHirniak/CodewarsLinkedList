from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if node is None:
        raise ValueError
    if index < 0:
        raise ValueError
    head = node
    count = 0
    while count!=index:
        head = head.next
        count+=1
        if head==None:
            raise IndexError
    return head
