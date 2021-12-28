class Solution:
    def maxLen(self, n, arr):
        #Code here
        hash_map = dict()
        longest = 0
        summation = 0
        for i in range(len(arr)):
            curr_longest = 0
            summation += arr[i]
            if summation == 0:
                longest = i + 1
            else: 
                if summation in hash_map.keys():
                    curr_longest = i - hash_map[summation]
                    longest = max(curr_longest, longest)
                else:
                    hash_map[summation] = i

        return longest 
