import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from com.enigmagpt.learning.leetcode.algo.merge_two_sorted_lists_21 import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next == None:
            return None

        node = head

        count = Solution.countList(Solution, node)

        middle = math.ceil(count / 2)

        i = 0
        prevNode = None
        while i != middle:
            prevNode = node
            node = node.next
            i += 1

        nextNode = node.next

        Solution.remove(Solution, prevNode, node, nextNode)

        return head


    def countList(self, node):
        count = 0
        while node.next != None:
            count += 1
            node = node.next
        return count


    def remove(self, prevNode, node, nextNode):
        if nextNode == None:
            prevNode.next = None
        else:
            prevNode.next = nextNode
