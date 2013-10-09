import Zero
import Events
import Property
import VectorMath

class RedTowerBulletLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        Zero.Connect(self.Owner, Events.CollisionPersisted, self.OnCollision)
        self.Speed = 5
        self.targetedUnit = 0
        self.Damage = 0
        pass
    def onLogicUpdate(self, UpdateEvent):
        if (self.targetedUnit):
            self.Speed += UpdateEvent.Dt * 5
            direction = self.targetedUnit.Transform.Translation - self.Owner.Transform.Translation
            direction.normalize()
            self.Owner.Transform.Translation += VectorMath.Vec3(direction.x * (UpdateEvent.Dt * self.Speed), direction.y * (UpdateEvent.Dt * self.Speed), 0)
        else:
            self.Owner.Destroy()
    def OnCollision(self, CollisionEvent):
        otherObject = CollisionEvent.OtherObject
        if (otherObject == self.targetedUnit):
            otherObject.CreepLogic.health -= self.Damage
            self.Owner.Destroy()
Zero.RegisterComponent("RedTowerBulletLogic", RedTowerBulletLogic)