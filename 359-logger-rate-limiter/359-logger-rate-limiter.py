class Logger:

    def __init__(self):
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hashmap:
            self.hashmap[message] = timestamp
            return True
        
        if message in self.hashmap:
            if timestamp - self.hashmap[message] < 10:
                return False
            else:
                self.hashmap[message] = timestamp
                return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)