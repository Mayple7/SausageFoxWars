import Zero
import Events
import Property
import VectorMath
import Color
import random

Vec3 = VectorMath.Vec3

class UnitScript:
    def Initialize(self, initializer):
        # Initializes the unit movement and timers
        self.currentx = 0
        self.currenty = 0
        self.direction = 0
        self.MovementActive = 1
        self.MovementTimer = 0.1
        self.MovingActive = 0
        self.MovingTimer = self.MovementTimer / 16
        self.move = Vec3(0,0,0)
        
        # Test stuff
        self.testx = 0
        self.testy = 0
        
        # Gets the HUD to reduce lives
        self.player = self.Space.FindObjectByName("Player")
        self.levelsettings = self.Space.FindObjectByName("LevelSettings")
        self.health = self.levelsettings.CreepLogic.hparray[self.player.PlayerLogic.level-1]
        self.speed = self.levelsettings.CreepLogic.speedarray[self.player.PlayerLogic.level-1]
        self.bounty = self.levelsettings.CreepLogic.bountyarray[self.player.PlayerLogic.level-1]
        
        # Tower effects
        self.slow = False
        self.stun = False
        self.stuntimer = 0
        self.slowtimer = 0
        
        # Random
        self.randomPrevelent = 0
        if (random.randint(0,1)):
            self.randomPrevelent = 1
        
        # On update
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)

    def resetWeight(self):
        #Resets all the weights and refreshes the grid
        GameLogic = self.Space.FindObjectByName("GameLogic")
        for i in range(1, GameLogic.GameLogic.xsize - 1):
            for j in range(1, GameLogic.GameLogic.ysize - 1):
                    GameLogic.GameLogic.node_array[i][j].weight = -2
        
        GameLogic.GameLogic.node_array[GameLogic.GameLogic.endx][GameLogic.GameLogic.endy].weight = 0
        GameLogic.GameLogic.refreshWeight()

    def TowerEffect(self, UpdateEvent):
        #Updates the creep if he is slowed or stunned
        if(self.stun):
            self.stuntimer += UpdateEvent.Dt
            self.speed = 0
            self.Owner.Sprite.Color = Color.Black
            
            if(self.stuntimer > 1):
                self.stun = False
                self.stuntimer = 0
                self.Owner.Sprite.Color = Color.Red
                self.speed = self.levelsettings.CreepLogic.speedarray[self.player.PlayerLogic.level-1]
        
        elif(self.slow):
            self.slowtimer += UpdateEvent.Dt
            self.speed = self.levelsettings.CreepLogic.speedarray[self.player.PlayerLogic.level-1] * 0.5
            self.Owner.Sprite.Color = Color.Blue
            
            if(self.slowtimer > 2):
                self.slow = False
                self.slowtimer = 0
                self.Owner.Sprite.Color = Color.Red
                self.speed = self.levelsettings.CreepLogic.speedarray[self.player.PlayerLogic.level-1]

    def OnLogicUpdate(self, UpdateEvent):
        # Game logic location
        GameLogic = self.Space.FindObjectByName("GameLogic")
        
        # Tower effects (Stun or Slow)
        self.TowerEffect(UpdateEvent)
        
        #Checks if the creep is dead
        if(self.health <= 0):
            self.player.PlayerLogic.money += self.bounty
            self.Owner.Destroy()
            
        self.Owner.SpriteText.Text = str(round(self.health))
        
        if (self.MovingTimer > 0 and self.MovingActive == 0):
            self.MovingTimer -= UpdateEvent.Dt
        if(self.MovingTimer <= 0):
            self.MovingActive = 1
            self.MovingTimer = 0
        if(Vec3(round(self.Owner.Transform.Translation.x,1), round(self.Owner.Transform.Translation.y*-1,1), 0) == Vec3(self.currentx, self.currenty, 0)):
            self.MovementActive = 1
        
        if(self.MovementActive == 1):
            
            self.currentx = round(self.Owner.Transform.Translation.x)
            self.currenty = round(-1 * (self.Owner.Transform.Translation.y))
            #print(Vec3(self.Owner.Transform.Translation.x, self.Owner.Transform.Translation.y*-1, 0))
            down  = GameLogic.GameLogic.node_array[self.currentx][self.currenty+1].weight
            left  = GameLogic.GameLogic.node_array[self.currentx-1][self.currenty].weight
            up    = GameLogic.GameLogic.node_array[self.currentx][self.currenty-1].weight
            right = GameLogic.GameLogic.node_array[self.currentx+1][self.currenty].weight
            
            #print(str(self.currenty) + " : " + str(self.currentx))
            #print("D: " + str(down) + "L: " + str(left) + "U: " + str(up) + "R: " + str(right))
            if (down == -1):
                down = 1000000
            if (left == -1):
                left = 1000000
            if (up == -1):
                up = 1000000
            if (right == -1):
                right = 1000000
            
            changex = 0
            changey = 0
            
            if (not(GameLogic.GameLogic.node_array[self.currentx][self.currenty].weight == 0)):
                # DOWN:
                if (down <= left and (down < up or (self.randomPrevelent and down == up)) and down <= right):
                    if (GameLogic.GameLogic.node_array[self.currentx][self.currenty + 1].name == 0):
                        self.currenty += 1
                        self.direction = 0
                    else:
                        changey -= 1
                        self.resetWeight()
                # LEFT:
                elif (left <= down and left <= up and left <= right):
                    if (GameLogic.GameLogic.node_array[self.currentx - 1][self.currenty].name == 0):
                        self.currentx -= 1
                        self.direction = 1
                    else:
                        changex -= 1
                        self.resetWeight()
                # UP:
                elif (up <= down and up <= left and up <= right):
                    if (GameLogic.GameLogic.node_array[self.currentx][self.currenty - 1].name == 0):
                        self.currenty -= 1
                        self.direction = 2
                    else:
                        changey -= 1
                        self.resetWeight()
                # RIGHT:
                elif (right <= down and right <= left and right <= up):
                    if (GameLogic.GameLogic.node_array[self.currentx + 1][self.currenty].name == 0):
                        self.currentx += 1
                        self.direction = 3
                    else:
                        changex += 1
                        self.resetWeight()
                
                # Check if a tower is in the space
                if (GameLogic.GameLogic.node_array[self.currentx + changex][self.currenty + changey].name != 0):
                    # Destroy the tower
                    GameLogic.GameLogic.node_array[self.currentx + changex][self.currenty + changey].name.Destroy()
                    GameLogic.GameLogic.node_array[self.currentx + changex][self.currenty + changey].tower = False
                    GameLogic.GameLogic.node_array[self.currentx + changex][self.currenty + changey].name = 0
                
                self.Owner.Sprite.CurrentFrame = self.direction
                self.move = Vec3(self.currentx, self.currenty, 0) - Vec3(round((self.Owner.Transform.Translation.x)),round(-1*(self.Owner.Transform.Translation.y)),0)
                
            else:
                # Reached the end
                self.player.PlayerLogic.lives -= 1
                self.Owner.Destroy()
            
            self.MovementActive = 0
            self.MovingActive = 1
            self.MovingTimer = (self.speed) / 16
            #print(Vec3(self.currentx, self.currenty, 0))
            
        if (self.MovingActive == 1):
            self.Owner.Transform.Translation += VectorMath.Vec3((self.move.x * self.speed), -(self.move.y * self.speed), 0)
            self.MovingTimer = (self.speed) / 16
            self.MovingActive = 0
            
Zero.RegisterComponent("UnitScript", UnitScript)