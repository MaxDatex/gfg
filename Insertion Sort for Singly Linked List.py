'''
Given a singly linked list, sort the list (in ascending order) using insertion sort algorithm.
'''


class Solution:
    def insertionSort(self, head):
        if not head or not head.next:
            return head
        
        res = Node(-1)
        res.next = head
        while(head.next):
            if head.next.data<head.data:
                cur = head.next
                head.next=head.next.next
                ptr = res.next
                prev = res
                while(ptr.data<cur.data):
                    prev = ptr
                    ptr = ptr.next
                prev.next = cur
                cur.next = ptr
                continue
            head=head.next
                
        return res.next


# Took too much time
class Solution:
    def insertionSort(self, head):
        if not head or head.next == None:
            return head
            
        dummy = Node(float('-inf'))
        
        dummy.next = head
        curr = dummy.next
        n = j = 0
        
        while curr:
            n = j
            node = dummy.next
            temp = dummy
            while curr.data >= node.data and n:
                temp = node
                node = node.next
                n -= 1
               
            j += 1
            
            temp.next = curr
            next_curr = curr.next
            curr.next = node
            
            while n > 1:
                node = node.next
                n -=1
            
            curr = next_curr
            node.next = curr
            
        head = dummy.next
        return head
