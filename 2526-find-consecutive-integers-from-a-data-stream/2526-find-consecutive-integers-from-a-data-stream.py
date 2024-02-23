class DataStream:

    def __init__(self, value: int, k: int):
        self.count = 0 
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count += 1
        else: 
            self.count = 0 
            
        return self.count >= self.k