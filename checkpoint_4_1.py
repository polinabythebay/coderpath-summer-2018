import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
      self.val = x
      self.next = None
    
    def __str__(self):
      head = self
      result = []
      while (head.next is not None):
        result.append(str(head.val))
        head = head.next
      result.append(str(head.val))
      return " -> ".join(result)

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
      if A.next is None:
        return A
      result = tail = A
      size = 1
      values = []
      values.append(tail.val)
      while(tail.next):
        size += 1
        tail = tail.next
        values.append(tail.val)
      half = math.floor(size/2)
      tail = A 
      position = 0
      while(half > 0):
        half -= 1
        tail.val = values[len(values) - 1 - position] - tail.val 
        position += 1
        tail = tail.next
      return result

# 1 -> 2 -> 3 -> 4 -> 5
s = Solution()

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
# print(l1)

s.subtract(l1)
