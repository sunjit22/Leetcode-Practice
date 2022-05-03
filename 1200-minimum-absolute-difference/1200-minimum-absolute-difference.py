class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum_index = []
        minimum = float('inf')
        for i in range(1,len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if diff < minimum:
                minimum = diff
                minimum_index.clear()
                minimum_index.append([arr[i-1],arr[i]])
            elif diff == minimum:
                 minimum_index.append([arr[i-1],arr[i]])
                    
        return minimum_index            

        