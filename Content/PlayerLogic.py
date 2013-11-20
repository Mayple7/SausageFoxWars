import Zero
import Events
import Property
import VectorMath
import os

class PlayerLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        
        #Sets the player's starting stats
        self.lives = 30
        self.income = 30
        self.money = 90
        self.level = 1
        self.levelCount = 0
        self.time = 10
        self.race = self.towerstats.race
        
        self.numRed = [[0] * 4 for i in range(4)]
        self.numGreen = [[0] * 4 for i in range(4)]
        self.numBlue = [[0] * 4 for i in range(4)]
        self.numYellow = [[0] * 4 for i in range(4)]
        
        for i in range(4):
            self.numRed[i] = 0
        for i in range(4):
            self.numGreen[i] = 0
        for i in range(4):
            self.numBlue[i] = 0
        for i in range(4):
            self.numYellow[i] = 0
        
        #Sets the variables to edit the HUD
        self.hudspace = Zero.Game.FindSpaceByName("HUDLevel")
        self.moneyText = self.hudspace.FindObjectByName("Money")
        self.timerText = self.hudspace.FindObjectByName("Timer")
        self.livesText = self.hudspace.FindObjectByName("Lives")
        
        self.moneyText.SpriteText.Visible = True
        self.timerText.SpriteText.Visible = True
        self.livesText.SpriteText.Visible = True
        self.hudspace.FindObjectByName("Selector").Sprite.Visible = True
        self.hudspace.FindObjectByName("TowerUI").Sprite.Visible = True
        
        Upgrade1 = self.hudspace.CreateAtPosition("Upgrade1",VectorMath.Vec3(-3.977,-7.2,0))
        Upgrade1.Upgrade1Logic.LevelSpace = self.Space
        Upgrade2 = self.hudspace.CreateAtPosition("Upgrade2",VectorMath.Vec3(-1.345,-7.2,0))
        Upgrade2.Upgrade2Logic.LevelSpace = self.Space
        Upgrade3 = self.hudspace.CreateAtPosition("Upgrade3",VectorMath.Vec3(1.298,-7.2,0))
        Upgrade3.Upgrade3Logic.LevelSpace = self.Space
        Upgrade4 = self.hudspace.CreateAtPosition("Upgrade4",VectorMath.Vec3(3.962,-7.2,0))
        Upgrade4.Upgrade4Logic.LevelSpace = self.Space
    def onLogicUpdate(self, UpdateEvent):
        self.time -= UpdateEvent.Dt
        
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.PageDown)):
            self.money += 10000
        
        #Timer to give the player income and increase the level
        if(self.time <= 0):
            self.money += self.income
            self.time = 30
            self.levelCount += 1
            
        if(self.lives <= 0):
            self.file = open("wave_data.txt", 'a')
            self.file.write(str(self.level) + "," + str(self.money) + ",")
            for i in range(4):
                self.file.write(str(self.numRed[i]) + ",")
            for i in range(4):
                self.file.write(str(self.numGreen[i]) + ",")
            for i in range(4):
                self.file.write(str(self.numBlue[i]) + ",")
            for i in range(4):
                self.file.write(str(self.numYellow[i]) + ",")
            self.file.write("\n")
            self.file.close()
            Zero.Game.Quit()
            
        self.updateText()
        
    def updateText(self):
        #Updates all the text in the HUD
        self.moneyText.SpriteText.Text = str(self.money) + " G"
        self.timerText.SpriteText.Text = str(round(self.time))
        self.livesText.SpriteText.Text = "x " + str(self.lives)

Zero.RegisterComponent("PlayerLogic", PlayerLogic)