class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        window_sum = 0
        count =0
        for i in range(k):
            window_sum+= arr[i]
        if((window_sum/k)>= threshold):
            count+=1
        for i in range(k,len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            if((window_sum/k)>= threshold):
                count+=1
        return count

        