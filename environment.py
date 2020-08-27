#from __future__ import print_function
import constants as c
import pyrosim

class ENVIRONMENT:
    def __init__(self, ID):
        #print("Env ID number is:", ID)
        
        self.l = c.L
        self.w = c.L 
        self.h = c.L
      
        def Place_Light_Source_To_The_Front():
            self.x = 0
            self.y = 30*c.L
            self.z = 0
            
            
        def Place_Light_Source_To_The_Right():
            self.x = 30*c.L
            self.y = 0
            self.z = 0
            
        def Place_Light_Source_To_The_Left():
            self.x = -30*c.L
            self.y = 0
            self.z = 0
        
        def Place_Light_Source_To_The_Back():
            self.x = 0
            self.y = -30*c.L
            self.z = 0
            
            
        if (ID == 0):
            Place_Light_Source_To_The_Front()
        if (ID == 1):
            Place_Light_Source_To_The_Right()
        if (ID == 2):
            Place_Light_Source_To_The_Back()
        if (ID == 3):
            Place_Light_Source_To_The_Left()
        
        #print("xyz of the box", self.x,self.y,self.z)

        
        
    def Send_To(self, sim):
        self.lightSource = sim.send_box(x = self.x, y = self.y, z = self.z, height = self.h, width = self.w, length = self.l)
        sim.send_light_source( body_id = self.lightSource )