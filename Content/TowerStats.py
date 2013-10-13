import Zero
import Events
import Property
import VectorMath

class TowerStats:
    def Initialize(self, initializer):
        self.race = 1
        
        self.cost1 = 10
        self.cost2 = 15
        self.cost3 = 25
        self.cost4 = 40
        
        self.damage1 = 3
        self.damage2 = 2
        self.damage3 = 1
        self.damage4 = 20
        
        self.cooldown1 = 2
        self.cooldown2 = 1.75
        self.cooldown3 = 2.5
        self.cooldown4 = 4
        
        self.range1 = 3
        self.range2 = 3
        self.range3 = 2
        self.range4 = 8
        
    def setRace1(self):
        self.race = 1
        
        self.cost1 = 10
        self.cost2 = 15
        self.cost3 = 25
        self.cost4 = 40
        
        self.damage1 = 500
        self.damage2 = 2
        self.damage3 = 1
        self.damage4 = 20
        
        self.cooldown1 = 2
        self.cooldown2 = 1.75
        self.cooldown3 = 2.5
        self.cooldown4 = 4
        
        self.range1 = 5
        self.range2 = 4
        self.range3 = 3
        self.range4 = 8

Zero.RegisterComponent("TowerStats", TowerStats)