import Zero
import Events
import Property
import VectorMath
import math

class BulletSplashLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        #Initialize the tower splash range and damage
        self.range = 3
        self.damage = 1
    def onLogicUpdate(self, UpdateEvent):
        allObjects = self.Space.AllObjects();
        #Loops through all objects for splash effect
        for obj in allObjects:
            if("Unit" in obj.Name):
                distance = math.sqrt(math.pow((obj.Transform.Translation.x - self.Owner.Transform.Translation.x),2) + math.pow((obj.Transform.Translation.y - self.Owner.Transform.Translation.y),2))

                #Deals damage to enemies in range based on how far they are
                if (distance < self.range):
                    effect = distance / self.range
                    obj.UnitScript.health -= self.damage - effect
                    
        self.Owner.Destroy();

Zero.RegisterComponent("BulletSplashLogic", BulletSplashLogic)