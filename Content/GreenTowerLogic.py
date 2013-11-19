import Zero
import Events
import Property
import VectorMath
import math
import Color

class GreenTowerLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.onLogicUpdate)
        
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        
        #Initialize tower stats
        self.cost = self.towerstats.cost2[self.towerstats.towerlevel[1]]
        self.damage = self.towerstats.damage2[self.towerstats.towerlevel[1]]
        self.cooldown = self.towerstats.cooldown2[self.towerstats.towerlevel[1]]
        self.range = self.towerstats.range2
        self.bulletType = self.towerstats.bullet2
        self.level = 0
        
        #Location Variables
        self.xpos = 0
        self.ypos = 0
        self.targeted = False
        self.unitTargeted = 0
        
        #Shooting variables
        self.shotTimer = 0
        self.shoot = 0
        
        #Searching variables
        self.searchTimer = 0
        self.searchTarget = 1
        self.searchSpeed = 0.5
        
    def onLogicUpdate(self, UpdateEvent):
        #Finds a target and shoots if it is off CD
        self.findTarget()
        self.shotTimer -= UpdateEvent.Dt
        if (self.shotTimer < 0):
            self.shoot = 1
        
        #Searches every second instead of every frame
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
                #Loop through all objects to find targets
                for obj in allObjects:
                    if("Unit" in obj.Name):
                        distance = math.sqrt(math.pow((obj.Transform.Translation.x - self.Owner.Transform.Translation.x),2) + math.pow((obj.Transform.Translation.y - self.Owner.Transform.Translation.y),2))
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
                shot.RedTowerBulletLogic.damage = self.damage
                shot.RedTowerBulletLogic.BulletType = self.bulletType
        else:
            self.targeted = False
            self.unitTargeted = 0
            self.unitTargeted = 0

Zero.RegisterComponent("GreenTowerLogic", GreenTowerLogic)