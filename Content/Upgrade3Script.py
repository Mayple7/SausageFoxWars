import Zero
import Events
import Property
import VectorMath

class Upgrade3Script:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        
    def OnMouseUp(self, MouseEvent):
        if(self.towerstats.towerlevel[2] < 3):
            self.towerstats.towerlevel[2] += 1

Zero.RegisterComponent("Upgrade3Script", Upgrade3Script)