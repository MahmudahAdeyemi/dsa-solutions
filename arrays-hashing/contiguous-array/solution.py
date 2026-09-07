class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        runningsum = 0
        prefixsum = {0:-1}
        longest = 0
        for i in range(len(nums)):
            if(nums[i] == 0):
                nums[i] = -1
            runningsum +=nums[i]
            if(runningsum in prefixsum):
                if((i-prefixsum[runningsum]) > longest):
                    longest = i-prefixsum[runningsum]
            else:
                prefixsum[runningsum] =i
        return longest