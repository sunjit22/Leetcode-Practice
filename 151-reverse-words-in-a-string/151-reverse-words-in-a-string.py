class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split()
        words_list.reverse()
        return " ".join(words_list)
            
        