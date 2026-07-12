class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. Store all nodes in an array (use a copy variable 'curr' so 'head' isn't lost)
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        # 2. Use two pointers to link them in the zigzag pattern
        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            
            # If pointers met, stop to avoid linking a node to itself
            if left == right:
                break
                
            nodes[right].next = nodes[left]
            right -= 1
            
        # 3. Terminate the list cleanly to avoid cycles
        nodes[left].next = None
