import Zero
import Events
import Property
import VectorMath

class Upgrade3Script:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        self.Owner.SpriteText.Text = str(self.towerstats.upgradecost3[0]) + "g"
        
    def OnMouseUp(self, MouseEvent):
        self.player = self.Space.FindObjectByName("Player").PlayerLogic
        if(self.towerstats.towerlevel[2] < 3 and self.player.money >= self.towerstats.upgradecost3[self.towerstats.towerlevel[2]]):
            self.player.money -= self.towerstats.upgradecost3[self.towerstats.towerlevel[2]]
            self.towerstats.towerlevel[2] += 1
            if(self.towerstats.towerlevel[2] == 3):
                self.Owner.Destroy()
            else:
                self.Owner.SpriteText.Text = str(self.towerstats.upgradecost3[self.towerstats.towerlevel[2]]) + "g"

Zero.RegisterComponent("Upgrade3Script", Upgrade3Script)