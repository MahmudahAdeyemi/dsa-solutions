class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedsquare = [0]*len(nums)
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        while((left<right) or (index >=0)):
            if((abs(nums[left])) > (abs(nums[right]))):
                sortedsquare[index] = nums[left] **2
                left +=1
            else:
                sortedsquare[index] = nums[right] **2
                right -=1
            index -=1
        return sortedsquare
        
