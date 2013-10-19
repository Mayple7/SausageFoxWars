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
        self.maxEnemies = 30
        
        #Initializes the timers
        self.spawnTimer = 0
        self.leveltimer = 0
        self.starttimer = 0
        self.gamestart = False
        
        #Sets up HUD variables
        self.hudspace = Zero.Game.FindSpaceByName("HUDLevel")
        self.levelTimerText = self.hudspace.FindObjectByName("LevelTimer")
        self.player = self.Space.FindObjectByName("Player")
        
    def OnLogicUpdate(self, UpdateEvent):
        if(self.starttimer < 10):
            self.starttimer += UpdateEvent.Dt
            self.leveltimer += UpdateEvent.Dt
            self.levelTimerText.SpriteText.Text = "Next Level: " + str(round(10 - self.leveltimer))
        else:
            if(self.gamestart == False):
                self.leveltimer = 0
                self.gamestart = True
            if(self.player.PlayerLogic.level > 60):
                self.Space.ReloadLevel()
            #Updates the timers and displays it on screen
            self.leveltimer += UpdateEvent.Dt
            self.spawnTimer += UpdateEvent.Dt
            self.levelTimerText.SpriteText.Text = "Next Level: " + str(round(30 - self.leveltimer))
            
            #Changes level after 30 seconds
            if(self.leveltimer > 30):
                self.leveltimer = 0
                self.player.PlayerLogic.level += 1
                self.enemyCount = 0
                    
            #Spawns a set number of creeps
            if(self.enemyCount < self.maxEnemies and self.spawnTimer >= 0.5 and self.player.PlayerLogic.level <= 60):
                unit = self.Space.CreateAtPosition("Unit", self.Owner.Transform.Translation)
                unit.Transform.Translation += Vec3(0,0,1)
                self.spawnTimer = 0
                self.enemyCount += 1
                
        

Zero.RegisterComponent("EnemySpawnerLogic", EnemySpawnerLogic)