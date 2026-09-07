class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        ransomdic = {}
        magazinedic = {}
        for item in ransomNote:
            ransomdic[item] = ransomdic.get(item, 0) + 1
        
        for item in magazine:
            if(item in magazinedic):
                magazinedic[item] +=1
            else:
                magazinedic[item] =1
        
        for key,value in ransomdic.items():
            if(not(key in magazinedic)):
                return False
            if( magazinedic[key] < ransomdic[key]):
                return False
        return True