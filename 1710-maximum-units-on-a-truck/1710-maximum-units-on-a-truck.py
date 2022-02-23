class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_box = sorted(boxTypes, key = lambda x:x[1], reverse=True)
        
        result = 0
        num_box = 0
        
        for i in range(len(sorted_box)):
            for j in range(sorted_box[i][0]):
                res = sorted_box[i][1]
                if num_box + 1 <= truckSize:
                    result += res
                    num_box += 1
                    
        return result             