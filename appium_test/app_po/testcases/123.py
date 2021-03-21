import sys
import os
print(os.getcwd())
print(os.path.abspath('../..'))
sys.path.append(os.path.abspath('../..'))