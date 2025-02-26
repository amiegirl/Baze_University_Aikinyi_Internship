from django.shortcuts import render
from django.http import JsonResponse
from .my_blockchain import Blockchain
blockchain = Blockchain()
def mine_block(request):
  proof = 12345 # Dummy proof of work (in reality, a real proof-of-work function is needed)
  block = blockchain.create_block(proof)
  response = {'message': 'Block Mined!', 'block': block}
  return JsonResponse(response)

def get_chain(request):
   response = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
   return JsonResponse(response)