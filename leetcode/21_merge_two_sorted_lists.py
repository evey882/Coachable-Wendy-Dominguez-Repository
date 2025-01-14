class ListNode:
    """Node Class"""
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    """Solution Class"""
    def mergeTwoLists(self, list1 , list2 ):
        """
            This problem requires a merge of two sorted linked lists, while maintaining the overall sorted order.
            The solution below makes use of a dummy node, to serve as a temporary head and traverses both lists
            verifying which value is less and putting that as the following node. It does this in O(n) time while maintaining O(1) space.
        """
        dummy_node = ListNode()
        curr = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 or list2

        return dummy_node.next