import Zero
import Events
import Property
import VectorMath

class UpgradeBasic:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.onMouseUp)
        
        self.cost = 5
        self.damage = 1
        self.cooldown = 2
        self.range = 3
        self.bulletType = 0
        
        self.upgradecost = 100
        self.towerlevel = 1
        
    def onMouseUp(self, MouseEvent):
        if(self.GameLogic.PlayerLogic.money >= self.cost):
            if(self.towerlevel == 1):
                self.towerlevel = 2
                self.GameLogic.PlayerLogic.money -= self.cost
                #self.
                self.cost = 500

Zero.RegisterComponent("UpgradeBasic", UpgradeBasic)