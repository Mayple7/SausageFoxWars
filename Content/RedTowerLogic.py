import Zero
import Events
import Property
import VectorMath
import math
import Color

class RedTowerLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        
        #Initialize tower stats
        self.cost = 5
        self.damage = 1
        self.cooldown = 1
        self.range = 3
        self.bulletType = 0
        
        #Initializes the tower location
        self.xpos = 0
        self.ypos = 0
        self.targeted = False
        self.unitTargeted = 0
        
        #Variables for shooting
        self.shotTimer = 0
        self.shoot = 0
        
        #Timer variables
        self.searchTimer = 0
        self.searchTarget = 1
        self.searchSpeed = 0.5
        
    def onLogicUpdate(self, UpdateEvent):
        #Finds a target the shoots if it is off CD
        self.findTarget()
        self.shotTimer -= UpdateEvent.Dt
        if (self.shotTimer < 0):
            self.shoot = 1
            
        #Searches for a target every second
        self.searchTimer -= UpdateEvent.Dt
        if (self.searchTimer < 0):
            self.searchTarget = 1
        
    def findTarget(self):
        #Searches every second
        if(self.searchTarget):
            self.searchTarget = 0
            self.searchTimer = self.searchSpeed
            #Search if the tower doesn't have a target
            if(not self.targeted):
                allObjects = self.Space.AllObjects();
                #Loop through all objects to find a target
                for obj in allObjects:
                    if(obj.Name == "Unit"):
                        distance = math.sqrt(math.pow((obj.Transform.Translation.x - self.Owner.Transform.Translation.x),2) + math.pow((obj.Transform.Translation.y - self.Owner.Transform.Translation.y),2))
                        #Set the target if in range
                        if (distance < self.range):
                            self.unitTargeted = obj
                            self.targeted = True
                        continue
                        
        #Runs the code if there is a unit targeted
        if(self.unitTargeted):
            distance = math.sqrt(math.pow((self.unitTargeted.Transform.Translation.x - self.Owner.Transform.Translation.x),2) + math.pow((self.unitTargeted.Transform.Translation.y - self.Owner.Transform.Translation.y),2))
            #Untargets a unit if it is out of range
            if (distance > self.range):
                self.targeted = False
                self.unitTargeted.Sprite.Color = Color.Red
                self.unitTargeted = 0
            #Shoots the target 
            elif(self.shoot):
                self.shoot = 0
                self.shotTimer = self.cooldown
                shot = self.Space.CreateAtPosition("RedTowerBullet", VectorMath.Vec3(self.Owner.Transform.Translation.x, self.Owner.Transform.Translation.y, 3))
                shot.RedTowerBulletLogic.targetedUnit = self.unitTargeted
                shot.RedTowerBulletLogic.Damage = self.damage
                shot.RedTowerBulletLogic.BulletType = self.bulletType
        else:
            self.targeted = False
            
Zero.RegisterComponent("RedTowerLogic", RedTowerLogic)