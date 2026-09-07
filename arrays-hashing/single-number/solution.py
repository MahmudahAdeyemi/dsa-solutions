class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydic = {}
        for item in nums:
            if(item in mydic):
                mydic[item] += 1
            else:
                mydic[item] = 1
        for key,value in mydic.items():
            if(value == 1):
                return key