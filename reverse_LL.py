# Time Complexity : O(n), where n is the number of nodes in the list
# Space Complexity : O(1) for iterative, O(n) for recursive due to call stack
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Iterative approach
def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # Store next
        curr.next = prev       # Reverse current node's pointer
        prev = curr            # Move pointers one step forward
        curr = next_node
    return prev

# Recursive approach
def reverseListRecursive(head):
    if not head or not head.next:
        return head
    new_head = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
