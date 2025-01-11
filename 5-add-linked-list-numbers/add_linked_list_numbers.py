#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class SolutionListIntList:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse_linked_list(l):
            cur_node = l
            next_node = cur_node.next
            prev_node = None
            while cur_node.next != None:
                cur_node.next = prev_node
                prev_node = cur_node
                cur_node = next_node
                next_node = cur_node.next
                # print("running \n")
            cur_node.next = prev_node
            
            return cur_node


        def linked_list_to_integer(l: ListNode):
            head = l
            num = 0
            digits = []

            while l.next != None:
                # print(digits)
                # print(l.val)
                # print(str(l.next.val) + "\n")
                digits.append(l.val)
                l = l.next
            digits.append(l.val)
            # print(digits)

            for index, digit in enumerate(digits):
                num += digit * (10 ** (len(digits) - index - 1))
                # print(num)
            
            return num
        
        def integer_to_linked_list(num):
            if num == 0:
                return ListNode()
            else:
                digits = str(num)
                head_node = ListNode(int(digits[0]))
                last_node = head_node
                for digit in digits[1:]:
                    last_node.next = ListNode(int(digit))
                    last_node = last_node.next
                return head_node
                
        num_1 = linked_list_to_integer(reverse_linked_list(l1))
        # num_1_r = reverse_linked_list(l1)
        # print(linked_list_to_integer(num_1_r))
        # print(num_1)
        num_2 = linked_list_to_integer(reverse_linked_list(l2))
        # print(num_2)
        # print(linked_list_to_integer(integer_to_linked_list(num_1 + num_2)))
        return reverse_linked_list(integer_to_linked_list(renum_1 + num_2))
    
Solution.addTwoNumbers(Solution, ListNode(1, ListNode(2, ListNode(3, None))), ListNode(1, ListNode(1,ListNode(1, None))))
