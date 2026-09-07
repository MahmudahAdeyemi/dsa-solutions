class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        left = 0
        lenth =0
        max_freq=0
        for right in range(len(s)):
            if(s[right] in count):
                count[s[right]]+=1
            else:
                count[s[right]] = 1
            max_freq = max(max_freq, count[s[right]])
            while((right-left+1)-max_freq > k):
                
                if(count[s[left]]!=0):
                    count[s[left]]-=1
                left+=1
            lenth = max(lenth,right-left+1)
        return lenth