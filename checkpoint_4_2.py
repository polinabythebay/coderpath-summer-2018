class Solution:
    # @param A : list of integers
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
      arr = A
      if len(arr) == 1:
        return [-1]
      result = arr[:]
      result[len(result)-1] = -1 # we know what the end is

      # naive Solution
      # for every elt in array 
      # search the subarray in front of it 
      # and find the smallest positive difference
      # space is linear 
      # time is n^2
      for i in range(len(arr)-1):
        next_greater = None
        for j in range(i+1, len(arr)):
          if arr[j] > arr[i]:
            next_greater = arr[j]
            break
        if next_greater is None:
          result[i] = -1
        else:
          result[i] = next_greater
      return result
