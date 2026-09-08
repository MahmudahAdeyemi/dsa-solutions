class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        results = []
        for word in words:
            mydic = {}
            check = True
            for i in range (len(word)):
                if(pattern[i] in mydic):
                    if(mydic[pattern[i]] != word[i]):
                        check = False
                        break
                elif((word[i] in mydic.values()) and not (pattern[i] in mydic)):
                    check = False
                    break
                else:
                    mydic[pattern[i]] = word[i]
            if(check):
                results.append(word)
        return results