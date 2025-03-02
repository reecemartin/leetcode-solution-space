# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        if head.next == None:
            return None
        last_n_nodes = []
        while head.next != None:
            if len(last_n_nodes) < n + 1:
                last_n_nodes.append(head)
            else:
                last_n_nodes.pop(0)
                last_n_nodes.append(head)
            head = head.next

        if len(last_n_nodes) < n + 1:
            last_n_nodes.append(head)
        else:
            last_n_nodes.pop(0)
            last_n_nodes.append(head)
        head = head.next

        if head == None and len(last_n_nodes) < n + 1:
            return last_n_nodes[1]
        target = last_n_nodes[0].next
        last_n_nodes[0].next = target.next
        target.next = None
        return first
