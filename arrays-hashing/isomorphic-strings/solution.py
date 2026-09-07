class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sdic ={}
        tdic = {}
        for i in range(len(s)):
            if(s[i] in sdic):
                if(sdic[s[i]] != t[i]):
                    return False
            if(t[i] in tdic):
                if(tdic[t[i]] != s[i]):
                    return False
            sdic[s[i]] = t[i]
            tdic[t[i]] = s[i]
        return True


