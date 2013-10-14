import Zero
import Events
import Property
import VectorMath

class Upgrade2Script:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        
    def OnMouseUp(self, MouseEvent):
        if(self.towerstats.towerlevel[0] < 3):
            self.towerstats.towerlevel[0] += 1

Zero.RegisterComponent("Upgrade2Script", Upgrade2Script)