class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for element in arr:
            if element in hashmap:
                hashmap[element] += 1
            else:
                hashmap[element] = 1

        counter = []
        for val in hashmap.values():
            counter.append(val)
            
        return len(counter) == len(set(counter))     