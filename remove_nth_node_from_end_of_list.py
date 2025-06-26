# Time Complexity : O(sz), where sz is the number of nodes in the list
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy

    # Move fast pointer n+1 steps ahead to maintain a gap
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the nth node from end
    slow.next = slow.next.next

    return dummy.next
