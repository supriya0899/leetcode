# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        cur = head

        arr= []
        while head:
            arr.append(head.val)
            head = head.next
        
        arr1 = [arr[i] for i in range(len(arr)//2)]
        arr2 = [arr[i] for i in range(len(arr)//2, len(arr))]

        arr2 = arr2[::-1]

        ans = []

        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            ans.append(arr1[i])
            ans.append(arr2[j])
            i += 1
            j += 1
        
        if i < len(arr1):
            ans.append(arr1[i])
        
        if j < len(arr2):
            ans.append(arr2[j])
        
        i = 0
        while cur:
            cur.val = ans[i]
            i += 1
            cur = cur.next
        #print(ans)

        

        
          
