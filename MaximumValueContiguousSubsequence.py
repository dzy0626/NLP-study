"""Maximum Value Contiguous Subsequence. Given a sequence of n real numbers A(1) ... A(n), 
   determine a contiguous subsequence A(i) ... A(j) for which the sum of elements in the 
   subsequence is maximized."""
class Solution():
    def __init__(self, waitForSumSequence):
        self.waitForSumSequence = waitForSumSequence
        self.sumOfContiguousSubsequene = []

    def findGreatestSumOfSubArray(self):
        if self.waitForSumSequence == None:
            return None
        else:
            self.sumOfContiguousSubsequene.append(self.waitForSumSequence[0])
        for i in range(1, len(self.waitForSumSequence)):
            if self.sumOfContiguousSubsequene[i - 1] <= 0:
                self.sumOfContiguousSubsequene.append(self.waitForSumSequence[i])
            else:
                self.sumOfContiguousSubsequene.append( self.sumOfContiguousSubsequene[i-1] + self.waitForSumSequence[i])
        return max(self.sumOfContiguousSubsequene)        

import random
randomArray = [random.randint(-100,100) for i in range(10)]
array = Solution(randomArray)
print(randomArray)
print(array.findGreatestSumOfSubArray())