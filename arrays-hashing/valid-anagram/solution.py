class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        sdic = {}
        tdic = {}

        for item in s:
            if item in sdic:
                sdic[item] += 1
            else:
                sdic[item] = 1

        for item in t:
            if item in tdic:
                tdic[item] += 1
            else:
                tdic[item] = 1
        
        if len(sdic) != len(tdic):
            return False
        
        for key, value in sdic.items():
            if key not in tdic:
                return False
            
            if value != tdic[key]:
                return False
        
        return True
