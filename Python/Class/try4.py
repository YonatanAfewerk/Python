import cowsay 
import sys
from module import hello, goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
