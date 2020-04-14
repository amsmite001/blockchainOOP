import hashlib
import time

class Block:
    def __init__(self, index, data, timestamp, prevhashS):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.hashS = self.calcHash()
        self.prevhashS = prevhashS
    def calcHash(self):
        return str(hashlib.sha256(self.index + self.prevoiusHash + self.timestamp + self.data))

class Blockchain:
    def __init__(self):
        
