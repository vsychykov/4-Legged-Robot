#from __future__ import print_function
import constants as c
import pyrosim
from environment import ENVIRONMENT
    
class ENVIRONMENTS:
    
    def __init__(self):
    
        self.envs = {}
        
        for e in range( 0 , c.numEnvs):
            #self.ID = e
            self.envs[e] = ENVIRONMENT(e)
            