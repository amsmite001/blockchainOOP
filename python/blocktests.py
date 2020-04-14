import unittest
from block import Blockchain
from block import Block

class block_test(unittest.TestCase):
    def testDefaults(self):
        genesis = Blockchain.setGenesisBlock()
        self.assertEqual(genesis.index, 0)