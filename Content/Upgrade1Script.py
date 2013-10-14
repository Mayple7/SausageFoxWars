import Zero
import Events
import Property
import VectorMath

class Upgrade1Script:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        
    def OnMouseUp(self, MouseEvent):
        if(self.towerstats.towerlevel[0] < 4):
            self.towerstats.towerlevel[0] += 1

Zero.RegisterComponent("Upgrade1Script", Upgrade1Script)