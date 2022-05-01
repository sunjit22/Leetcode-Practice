class Solution:
    def countPoints(self, rings: str) -> int:
        hashmap = {}
        for i in range(len(rings)):
            if rings[i].isdigit():
                if rings[i] in hashmap:
                    hashmap[rings[i]].append(rings[i-1])
                else:    
                    hashmap[rings[i]] = [rings[i-1]]
           
        count = 0
        for key,value in hashmap.items():
            if "R" in hashmap[key] and "G" in hashmap[key] and "B" in hashmap[key]:
                count += 1
                
        return count        
        