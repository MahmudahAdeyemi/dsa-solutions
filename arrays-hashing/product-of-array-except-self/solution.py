class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftproduct = [1]
        for i in range(1,len(nums)):
            leftproduct.append(leftproduct[i-1] * nums[i-1])
            
        rightproduct = 1
        for i in range(len(nums)-1,-1,-1):
            leftproduct[i] *= rightproduct
            rightproduct *= nums[i]
        
        return leftproduct