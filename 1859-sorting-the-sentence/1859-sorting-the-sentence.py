class Solution:
    def sortSentence(self, s: str) -> str:
        sent_list = s.split(" ")
        sent_list.sort(key = lambda s : s[-1])
        for i in range(len(sent_list)):
            sent_list[i] = sent_list[i][0:-1]
        return " ".join(sent_list)
             
        