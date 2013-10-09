import Zero
import Events
import Property
import VectorMath

class CreepLogic:
    def Initialize(self, initializer):
        #Initializes the creep's stats
        self.health = 10
        self.speed = 0.5
        self.level = 0
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        
    def onLogicUpdate(self, UpdateEvent):
        
        self.Owner.SpriteText.Text = str(self.level)
        
        #Destroys creep if hp reaches 0
        if (self.health <= 0):
            self.Owner.Destroy()
    
        

Zero.RegisterComponent("CreepLogic", CreepLogic)