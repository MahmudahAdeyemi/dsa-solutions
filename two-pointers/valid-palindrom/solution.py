class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newword = s.replace(" ", "").replace(",", "").replace(":", "").replace("/","").replace(".", "").replace("@", "").replace("#", "").replace("_", "").replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("\\", "").replace("\"", "").replace("\'", "").replace("-", "").replace("?", "").replace(";", "").replace("!", "").replace("(", "").replace(")", "").replace("`", "").lower()
        left = 0
        right = len(newword) -1
        while(left<right):
            if(newword[right]!= newword[left]):
                return False
            left +=1
            right -=1
        return True