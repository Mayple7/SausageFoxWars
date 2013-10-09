import Zero
import Events
import Property
import VectorMath
import math
import Color

class RedTowerLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        
        self.cost = 5
        self.damage = 1
        self.cooldown = 1
        self.range = 3
        self.bulletType = 0
        
        self.xpos = 0
        self.ypos = 0
        self.targeted = False
        self.unitTargeted = 0
        
        self.shotTimer = 0
        self.shoot = 0
        
        self.searchTimer = 0
        self.searchTarget = 1
        self.searchSpeed = 0.5
        
    def onLogicUpdate(self, UpdateEvent):
        self.findTarget()
        self.shotTimer -= UpdateEvent.Dt
        if (self.shotTimer < 0):
            self.shoot = 1
            
        self.searchTimer -= UpdateEvent.Dt
        if (self.searchTimer < 0):
            self.searchTarget = 1
        
    def findTarget(self):
        if(self.searchTarget):
            self.searchTarget = 0
            self.searchTimer = self.searchSpeed
            if(not self.targeted):
                allObjects = self.Space.AllObjects();
                for obj in allObjects:
                    if(obj.Name == "Unit"):
                        if(not self.targeted):
                            distance = math.sqrt(math.pow((obj.Transform.Translation.x - self.Owner.Transform.Translation.x),2) + math.pow((obj.Transform.Translation.y - self.Owner.Transform.Translation.y),2))
                            if (distance < self.range):
                                self.unitTargeted = obj
                                self.targeted = True
                                obj.Sprite.Color = Color.Brown
                                
        if(self.unitTargeted):
            distance = math.sqrt(math.pow((self.unitTargeted.Transform.Translation.x - self.Owner.Transform.Translation.x),2) + math.pow((self.unitTargeted.Transform.Translation.y - self.Owner.Transform.Translation.y),2))
            if (distance > self.range):
                self.targeted = False
                self.unitTargeted.Sprite.Color = Color.Red
                self.unitTargeted = 0
            if (self.shoot):
                self.shoot = 0
                self.shotTimer = self.cooldown
                shot = self.Space.CreateAtPosition("RedTowerBullet", VectorMath.Vec3(self.Owner.Transform.Translation.x, self.Owner.Transform.Translation.y, 3))
                shot.RedTowerBulletLogic.targetedUnit = self.unitTargeted
                shot.RedTowerBulletLogic.Damage = self.damage
                shot.RedTowerBulletLogic.BulletType = self.bulletType
        if(not self.unitTargeted):
            self.targeted = False
            self.unitTargeted = 0
Zero.RegisterComponent("RedTowerLogic", RedTowerLogic)