import hashlib
import datetime

class Block():
    def __init__(self, index, data, timestamp, prevhashS):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.hashS = self.calcHash()
        self.prevhashS = prevhashS

    def calcHash(self):
        return hashlib.sha256(self.index + self.prevoiusHash + self.timestamp + self.data).hexdigest()

class Blockchain():
    def __init__(self):
        self.chain = [self.setGenesisBlock()]

    def setGenesisBlock(self):
        return Block(0,datetime.datetime.utcnow(), 'Genesis', '0')

    def addBlock(self, data):
        self.chain.append(Block(len(self.chain)+1,datetime.datetime.utcnow(), data, self.chain[len(self.chain)-1].hash))
    
    @property
    def lenChain(self):
        return len(self.chain)
    
    @property
    def lastBlock(self):
        return self.chain[-1]