import hashlib
import json
import datetime

class Block():
    def __init__(self, index, data, timestamp, prevhashS):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.prevhashS = prevhashS
        self.hashS = self.calcHash()
        

    def calcHash(self):
        hashing = hashlib.sha256()
        hashing.update(str(self.index).encode('utf-8')+str(self.timestamp).encode('utf-8') +str(self.data).encode('utf-8')+str(self.prevhashS).encode('utf-8'))
        return hashing.hexdigest()

def setGenesisBlock():
        return Block(0, 'Genesis', datetime.datetime.utcnow(), '0')

class Blockchain():
    def __init__(self, genesis):
        self.chain = [genesis]

    def addBlock(self, data):
        self.chain.append(Block(len(self.chain)+1,datetime.datetime.utcnow(), data, self.chain[len(self.chain)-1].hashS))
    
    def lenChain(self):
        return len(self.chain)
    
    def lastBlock(self):
        return self.chain[-1]