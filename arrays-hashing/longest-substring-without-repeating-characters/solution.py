class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        left = 0
        lenght = 0
        for right in range(len(s)):
            
            while(s[right] in window):
                window.remove(s[left])
                left +=1
            lenght = max(lenght, (right-left +1))
            window.add(s[right])
        return lenght
        