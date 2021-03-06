import Zero
import Events
import Property
import VectorMath

class Race3Button:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        
    def OnMouseUp(self, MouseEvent):
        self.Space.Create("TowerStats")
        towerstats = self.Space.FindObjectByName("TowerStats")
        towerstats.TowerStats.setRace3()
        self.Space.CreateAtPosition("MapCreate", VectorMath.Vec3(-10, -2, -30))

Zero.RegisterComponent("Race3Button", Race3Button)