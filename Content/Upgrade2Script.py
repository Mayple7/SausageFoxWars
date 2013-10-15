import Zero
import Events
import Property
import VectorMath

class Upgrade2Script:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        self.Owner.SpriteText.Text = str(self.towerstats.upgradecost2[0]) + "g"
        
    def OnMouseUp(self, MouseEvent):
        self.player = self.Space.FindObjectByName("Player").PlayerLogic
        if(self.towerstats.towerlevel[1] < 3 and self.player.money >= self.towerstats.upgradecost2[self.towerstats.towerlevel[1]]):
            self.player.money -= self.towerstats.upgradecost2[self.towerstats.towerlevel[1]]
            self.towerstats.towerlevel[1] += 1
            if(self.towerstats.towerlevel[1] == 3):
                self.Owner.Destroy()
            else:
                self.Owner.SpriteText.Text = str(self.towerstats.upgradecost2[self.towerstats.towerlevel[1]]) + "g"

Zero.RegisterComponent("Upgrade2Script", Upgrade2Script)