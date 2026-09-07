class Solution(object):
    def convert_to_dict(self, s, start, k):
        result = {}

        for char in s[start:start + k]:
            result[char] = result.get(char, 0) + 1

        return result

    def checkInclusion(self, s1, s2):
        k = len(s1)

        if k > len(s2):
            return False

        dic1 = self.convert_to_dict(s1, 0, k)
        dic2 = self.convert_to_dict(s2, 0, k)
        if(dic1 == dic2):
            return True
        for i in range(k,len(s2)):
            if(s2[i] in dic2):
                dic2[s2[i]] +=1
            else:
                dic2[s2[i]] =1
            dic2[s2[i-k]] -=1
            if(dic2[s2[i-k]] == 0):
                del (dic2[s2[i-k]])
            if(dic1 == dic2):
                return True
            
        return False