class Trie:

    def __init__(self):
        self.tree = {'*':'*'}

    def insert(self, word: str) -> None:
        current = self.tree
        for char in word:
            if char not in current:
                current[char] = dict()
            current = current[char]
        current['*'] = '*'    
            
    def search(self, word: str) -> bool:
        current = self.tree
        for char in word:
            if char not in current:
                return False
            current = current[char]
        if '*' in current:
            return True        
        return False

    
    def startsWith(self, prefix: str) -> bool:
        current = self.tree
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)