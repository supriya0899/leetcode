# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ans = []

        for i in lists:
            head = i
            while head:
                ans.append(head.val)
                head = head.next
        
        ans.sort()

        cur = temp = ListNode()
        for i in ans:
            temp.next = ListNode(i)
            temp = temp.next
        return cur.next


        




        
            
