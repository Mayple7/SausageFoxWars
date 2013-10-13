import Zero
import Events
import Property
import VectorMath
import Color
import math

class CreepLogic:
    def Initialize(self, initializer):
        #Initializes the creep's stats
        self.speedarray = [[0] * 60 for i in range(60)]
        self.hparray = [[0] * 60 for i in range(60)]
        self.bountyarray = [[0] * 60 for i in range(60)]
        self.setCreepArray()
            
    def setCreepArray(self):
        for i in range(60):
            self.hparray[i] = round(50 * math.exp(0.1622*i))
            self.bountyarray[i] = round(math.exp(0.1*i))
            if(i == 10 or i == 20 or i == 30 or i == 40 or i == 50 or i == 60):
                self.speedarray[i] = 0.1
            else:
                self.speedarray[i] = 0.05

Zero.RegisterComponent("CreepLogic", CreepLogic)