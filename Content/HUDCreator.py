import Zero
import Events
import Property
import VectorMath

class HUDCreator:
    
    LevelforHUD = Property.Resource("Level")
    
    def Initialize(self, initializer):
        self.HUDSpace = Zero.Game.CreateNamedSpace("HUDLevel", "Space")
        
        self.HUDSpace.LoadLevel(self.LevelforHUD)
        
    def Destroyed(self):
        self.HUDSpace.Destroy()

Zero.RegisterComponent("HUDCreator", HUDCreator)