import Zero
import Events
import Property
import VectorMath

class PlayerLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        
        #Sets the player's starting stats
        self.lives = 30
        self.income = 30
        self.money = 30
        self.level = 1
        self.levelCount = 0
        self.time = 10
        
        #Sets the variables to edit the HUD
        self.hudspace = Zero.Game.FindSpaceByName("HUDLevel")
        self.moneyText = self.hudspace.FindObjectByName("Money")
        self.incomeText = self.hudspace.FindObjectByName("Income")
        self.levelText = self.hudspace.FindObjectByName("Level")
        self.timerText = self.hudspace.FindObjectByName("Timer")
        self.livesText = self.hudspace.FindObjectByName("Lives")
        
        
    def onLogicUpdate(self, UpdateEvent):
        self.time -= UpdateEvent.Dt
        
        #Timer to give the player income and increase the level
        if(self.time <= 0):
            self.money += self.income
            self.time = 10
            self.levelCount += 1
            
        self.updateText()
        
    def updateText(self):
        #Updates all the text in the HUD
        self.moneyText.SpriteText.Text = "Money: " + str(self.money)
        self.incomeText.SpriteText.Text = "Income: " + str(self.income)
        self.levelText.SpriteText.Text = "Level: " + str(self.level)
        self.timerText.SpriteText.Text = "Next Income: " + str(round(self.time))
        self.livesText.SpriteText.Text = "Lives: " + str(self.lives)

Zero.RegisterComponent("PlayerLogic", PlayerLogic)