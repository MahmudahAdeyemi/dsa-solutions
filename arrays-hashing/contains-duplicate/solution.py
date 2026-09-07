class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        mydict = {}
        for i in range(len(nums)):
            if(nums[i] in mydict):
                return True
            mydict[nums[i]] = 1
        return False