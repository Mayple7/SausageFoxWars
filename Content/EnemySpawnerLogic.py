import Zero
import Events
import Property
import VectorMath

Vec3 = VectorMath.Vec3

class EnemySpawnerLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        #Initializes the number of enemies and counters
        self.enemyCount = 0
        self.maxEnemies = 15
        
        #Initializes the timers
        self.spawnTimer = 0
        self.leveltimer = 0
        
        #Sets up HUD variables
        self.hudspace = Zero.Game.FindSpaceByName("HUDLevel")
        self.levelTimerText = self.hudspace.FindObjectByName("LevelTimer")
        self.levelset = self.Space.FindObjectByName("LevelSettings")
        
    def OnLogicUpdate(self, UpdateEvent):
        #Updates the timers and displays it on screen
        self.leveltimer += UpdateEvent.Dt
        self.spawnTimer += UpdateEvent.Dt
        self.levelTimerText.SpriteText.Text = "Next Level: " + str(round(30 - self.leveltimer))
        
        #Changes level after 30 seconds
        if(self.leveltimer > 30):
            self.leveltimer = 0
            self.levelset.PlayerLogic.level += 1
            self.enemyCount = 0
        
        #Spawns a set number of creeps
        if(self.enemyCount <= self.maxEnemies and self.spawnTimer >= 1):
            unit = self.Space.CreateAtPosition("Unit", self.Owner.Transform.Translation)
            unit.CreepLogic.level = self.levelset.PlayerLogic.level
            unit.Transform.Translation += Vec3(0,0,1)
            self.spawnTimer = 0
            self.enemyCount += 1
            
        

Zero.RegisterComponent("EnemySpawnerLogic", EnemySpawnerLogic)