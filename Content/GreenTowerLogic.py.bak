import Zero
import Events
import Property
import VectorMath

class GreenTowerLogic:
    def Initialize(self, initializer):
        self.cost = 25
        self.damage = 1
        self.cooldown = 3
        self.range = 5
        
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

Zero.RegisterComponent("GreenTowerLogic", GreenTowerLogic)