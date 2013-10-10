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
        self.Damage = 1
    def onLogicUpdate(self, UpdateEvent):
        allObjects = self.Space.AllObjects();
        #Loops through all objects for splash effect
        for obj in allObjects:
            if(obj.Name == "Unit"):
                distance = math.sqrt(math.pow((obj.Transform.Translation.x - self.Owner.Transform.Translation.x),2) + math.pow((obj.Transform.Translation.y - self.Owner.Transform.Translation.y),2))

                #Deals damage to enemies in range based on how far they are
                if (distance < self.range):
                    effect = distance / self.range
                    obj.CreepLogic.health -= self.Damage - effect
                    
        self.Owner.Destroy();

Zero.RegisterComponent("BulletSplashLogic", BulletSplashLogic)