# Find the kth smallest element in an unsorted array of non-negative integers.

# Definition of kth smallest element

#  kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
# In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based ) 
# NOTE
# You are not allowed to modify the array ( The array is read only ). 
# Try to do it using constant extra space.

# Example:

# A : [2 1 4 3 2]
# k : 3

# answer : 2

# strategy:
# loop through the array k times 
# first time find highest element and keep track of it 
# next time, I want to find an element that is not that 
# element but is the highest element 
# keep a hash of previous elements of size k-1 for constant lookup 
# current highest element is updated for every loop 
# after finding current highest element the kth time, return index

# time K * n where n in length of array 
# space: additional hash of up to size n, so space is linear

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, arr, k):
      if k == 0:
        return 0
      prev_smallest = {}

      while(k > 0):
        k -= 1
        current_smallest = float('inf')
        current_index = -1
        for i in range(len(arr)):
          # if elt is already considered smallest, skip
          if i in prev_smallest:
            continue
          else:
            if current_smallest > arr[i]:
              current_smallest = arr[i]
              current_index = i
        prev_smallest[current_index] = True
      return current_smallest

s = Solution()
print(s.kthsmallest([2,1,4,3,2], 3))

# smallest: 1 
# current_smallest = 2 
# add 2 to prevs 
