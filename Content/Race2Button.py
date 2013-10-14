import Zero
import Events
import Property
import VectorMath

class Race2Button:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        
    def OnMouseUp(self, MouseEvent):
        self.Space.Create("TowerStats")
        towerstats = self.Space.FindObjectByName("TowerStats")
        towerstats.TowerStats.setRace2()
        self.Space.CreateAtPosition("MapCreate", VectorMath.Vec3(-10, -2, -30))
        
Zero.RegisterComponent("Race2Button", Race2Button)