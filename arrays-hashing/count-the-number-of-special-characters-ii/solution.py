class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 0
        lowercaselist = {}
        uppercaselist = {}
        for letter in word:
            if(letter.islower()):
                lowercaselist[letter] = lowercaselist.get(letter, 0) + 1
                if(letter.upper() in uppercaselist.keys()):
                    lowercaselist.pop(letter)
            else:
                uppercaselist[letter] = uppercaselist.get(letter, 0) + 1
        for key in lowercaselist.keys():
            if key.upper() in uppercaselist.keys():
                count+=1
        
        return count