# space: creating up to n! new arrays for total permutations available
# plus linear space for recursive calls
# time: n! for generating up to all permutations
# utilizing tuples and a set to remove duplicate permutatins 

class Solution(object):
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, arr):
      results = set()
      self._permute(0, arr, results)
      return [list(x) for x in results]

    def _permute(self, start, arr, results):
      if start >= len(arr):
        results.add(tuple(arr))
      else:
        for i in range(start, len(arr)):
          self._swap(i, start, arr)
          self._permute(start+1, arr, results)
          self._swap(i, start, arr)

    def _swap(self, i, j, arr):
      tmp = arr[i]
      arr[i] = arr[j]
      arr[j] = tmp

s = Solution()
print(s.permute([1,1,2]))
# [[1, 2, 1], [2, 1, 1], [1, 1, 2]]
