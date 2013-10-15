import Zero
import Events
import Property
import VectorMath

class Upgrade4Script:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        
    def OnMouseUp(self, MouseEvent):
        if(self.towerstats.towerlevel[3] < 3):
            self.towerstats.towerlevel[3] += 1

Zero.RegisterComponent("Upgrade4Script", Upgrade4Script)