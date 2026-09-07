class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        if(len(s) ==0):
            return True
        i =0
        while(i<=len(t)-1):
            
            if(t[i] == s[count]):
                count +=1
            if(count == len(s)):
                return True
            i +=1
        return False