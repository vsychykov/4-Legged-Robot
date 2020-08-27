from __future__ import print_function
import pyrosim
import matplotlib.pyplot as plt
import random 
import copy
from robot import ROBOT
import pickle 
from population import POPULATION
from individual import INDIVIDUAL
import constants as c
from environments import ENVIRONMENTS
from environment import ENVIRONMENT

envs = ENVIRONMENTS()




parents = POPULATION(c.popSize)
parents.Initialize()
parents.Evaluate(envs, pp=False, pb=True)
#
parents.Print()


for g in range(1,c.numGens):
    
    children = POPULATION(c.popSize)
    children.Fill_From(parents)
    children.Evaluate(envs, pp=False, pb=True)
    print(g),
    children.Print(),
    print(),
    parents.ReplaceWith(children)



if (g==c.numGens-1):
    print(parents.p[0].fitness)
    for e in range(0,c.numEnvs):
        parents.p[0].Start_Evaluation(envs.envs[e], pp = False, pb = False)
        parents.p[0].Compute_Fitness()





