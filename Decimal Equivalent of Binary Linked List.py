'''
Given a singly linked list of length n. The link list represents a binary number, ie- it contains only 0s and 1s. Find its decimal equivalent.
The significance of the bits decreases with the increasing index in the linked list.
An empty linked list is considered to represent the decimal value 0. 

Since the answer can be very large, answer modulo 109+7 should be printed.
'''


class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        res = 0
        while head:
            res = (res * 2 + head.data) % MOD
            head = head.next
        return res


# Bitmagic
class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        res = head.data
        while head.next:
            res = (res << 1) | head.next.data
            head = head.next
            res %= MOD
        return res
