import Zero
import Events
import Property
import VectorMath
import Color

class CreepLogic:
    def Initialize(self, initializer):
        #Initializes the creep's stats
        self.health = 10
        self.startSpeed = 0.5
        self.speed = 0.5
        self.level = 0
        
        self.slowTime = 2
        self.slowTimer = self.slowTime
        self.slowed = False
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        
    def onLogicUpdate(self, UpdateEvent):
        #Update creep if he is slowed
        if (self.slowed):
            self.Owner.Sprite.Color = Color.Blue
            self.slowTimer -= UpdateEvent.Dt
            
            if (self.slowTimer < 0):
                self.slowed = False
                self.slowTimer = self.slowTime
                self.speed = self.startSpeed
        else:
            self.Owner.Sprite.Color = Color.Red
        
        self.Owner.SpriteText.Text = str(self.health)
        
        #Destroys creep if hp reaches 0
        if (self.health <= 0):
            self.Owner.Destroy()

Zero.RegisterComponent("CreepLogic", CreepLogic)