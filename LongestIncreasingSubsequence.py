"""Given a sequence of n real numbers A(1) ... A(n), determine a subsequence (not necessarily 
   contiguous) of maximum length in which the values in the subsequence form a strictly increasing 
   sequence. """
def longestIncreasingSubsequence(array):
   subsequenceForEveryValue = [1]
   for i in range(1, len(array)):
      maxLength = 1
      for j in range(1, i+1):
         if array[i] > array[i-j]:
            subsequenceForAiValue = subsequenceForEveryValue[i-j] + 1
            if subsequenceForAiValue > maxLength:
               maxLength = subsequenceForAiValue
      subsequenceForEveryValue.append(maxLength)
   return max(subsequenceForEveryValue)

import random
randomArray = [random.randint(-100,100) for i in range(10)]
print(randomArray)
print(longestIncreasingSubsequence(randomArray))

