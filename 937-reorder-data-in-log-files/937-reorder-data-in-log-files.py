class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letter_logs = []
        digit_logs = []
        result = []
        for i in range(len(logs)):
            log = logs[i].split()
            check_log = log[1]
            
            if log[1].isdigit():
                digit_logs.append(logs[i])
            else:
                letter_logs.append(logs[i])
                
        letter_logs.sort(key=lambda s: (s.split()[1],s.split()[2:], s.split()[0]))
        
        for let in letter_logs:
            result.append(let)
            
        for dig in digit_logs:
            result.append(dig)    
        return result