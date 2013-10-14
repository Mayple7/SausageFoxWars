import Zero
import Events
import Property
import VectorMath

class TowerStats:
    def Initialize(self, initializer):
        self.race = 1
        self.towerlevel = [[0] * 4 for i in range(4)]
        
        self.cost1 = [[1] * 4 for i in range(4)]
        self.cost2 = [[1] * 4 for i in range(4)]
        self.cost3 = [[1] * 4 for i in range(4)]
        self.cost4 = [[1] * 4 for i in range(4)]
        
        self.damage1 = [[1] * 4 for i in range(4)]
        self.damage2 = [[1] * 4 for i in range(4)]
        self.damage3 = [[1] * 4 for i in range(4)]
        self.damage4 = [[1] * 4 for i in range(4)]
        
        self.cooldown1 = [[1] * 4 for i in range(4)]
        self.cooldown2 = [[1] * 4 for i in range(4)]
        self.cooldown3 = [[1] * 4 for i in range(4)]
        self.cooldown4 = [[1] * 4 for i in range(4)]
        
        self.range1 = 3
        self.range2 = 3
        self.range3 = 2
        self.range4 = 8
        
        self.bullet1 = 0
        self.bullet2 = 1
        self.bullet3 = 3
        self.bullet4 = 0
        
    def setRace1(self):
        self.race = 1
        
        #Initialize the tower levels to 0
        for i in range(4):
            self.towerlevel[i] = 0
        
        #Race 1 level 1 tower costs
        self.cost1[0] = 10
        self.cost2[0] = 15
        self.cost3[0] = 25
        self.cost4[0] = 40
        
        #Race 1 level 1 tower damage
        self.damage1[0] = 500
        self.damage2[0] = 10
        self.damage3[0] = 1
        self.damage4[0] = 20
        
        #Race 1 level 1 tower cooldowns
        self.cooldown1[0] = 1.5
        self.cooldown2[0] = 1.75
        self.cooldown3[0] = 2
        self.cooldown4[0] = 4
        
        #Race 1 level 1 tower range
        self.range1 = 5
        self.range2 = 4
        self.range3 = 3
        self.range4 = 8
        
        #Race 1 bullet types
        self.bullet1 = 0
        self.bullet2 = 1
        self.bullet3 = 3
        self.bullet4 = 0
        
    def setRace2(self):
        self.race = 2
        
        #Initialize the tower levels to 0
        for i in range(4):
            self.towerlevel[i] = 0
        
        #Race 1 level 1 tower costs
        self.cost1[0] = 10
        self.cost2[0] = 15
        self.cost3[0] = 25
        self.cost4[0] = 40
        
        #Race 1 level 1 tower damage
        self.damage1[0] = 5
        self.damage2[0] = 101
        self.damage3[0] = 1
        self.damage4[0] = 20
        
        #Race 1 level 1 tower cooldowns
        self.cooldown1[0] = 1.5
        self.cooldown2[0] = 1.75
        self.cooldown3[0] = 2
        self.cooldown4[0] = 4
        
        #Race 1 level 1 tower range
        self.range1 = 5
        self.range2 = 4
        self.range3 = 3
        self.range4 = 8
        
        #Race 1 bullet types
        self.bullet1 = 0
        self.bullet2 = 1
        self.bullet3 = 3
        self.bullet4 = 0
        
    def setRace3(self):
        self.race = 3
        
        #Initialize the tower levels to 0
        for i in range(4):
            self.towerlevel[i] = 0
        
        #Race 1 level 1 tower costs
        self.cost1[0] = 10
        self.cost2[0] = 15
        self.cost3[0] = 25
        self.cost4[0] = 40
        
        #Race 1 level 1 tower damage
        self.damage1[0] = 5
        self.damage2[0] = 1
        self.damage3[0] = 100
        self.damage4[0] = 20
        
        #Race 1 level 1 tower cooldowns
        self.cooldown1[0] = 1.5
        self.cooldown2[0] = 1.75
        self.cooldown3[0] = 2
        self.cooldown4[0] = 4
        
        #Race 1 level 1 tower range
        self.range1 = 5
        self.range2 = 4
        self.range3 = 3
        self.range4 = 8
        
        #Race 1 bullet types
        self.bullet1 = 0
        self.bullet2 = 1
        self.bullet3 = 3
        self.bullet4 = 0

Zero.RegisterComponent("TowerStats", TowerStats)