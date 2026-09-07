class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if(len(pattern) != len(words)):
            return False
        mydic = {}
        for i in range (len(pattern)):
            if(pattern[i] in mydic):
                if(mydic[pattern[i]] != words[i]):
                    return False

            elif((words[i] in mydic.values()) and not (pattern[i] in mydic)):
                return False
            else:
                mydic[pattern[i]] = words[i]
        return True