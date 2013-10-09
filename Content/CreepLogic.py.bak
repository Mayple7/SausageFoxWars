import Zero
import Events
import Property
import VectorMath

class CreepLogic:
    def Initialize(self, initializer):
        self.health = 10
        self.speed = 0.5
        self.level = 0
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        
    def onLogicUpdate(self, UpdateEvent):
        self.Owner.SpriteText.Text = str(self.level)
        
        

Zero.RegisterComponent("CreepLogic", CreepLogic)