# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = new_list = ListNode(0)

        while list1 or list2:

            if list1 and list2:
                if list1.val < list2.val:
                    new_list.next = list1
                    list1 = list1.next
                else:
                    new_list.next = list2
                    list2 = list2.next
            else:
                if list1 and not list2:
                    new_list.next = list1
                    list1 = list1.next
                elif list2 and not list1:
                    new_list.next = list2
                    list2 = list2.next

            new_list = new_list.next

        return dummy.next


def example_list1() -> ListNode:
    l3 = ListNode(3, None)
    l2 = ListNode(2, l3)
    return ListNode(1, l2)


def example_list2() -> ListNode:
    l3 = ListNode(3, None)
    l2 = ListNode(2, l3)
    return ListNode(1, l2)


def iterate_and_print(li: ListNode):
    while li is not None:
        print(li.val)
        li = li.next



iterate_and_print(Solution.mergeTwoLists(Solution, example_list1(), example_list2()))
