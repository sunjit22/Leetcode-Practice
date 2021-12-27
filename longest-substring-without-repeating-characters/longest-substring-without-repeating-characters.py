class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
                
                