import unittest
import block
import datetime
from block import Blockchain
from block import Block

class block_test(unittest.TestCase):
    def testDefaults(self):
        genesis = block.setGenesisBlock()
        self.assertEqual(genesis.index, 0)
        self.assertNotEqual(genesis.hashS, None)
        self.assertEqual(genesis.data, 'Genesis')
        self.assertNotEqual(genesis.timestamp,None)
        self.assertEqual(genesis.prevhashS,'0')
        
    def testBlock(self):
        newblock = Block(0,"Hi",datetime.datetime.utcnow(), "No")
        self.assertEqual(newblock.index,0)
        self.assertEqual(newblock.prevhashS,"No")
        self.assertNotEqual(newblock.timestamp,None)
        self.assertNotEqual(newblock.hashS,None)
        
    def testChain(self):
        genesis = block.setGenesisBlock()
        testchain = Blockchain(genesis)
        testchain.addBlock("Where is this block at?!")
        self.assertEqual(testchain.lenChain(),2) #Gen + the one above
        self.assertNotEqual(testchain.lastBlock(),genesis)
