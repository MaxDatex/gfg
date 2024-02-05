'''
Given a sorted circular linked list of length n, the task is to insert a new node in this circular list so that it remains a sorted circular linked list.
'''


class Solution:
    def sortedInsert(self, head, data):
        temp = Node(data)
        
        # if head is None
        if not head:
            temp.next = temp
            return temp
            
        curr = head.next
        prev = head
        
        # Insert at the beginning
        if head.data >= data:
            while curr != head:
                prev = curr
                curr = curr.next
            prev.next = temp
            temp.next = curr
            return temp
        
        # Insert in the middle or at the end
        while data > curr.data:
            prev = curr
            curr = curr.next
            if curr == head:
                break

        prev.next = temp
        temp.next = curr
        return head
