import Zero
import Events
import Property
import VectorMath

class YellowTowerLogic:
    def Initialize(self, initializer):
        self.cost = 50
        self.damage = 1
        self.cooldown = 3
        self.range = 10
        
        self.xpos = 0
        self.ypos = 0
        self.targeted = False
        
    def onLogicUpdate(self, UpdateEvent):
        self.findTarget()
        
    def findTarget(self):
        if(not self.targeted):
            for i in range(self.range):
                for j in range(self.range):
                    pass

Zero.RegisterComponent("YellowTowerLogic", YellowTowerLogic)