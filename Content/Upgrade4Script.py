import Zero
import Events
import Property
import VectorMath

class Upgrade4Script:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        self.Owner.SpriteText.Text = str(self.towerstats.upgradecost4[0]) + "g"
        
    def OnMouseUp(self, MouseEvent):
        self.player = self.Space.FindObjectByName("Player").PlayerLogic
        if(self.towerstats.towerlevel[3] < 3 and self.player.money >= self.towerstats.upgradecost4[self.towerstats.towerlevel[3]]):
            self.player.money -= self.towerstats.upgradecost4[self.towerstats.towerlevel[3]]
            self.towerstats.towerlevel[3] += 1
            if(self.towerstats.towerlevel[3] == 3):
                self.Owner.Destroy()
            else:
                self.Owner.SpriteText.Text = str(self.towerstats.upgradecost4[self.towerstats.towerlevel[3]]) + "g"

Zero.RegisterComponent("Upgrade4Script", Upgrade4Script)