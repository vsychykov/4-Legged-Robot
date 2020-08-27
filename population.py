#from __future__ import print_function
import random
import numpy
import copy
import constants as c
from individual import INDIVIDUAL

class POPULATION:
    def __init__(self, popSize):
        self.popSize = popSize
        self.p = {}
        
#        for i in range(0,popSize):
#            self.p[i] = INDIVIDUAL(i)
            
    def Print(self):  
        for i in self.p:
            if ( i in self.p ):
                self.p[i].Print()
        #print()



    def Evaluate(self, envs, pp, pb):
        
        for i in self.p:
            self.p[i].fitness = 0
        
        for e in range(0, c.numEnvs):

            for i in self.p:
                self.p[i].Start_Evaluation(envs.envs[e],pp,pb)

            for i in self.p:
                self.p[i].Compute_Fitness()
                
        for i in self.p:
            self.p[i].fitness /= c.numEnvs
           




#    def Evaluate(self,pp,pb): # change here
#        
#        for i in self.p:
#            self.p[i].Start_Evaluation(pp,pb) #change here
#        
#        for i in self.p:
#            self.p[i].Compute_Fitness()
#            
           
            
    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()
            
    def ReplaceWith(self,other):
        for i in self.p:
            if ( self.p[i].fitness < other.p[i].fitness ):
                self.p[i] = other.p[i]
            
    def Initialize(self):
        for i in range(0,self.popSize):
            self.p[i] = INDIVIDUAL(i)
    
    def Fill_From(self , other):
        self.Copy_Best_From(other)
        #self.Print()
        self.Collect_Children_From(other)
        #self.Print()
        
    def Copy_Best_From(self, other):
        highestFit = other.p[0].fitness
        i=0
        for j in other.p:
            currentFit = other.p[j].fitness
            if(currentFit>highestFit):
                highestFit = currentFit
                i = j
        self.p[0] = copy.deepcopy(other.p[i])
        
    def Collect_Children_From(self,other):
        for j in other.p:
            if (j>0):
                #self.p[j] = other.p[j]
                winner=other.Winner_Of_Tournament_Selection()
                self.p[j] = copy.deepcopy(winner)
                self.p[j].Mutate()
        
    def Winner_Of_Tournament_Selection(other):

        p1= 0
        p2= 0

        while (p1==p2):
            p1= random.randint(0,other.popSize-1)
            p2= random.randint(0,other.popSize-1)

        if(other.p[p1].fitness>other.p[p2].fitness):
            return other.p[p1]
        else:
            return other.p[p2]

            
        