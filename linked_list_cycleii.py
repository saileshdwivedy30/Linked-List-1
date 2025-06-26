# Time Complexity : O(n), where n is the number of nodes in the list
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # First step: detect if a cycle exists using Floyd's cycle detection
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Cycle detected, now find the entry point
                start = head
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start

        # No cycle
        return None
