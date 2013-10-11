import Zero
import Events
import Property
import VectorMath
import Color

class CreepLogic:
    def Initialize(self, initializer):
        #Initializes the creep's stats
        self.startSpeed = 0.5
        self.speed = self.startSpeed
        self.level = 0
        
        self.slowTime = 2
        self.slowTimer = self.slowTime
        self.slowed = False
        
        self.player = self.Space.FindObjectByName("Player")
        self.health = self.player.PlayerLogic.level * 10
        
        self.bounty = self.player.PlayerLogic.level
        
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
                self.Owner.UnitScript.MovingTimer / 2
        else:
            self.Owner.Sprite.Color = Color.Red
        
        self.Owner.SpriteText.Text = str(round(self.health))
        
        #Destroys creep if hp reaches 0
        if (self.health <= 0):
            self.player.PlayerLogic.money += self.bounty
            self.Owner.Destroy()
            

Zero.RegisterComponent("CreepLogic", CreepLogic)