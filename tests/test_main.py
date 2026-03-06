import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import fifo, lru, optff

with open(os.path.join(os.path.dirname(__file__), '..', 'data', 'example.in')) as f:
    tokens = f.read().split()

k = int(tokens[0])
m = int(tokens[1])
pages = list(map(int, tokens[2:2 + m]))

print(f"FIFO: {fifo(pages, k)}")
print(f"LRU: {lru(pages, k)}")
print(f"OPTFF: {optff(pages, k)}")
