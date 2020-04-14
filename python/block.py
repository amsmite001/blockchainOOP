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
        self.chain = []
        self.setGenesisBlock(1,100)
    def initBlock(self,previousHash):
        block = {
            'index': len(self.chain)+1,
            'timestamp' : time(),
            'transaction': self.transaction
            'previousHash': previousHash or self.hash(self.chain[-1])
            }
        
        self.chain.append(block)
        return block
    def setGenesisBlock(self):
        genesis_Block = initBlock(
    def calcHash(self):
        return str(hashlib.sha256(self.index + self.prevoiusHash + self.timestamp + self.data))
