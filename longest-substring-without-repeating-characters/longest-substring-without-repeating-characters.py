class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Approach 1
        if s=="":
            return 0
        array = list(s)
        count = 1
        result = []
        for i in range(len(array)):
            inner_count = 1
            inner_result = []
            inner_result.append(array[i])
            for j in range(i+1, len(array)):
                if array[j] in inner_result:
                    break
                else:
                    inner_result.append(array[j])
                    inner_count += 1
                    if(inner_count > count):
                        count = inner_count
                        result = inner_result
        return count      
        
        # Approach 2 - Need to fix
#         hash_map = {}
#         max_len = 0
#         for i in range(len(s)):
#             curr_len = 0
#             if s[i] in hash_map.keys():
#                 curr_len = i - hash_map[s[i]]
#                 max_len = max(max_len, curr_len)
#                 hash_map[s[i]] = i
#             else:
#                 hash_map[s[i]] = i
        
#         if max_len == 0:
#             return len(s)
#         return max_len         