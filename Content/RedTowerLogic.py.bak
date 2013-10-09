import Zero
import Events
import Property
import VectorMath

class RedTowerLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        
        self.cost = 5
        self.damage = 1
        self.cooldown = 3
        self.range = 3
        
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

Zero.RegisterComponent("RedTowerLogic", RedTowerLogic)