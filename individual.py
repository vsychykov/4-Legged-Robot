#from __future__ import print_function
import random
import pyrosim
import math
import numpy
import constants as c
from environment import ENVIRONMENT

from robot import ROBOT
class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.fitness = 0
        self.genome = numpy.random.random_sample((5,8)) * 2 - 1
        #self.genome = numpy.random.random(4) * 2 - 1
        #self.genome = numpy.random.random() * 2 - 1
        #print(self.genome)
                 
   
    def Start_Evaluation(self, env, pp, pb):
        self.sim = pyrosim.Simulator(window_size=(800,600), eval_time=c.evalTime, xyz = [2,-2,2], play_blind = pb, play_paused = pp, use_textures=True)
        self.robot = ROBOT ( self.sim , self.genome)
        env.Send_To( self.sim )
        self.sim.start()

            
    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        y = self.sim.get_sensor_data( sensor_id = self.robot.L4 , svi = 0 )
        self.fitness += y[-1]
        #self.Print()
        del self.sim

        
#    def Compute_Fitness(self):
#        self.sim.wait_to_finish()
#        y = self.sim.get_sensor_data( sensor_id = self.robot.P4 , svi = 1 )
#        self.fitness = y[-1]
#        del self.sim
        
    def Mutate(self):
#        geneToMutate = random.randint(0,3)
#        self.genome[geneToMutate] = random.gauss( self.genome[geneToMutate]  , math.fabs(self.genome[geneToMutate]) ) 
        row = random.randint(0, 4) 
        col = random.randint(0, 7)
        self.genome[row][col] = random.gauss( self.genome[row][col]  , math.fabs(self.genome[row][col]) )
        
        if self.genome[row][col] > 1:
            self.genome[row][col] = 1
        if self.genome[row][col] < -1:
            self.genome[row][col] = -1
            
        
    def Print(self):
        #print(self.fitness)
        print('['),
        print(self.ID),
        print(self.fitness),
        print('] '),
        #print("[",self.ID,self.fitness,"]")
        