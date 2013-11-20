import Zero
import Events
import Property
import VectorMath

class Race1Button:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        
    def OnMouseUp(self, MouseEvent):
        self.Space.Create("TowerStats")
        towerstats = self.Space.FindObjectByName("TowerStats")
        towerstats.TowerStats.setRace1()
        self.map = self.Space.CreateAtPosition("MapCreate", VectorMath.Vec3(-10, -2, -30)).MapCreate
        
Zero.RegisterComponent("Race1Button", Race1Button)