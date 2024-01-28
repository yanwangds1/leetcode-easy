from typing import Optional

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def mergeTwolists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.value < list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1 is not None:
            current.next = list1
        if list2 is not None:
            current.next = list2

        return dummy.next

# Test example
def print_linked_list(head: Optional[ListNode]):
    while head is not None:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Creating two sorted linked lists
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

# Creating an instance of the Solution class
solution = Solution()

# Merging the two lists using the mergeTwoLists method
merged_list = solution.mergeTwolists(list1, list2)

# Printing the original lists and the merged list
print("List 1:")
print_linked_list(list1)

print("\nList 2:")
print_linked_list(list2)

print("\nMerged List:")
print_linked_list(merged_list)