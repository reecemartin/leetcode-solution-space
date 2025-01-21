#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class SolutionListIntList:
    def add_two_numbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
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
    
class SolutionListAddition:
    def add_two_numbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur_node_1, cur_node_2 = l1, l2
        carry_over = 0
        while cur_node_1 != None and cur_node_2 != None:
            # print(cur_node_1.val)
            # print(cur_node_2.val)
            value = cur_node_1.val + cur_node_2.val + carry_over
            # print(value)
            # print("\n")

            if value > 10:
                carry_over = value // 10
            elif value == 10:
                carry_over = 1
            else:
                carry_over = 0

            cur_node_1.val = value % 10
            cur_node_1, cur_node_2 = cur_node_1.next, cur_node_2.next

        # print("Middle")

        if carry_over != 0 and cur_node_2 == None and cur_node_1 == None:
            cur_node_1 = l1

            while cur_node_1.next != None:
                cur_node_1 = cur_node_1.next

            cur_node_1.next = ListNode(carry_over, None)

        elif cur_node_1:

            while cur_node_1:
                print(carry_over)
                print(cur_node_1.next)
                if cur_node_1.next == None:
                    value = (cur_node_1.val + carry_over)
                    cur_node_1.val = value % 10
                    cur_node_1.next = ListNode(value // 10, None)
                    return l1
                elif cur_node_1.val + carry_over > 9:
                    print("Active")
                    value = cur_node_1.val + carry_over
                    cur_node_1.val = (value) % 10
                    carry_over = (value) // 10
                else:
                    pass
                # print("Rest of Item")
                # print(cur_node_2.val + carry_over)
                    carry_over = 0
                cur_node_1 = cur_node_1.next

        elif cur_node_2:
            cur_node_1, cur_node_2 = l1, l2

            while cur_node_1.next != None and cur_node_2.next != None:
                cur_node_1 = cur_node_1.next
                cur_node_2 = cur_node_2.next

            while cur_node_2:
                if cur_node_2.val + carry_over > 9:
                    cur_node_1.next = ListNode((cur_node_2.val + carry_over) // 10)
                    carry_over = carry_over % 10
                else:
                    cur_node_1.next = ListNode(cur_node_2.val + carry_over)
                # print("Rest of Item")
                # print(cur_node_2.val + carry_over)
                    carry_over = 0
                cur_node_1, cur_node_2 = cur_node_1.next, cur_node_2.next

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

        print(465 + 742)
        print(11 % 10)
        print(linked_list_to_integer(l1))
        return l1
    
SolutionListAddition.add_two_numbers_2(SolutionListAddition, ListNode(2, ListNode(4, ListNode(3, None))), ListNode(5, ListNode(6,ListNode(4, None))))