# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:46:23 2020

@author: Ruifan
"""

import hashlib 
import datetime as dt
from flask import Flask
import random

class Block():
    def __init__(self, id, timestamp, data, prev_hash):
        self.id = id
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.own_hash = self.hash_block()
        self.proof = None #Proof will eventually be filled in
        
    def hash_block(self):
        hasher = hashlib.sha256()
        block_str = (str(self.id) + str(self.timestamp) + str(self.data) + 
                     str(self.prev_hash)).encode('utf-8')
        hasher.update(block_str)
        return hasher.hexdigest()
        
class Blockchain():
    def __init__(self):
        # Initiation creates empty chain and adds genesis block
        self.blocks = []
        self.blocks.append(self.create_genesis_block())
        
    def create_genesis_block(self):
        genesis = Block(0, dt.datetime.now(), {'genesis block':0}, 0)
        # Set a random proof of work
        random_proof = random.randint(0, 100000)
        genesis.proof = random_proof
        return genesis
        
    def add_new_block(self, data):
        # new_block is Block object 
        prev_block = self.blocks[-1]
        prev_hash = prev_block.own_hash
        prev_id = prev_block.id
        prev_proof = prev_block.proof
        new_id = prev_id + 1
        
        new_block = Block(new_id, dt.datetime.now(), data, prev_hash)
        
        # Calculate new proof of work and update the value before adding the new block to the chain
        new_proof = self.proof_of_work(prev_proof)
        new_block.proof = new_proof
        self.blocks.append(new_block)
        
    def print_blockchain(self):
        all_blocks = [(i.id, i.timestamp, i.data, i.prev_hash, i.own_hash) for i in self.blocks]
        print(all_blocks)
        
    def proof_of_work(self, prev_proof):
        # Find a number q, where p is he previous proof, where hash of pq begins with 0000
        proof = 0
        valid = False
        
        while valid == False:
            guess = f'{prev_proof}{proof}'.encode('utf-8')
            guess_hash = hashlib.sha256(guess).hexdigest()
            #print(guess_hash[:4])
            if guess_hash[:4] == "0000":
                valid = True
            else:
                proof += 1
        return proof
            
        
    
x = Block(123, dt.datetime(2020, 1, 29, 23, 15, 15), {'sender':'x123', 'recipient':'qwe12', 'amt':420}, 145)
#print(x.hash_block())

xx = Blockchain()
#print (xx.blocks)
xx.add_new_block({'sender':'pq444', 'recipient':'qwe12', 'amt':40})

xx.print_blockchain()








































































