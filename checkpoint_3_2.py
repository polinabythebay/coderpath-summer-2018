
# Notes:

# - for 3B, check if there are pointers in CTCI about dealing with continuous subsequences 
#   - intended solution is to use three pointers, it's not obvious to think that way

# Given an array of non negative integers A, and a range (B, C), 
# find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C

# Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]
# where 0 <= i <= j < size(A)

# Example :

# A : [10, 5, 1, 0, 2]
# (B, C) : (6, 8)
# ans = 3 
# as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in the range [6, 8]

## Problem solving:

# this problems takes advantage of a sliding window done right (and optimal)
# this also does not work for negative values unfortunately, but it works for positive values.
# Correct solution that is fast enough to pass InterviewBit:
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
      # have three pointers 
      # so, start every range with every elt in array 
      # increment that range if within sum
      # if not within sum, break and start range at next element
      count = 0
      for i in range(len(A)):
        sum = 0
        for j in range (i, len(A)):
          sum += A[j]
          if sum >= B and sum <= C:
            # print(A[i], A[j])
            count += 1
          if sum > C:
            break
      return count

# =====================
# Previous Attempts 
# =====================

# NOTE: this solution breaks for negative values
# It's also way too complicated 
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
      num_in_range = 0
      start_index = 0
      end_index = 0
      arr = A
      sum_current = arr[0]
 
      while (start_index != len(arr)-1 or end_index != len(arr)-1):
        # do the check 
        if sum_current >= B and sum_current <= C:
          num_in_range += 1
          # print("current sum", sum_current)
          # print("current start", arr[start_index])
          # print("current end", arr[end_index])

        # all of this logic to determine if we 
        # should increment pointers breaks if 
        # the values can be negative
        if end_index == len(arr)-1:
          sum_current -= arr[start_index]
          start_index += 1
        elif sum_current >= B and sum_current <= C:
          end_index += 1
          sum_current += arr[end_index]
        elif sum_current < B:
          end_index += 1
          sum_current += arr[end_index]
        else:
          # if sum is greater than range 
          # and end_index is not at the end
          if end_index == start_index:
            end_index += 1
            start_index += 1
            sum_current = arr[end_index]
          else:
            sum_current -= arr[start_index]
            start_index += 1
      # do one last check for the last thing in the array 
      sum_current = arr[start_index]
      if sum_current >= B and sum_current <= C:
        num_in_range += 1
      return num_in_range

s = Solution()
print(s.numRange([10, 5, 1, 0, 2], 6, 8)) # 3
print(s.numRange([-2,5,-1], -2, 2)) # should be 3, breaks and returns 2

print(s.numRange([ 80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90 ], 99, 269)) # this is supposed to be 58 instead of 24, so my incrementing indexes is not working as expected, ugh


# ===========
# This version technically passes but it takes too long to run

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
      arr = A
      known_ranges = set()

      # I need the for loop because there are 
      # some subsets I skip because they happen to be 
      # contained within a few use cases 
      # this still breaks on negative numbers though!
      for i in range(len(arr)):
        num_in_range = i
        start_index = i
        end_index = i
        sum_current = arr[i]

        while (start_index != len(arr)-1 or end_index != len(arr)-1):
          # do the check 
          if sum_current >= B and sum_current <= C:
            if (start_index, end_index) not in known_ranges:
              known_ranges.add((start_index, end_index))
            # increment if we haven't seen this range before 
            # print("current sum", sum_current)
            # print("current start", arr[start_index])
            # print("current end", arr[end_index])

          # all of this logic to determine if we 
          # should increment pointers breaks if 
          # the values can be negative
          if end_index == len(arr)-1:
            sum_current -= arr[start_index]
            start_index += 1
          elif sum_current >= B and sum_current <= C:
            end_index += 1
            sum_current += arr[end_index]
          elif sum_current < B:
            end_index += 1
            sum_current += arr[end_index]
          else:
            # if sum is greater than range 
            # and end_index is not at the end
            if end_index == start_index:
              end_index += 1
              start_index += 1
              sum_current = arr[end_index]
            else:
              sum_current -= arr[start_index]
              start_index += 1
      # do one last check for the last thing in the array 
      sum_current = arr[start_index]
      if sum_current >= B and sum_current <= C:
        if (start_index, end_index) not in known_ranges:
          known_ranges.add((start_index, end_index))
      return len(known_ranges)
