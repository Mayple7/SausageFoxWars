import Zero
import Events
import Property
import VectorMath
import math

class BulletSplashLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        self.range = 3
        self.Damage = 0
    def onLogicUpdate(self, UpdateEvent):
        allObjects = self.Space.AllObjects();
        for obj in allObjects:
            if(obj.Name == "Unit"):
                distance = math.sqrt(math.pow((obj.Transform.Translation.x - self.Owner.Transform.Translation.x),2) + math.pow((obj.Transform.Translation.y - self.Owner.Transform.Translation.y),2))
                if (distance < self.range):
                    obj.CreepLogic.health -= self.Damage
                    print(obj.CreepLogic.health)
                    pass
        self.Owner.Destroy();
        pass

Zero.RegisterComponent("BulletSplashLogic", BulletSplashLogic)