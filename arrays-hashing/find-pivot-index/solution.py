class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalsum = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            rightsum = totalsum-leftsum-nums[i]
            if(rightsum==leftsum):
                return i
            leftsum+=nums[i]
        return (-1)