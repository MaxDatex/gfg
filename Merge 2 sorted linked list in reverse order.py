'''
Given two linked lists of size N and M, which are sorted in non-decreasing order. 
The task is to merge them in such a way that the resulting list is in non-increasing order.
'''


def reverse(h):
    prev = None
    current = h
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


class Solution:
    def mergeResult(self, h1, h2):
        
        if h1 == None:
            return reverse(h2)
        if h2 == None:
            return reverse(h1)
            
        if h1.data > h2.data:
            h2, h1 = h1,h2
            
        if h1.next == None:
            h1.next = h2
            return reverse(h1)
            
        curr1 = h1
        next1 = h1.next
        curr2 = h2
        next2 = h2.next
        
        while (next1 != None) and (curr2 != None):
            
            if (curr1.data <= curr2.data) and (next1.data >= curr2.data):
                next2 = curr2.next
                curr1.next = curr2
                curr2.next = next1
                
                curr1 = curr2
                curr2 = next2
                
            else:
                if (next1.next):
                    next1 = next1.next
                    curr1 = curr1.next
                else:
                    next1.next = curr2
                    return reverse(h1)
        return reverse(h1)
