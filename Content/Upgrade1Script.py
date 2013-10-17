import Zero
import Events
import Property
import VectorMath

class Upgrade1Script:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        self.Owner.SpriteText.Text = str(self.towerstats.upgradecost1[0]) + "g"
        
    def OnMouseUp(self, MouseEvent):
        self.player = self.Space.FindObjectByName("Player").PlayerLogic
        if(self.towerstats.towerlevel[0] < 3 and self.player.money >= self.towerstats.upgradecost1[self.towerstats.towerlevel[0]]):
            self.player.money -= self.towerstats.upgradecost1[self.towerstats.towerlevel[0]]
            self.towerstats.towerlevel[0] += 1
            if(self.towerstats.towerlevel[0] == 3):
                self.Owner.Destroy()
            else:
                self.Owner.SpriteText.Text = str(self.towerstats.upgradecost1[self.towerstats.towerlevel[0]]) + "g"

Zero.RegisterComponent("Upgrade1Script", Upgrade1Script)