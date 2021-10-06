"""
Run script for DELTA
"""

#Import libraries
from speech import Speech

#Defs/classes
class Delta:
    
    def __init__(self):
        self.run()
    
    def run(self):
        print('Running DELTA')
        Speech().run()

if __name__ == '__main__':
    Delta()