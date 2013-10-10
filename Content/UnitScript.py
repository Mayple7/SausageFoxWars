import Zero
import Events
import Property
import VectorMath

Vec3 = VectorMath.Vec3

class UnitScript:
    def Initialize(self, initializer):
        #Initializes the unit movement and timers
        self.currentx = 0
        self.currenty = 0
        self.MovementActive = 0
        self.MovementTimer = 0.1
        self.MovingActive = 0
        self.MovingTimer = self.MovementTimer/16
        self.move = Vec3(0,0,0)
        self.MoveSpeed = 0.5
        
        #Test stuff
        self.testx = 0
        self.testy = 0
        
        #Gets the HUD to reduce lives
        self.levelSettings = self.Space.FindObjectByName("LevelSettings")
        
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
    def resetWeight(self):
        #Resets all the weights and refreshes the grid
        GameLogic =self.Space.FindObjectByName("GameLogic")
        for i in range(1, GameLogic.GameLogic.xsize - 1):
            for j in range(1, GameLogic.GameLogic.ysize - 1):
                    GameLogic.GameLogic.node_array[i][j].weight = -2
                    
        GameLogic.GameLogic.node_array[GameLogic.GameLogic.endx][GameLogic.GameLogic.endy].weight = 0
        GameLogic.GameLogic.refreshWeight()
                        
    def OnLogicUpdate(self, UpdateEvent):
        self.MoveSpeed = self.Owner.CreepLogic.speed
        if(self.MovementTimer <= 0):
            self.MovementActive = 1
            self.MovementTimer = 0
            
        if (self.MovingTimer > 0 and self.MovingActive == 0):
            self.MovingTimer -= UpdateEvent.Dt
        if(self.MovingTimer <= 0):
            self.MovingActive = 1
            self.MovingTimer = 0
        
        GameLogic = self.Space.FindObjectByName("GameLogic")
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Space)):
            GameLogic.GameLogic.printField()
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.R)):
            GameLogic.GameLogic.refreshWeight()
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.T)):
            print(GameLogic.GameLogic.count)
            
        if(self.MovementActive == 1):
            self.currentx = round(self.Owner.Transform.Translation.x)
            self.currenty = round(-1*(self.Owner.Transform.Translation.y))
            down = GameLogic.GameLogic.node_array[self.currentx][self.currenty+1].weight
            left = GameLogic.GameLogic.node_array[self.currentx-1][self.currenty].weight
            up = GameLogic.GameLogic.node_array[self.currentx][self.currenty-1].weight
            right = GameLogic.GameLogic.node_array[self.currentx+1][self.currenty].weight
            
            #print(str(self.currenty) + " : " + str(self.currentx))
            #print("D: " + str(down) + "L: " + str(left) + "U: " + str(up) + "R: " + str(right))
            if (down == -1):
                down = 10000
            if (left == -1):
                left = 10000
            if (up == -1):
                up = 10000
            if (right == -1):
                right = 10000
                
            if(not(GameLogic.GameLogic.node_array[self.currentx][self.currenty].weight == 0)):
                
                if(down <= left and down <= up and down <= right):
                    if (GameLogic.GameLogic.node_array[self.currentx][self.currenty+1].name == 0):
                        self.currenty += 1
                    else:
                        #print(GameLogic.GameLogic.node_array[self.currenty+1][self.currentx].name)
                        GameLogic.GameLogic.node_array[self.currentx][self.currenty+1].name.Destroy()
                        GameLogic.GameLogic.node_array[self.currentx][self.currenty+1].tower = False
                        GameLogic.GameLogic.node_array[self.currentx][self.currenty+1].name = 0
                        self.testx = self.currentx
                        self.testy = self.currenty
                        self.resetWeight()
                    #print("down")
                elif(left <= down and left <= up and left <= right):
                    if (GameLogic.GameLogic.node_array[self.currentx-1][self.currenty].name == 0):
                        self.currentx -= 1
                    else:
                        #print(GameLogic.GameLogic.node_array[self.currenty][self.currentx-1].name)
                        GameLogic.GameLogic.node_array[self.currentx-1][self.currenty].name.Destroy()
                        GameLogic.GameLogic.node_array[self.currentx-1][self.currenty].tower = False
                        GameLogic.GameLogic.node_array[self.currentx-1][self.currenty].name = 0
                        self.testx = self.currentx
                        self.testy = self.currenty
                        self.resetWeight()
                    #print("left")
                elif(up <= down and up <= left and up <= right):
                    if (GameLogic.GameLogic.node_array[self.currentx][self.currenty-1].name == 0):
                        self.currenty -= 1
                    else:
                        #print(GameLogic.GameLogic.node_array[self.currenty-1][self.currentx].name)
                        GameLogic.GameLogic.node_array[self.currentx][self.currenty-1].name.Destroy()
                        GameLogic.GameLogic.node_array[self.currentx][self.currenty-1].tower = False
                        GameLogic.GameLogic.node_array[self.currentx][self.currenty-1].name = 0
                        self.testx = self.currentx
                        self.testy = self.currenty
                        self.resetWeight()
                    #print("up")
                elif(right <= down and right <= left and right <= up):
                    if (GameLogic.GameLogic.node_array[self.currentx+1][self.currenty].name == 0):
                        self.currentx += 1
                    else:
                        #print(GameLogic.GameLogic.node_array[self.currenty][self.currentx+1].name)
                        GameLogic.GameLogic.node_array[self.currentx+1][self.currenty].name.Destroy()
                        GameLogic.GameLogic.node_array[self.currentx+1][self.currenty].tower = False
                        GameLogic.GameLogic.node_array[self.currentx+1][self.currenty].name = 0
                        self.testx = self.currentx
                        self.testy = self.currenty
                        self.resetWeight()
                    #print("right")
                self.move = Vec3(self.currentx,self.currenty, 0) - Vec3(round((self.Owner.Transform.Translation.x)),round(-1*(self.Owner.Transform.Translation.y)),0)
            else:
                self.levelSettings.PlayerLogic.lives -= 1
                self.Owner.Destroy()
            self.MovementTimer = self.MoveSpeed
            self.MovementActive = 0
            
        if (self.MovingActive == 1):
            self.Owner.Transform.Translation += VectorMath.Vec3((self.move.x)/16, -(self.move.y)/16, 0)
            self.MovingTimer = (self.MoveSpeed)/16
            self.MovementTimer -= (self.MoveSpeed)/16
            self.MovingActive = 0
        #print(GameLogic.GameLogic.node_array[self.currenty-1][self.currentx].tower)
        #print(self.Owner.Transform.Translation)
    
Zero.RegisterComponent("UnitScript", UnitScript)