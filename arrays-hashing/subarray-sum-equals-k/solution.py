class Solution(object):
    def subarraySum(self, nums, k):
        prefixsum = 0
        freq = {0: 1}
        count = 0

        for num in nums:
            prefixsum += num
            if (prefixsum - k) in freq:
                count += freq[prefixsum - k]
            freq[prefixsum] = freq.get(prefixsum, 0) + 1
        return count