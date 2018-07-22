# faster solution:

class Solution(object):
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
      nums = {x:None for x in A}
      result = 0
      for key in nums:
        # check if it is the first elt in the sequence 
        # by seeing if it's previous elt is in nums
        if key-1 in nums:
          continue 
        else:
          result = max(result, self._getSeq(nums, key, 0))
      return result
    
    def _getSeq(self, nums, key, size):
      while key in nums:
        size += 1
        key += 1
      return size

##### Previous solution attempt

class Solution(object):
    # @param A : tuple of integers
    # @return an integer

    # this works, but it's slow 

    # perfectly valid solution but it's too slow
    def longestConsecutive(self, A):
      nums = {x:None for x in A}
      result = 0
      for key in nums:
        current_seq = self._getSeq(nums, key, 0)
        nums[key] = current_seq
        result = max(result, current_seq)
      return result
    
    def _getSeq(self, nums, key, size):
      if key not in nums:
        return size 
      else:
        if nums[key] is not None:
          return size + nums[key]
        else:
          return self._getSeq(nums, key+1, size+1)

s = Solution()
result = s.longestConsecutive([4, 3, 2, 1])
print(result)
# 4
