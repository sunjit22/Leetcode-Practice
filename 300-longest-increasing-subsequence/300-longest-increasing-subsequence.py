class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:   
        sub = [nums[0]]
        
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)
        
        
        
#         nums_sorted = sorted(set(nums))
#         return self.lcs(nums, nums_sorted, len(nums), len(nums_sorted))
        
#     def lcs(self,arr_1, arr_2, m, n):
#         if m == 0 or n == 0:
#             return 0
#         elif arr_1[m-1] == arr_2[n-1]:
#             return 1 + self.lcs(arr_1, arr_2, m-1, n-1)
#         else:
#             return max(self.lcs(arr_1, arr_2, m-1, n), self.lcs(arr_1, arr_2, m, n-1))