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
        self.incomeText = self.hudspace.FindObjectByName("Income")
        self.levelText = self.hudspace.FindObjectByName("Level")
        self.timerText = self.hudspace.FindObjectByName("Timer")
        self.livesText = self.hudspace.FindObjectByName("Lives")
        
        self.moneyText.SpriteText.Visible = True
        self.incomeText.SpriteText.Visible = True
        self.levelText.SpriteText.Visible = True
        self.timerText.SpriteText.Visible = True
        self.livesText.SpriteText.Visible = True
        self.hudspace.FindObjectByName("Selector").Sprite.Visible = True
        self.hudspace.FindObjectByName("TowerUI").Sprite.Visible = True
        self.hudspace.FindObjectByName("LevelTimer").SpriteText.Visible = True
        
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
        self.moneyText.SpriteText.Text = "Money: " + str(self.money)
        self.incomeText.SpriteText.Text = "Income: " + str(self.income)
        self.levelText.SpriteText.Text = "Level: " + str(self.level)
        self.timerText.SpriteText.Text = "Next Income: " + str(round(self.time))
        self.livesText.SpriteText.Text = "Lives: " + str(self.lives)

Zero.RegisterComponent("PlayerLogic", PlayerLogic)