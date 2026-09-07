class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        currentsum = 0
        minimumvalue = 0
        left = 0
        for right in range(len(nums)):
            currentsum += nums[right]
            while(currentsum >= target):
                currentsum -= nums[left]
                newmin = right-left +1
                left +=1
                if(minimumvalue == 0):
                    minimumvalue = newmin
                else:
                    minimumvalue = min(newmin,minimumvalue)
        return minimumvalue