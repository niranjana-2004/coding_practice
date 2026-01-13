from typing import Optional

class ListNode:    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    current.next = list1 if list1 else list2
    return dummy.next

def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
if __name__ == "__main__":
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    merged = mergeTwoLists(list1, list2)
    print_linked_list(merged)
