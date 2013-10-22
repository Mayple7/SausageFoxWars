import Zero
import Events
import Property
import VectorMath

'''

#YOLOsweg

 0+ Empty spaces
 -1 Wall
 -2 Unnassigned

'''

Vec3 = VectorMath.Vec3

class GameLogic:
    InputType = Property.Bool(default = True)
    GamepadIndex = Property.Int(default = 0)
    def Initialize(self, initializer):
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
        self.debugMode = False
        
        self.SelectingCell = 0
        self.CellSelected = 0
        self.CellSelectedx = 5
        self.CellSelectedy = 5
        self.CellSelectedxStick = 5
        self.CellSelectedyStick = 5
        
        self.towerChoice = 1
        self.towerChoiceMax = 4
         
        self.hudspace = Zero.Game.FindSpaceByName("HUDLevel")
        self.select = self.hudspace.FindObjectByName("Selector")
        level = self.Space.FindObjectByName("LevelSettings")
        self.player = level.PlayerLogic
        
        self.red = self.hudspace.FindObjectByName("RedTower")
        self.blue = self.hudspace.FindObjectByName("BlueTower")
        self.green = self.hudspace.FindObjectByName("GreenTower")
        self.yellow = self.hudspace.FindObjectByName("YellowTower")
        
        self.Gamepad = Zero.Gamepads.GetGamePad(self.GamepadIndex)
        
        if(self.InputType == False and self.Gamepad):
            Zero.Connect(self.Gamepad, Events.ButtonDown, self.OnButtonDown)
            Zero.Connect(self.Gamepad, Events.ButtonUp, self.OnButtonUp)
        
        #Snatches the size and end from the MapCreate script
        self.xsize = self.Space.FindObjectByName("MapCreate").MapCreate.xsize
        self.ysize = self.Space.FindObjectByName("MapCreate").MapCreate.ysize
        self.endx = self.Space.FindObjectByName("MapCreate").MapCreate.endx
        self.endy = self.Space.FindObjectByName("MapCreate").MapCreate.endy
        
        #Sets up the array for cell
        self.node_array = [[[0]*self.ysize for i in range(self.ysize)][0]*self.xsize for i in range(self.xsize)]
        self.count = 0
        #Initializes the play field
        for i in range(self.xsize):
            for j in range(self.ysize):
                #Sets up the play field for the walls
                if(i == 0 or i == self.xsize-1 or j == 0 or j == self.ysize-1):
                    self.node_array[i][j] = Cell()
                    self.node_array[i][j].Initialize(1)
                    self.node_array[i][j].weight = -1
                    
                #Sets up the cell play field
                else:
                    self.node_array[i][j] = Cell()
                    self.node_array[i][j].Initialize(1)
                
        #Sets the end point weight to 0
        self.node_array[self.endx][self.endy].weight = 0
        
        #Refreshes all the weight
        self.refreshWeight()
        
    def OnLogicUpdate(self, UpdateEvent):
        if(not self.InputType):
            if (self.SelectingCell == 0):
                self.CellSelected = self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.HoverState()
                self.SelectingCell = 1
                
            direction = self.Gamepad.LeftStick
            
            self.CellSelectedxStick += direction.x * (UpdateEvent.Dt * 5)
            self.CellSelectedyStick -= direction.y * (UpdateEvent.Dt * 5)
            
            if (self.CellSelectedxStick < 1):
                    self.CellSelectedxStick = 1
                    
            if (self.CellSelectedxStick > self.xsize-2):
                    self.CellSelectedxStick = self.xsize-2
                    
            if (self.CellSelectedyStick < 1):
                    self.CellSelectedyStick = 1
            
            if (self.CellSelectedyStick > self.ysize-2):
                    self.CellSelectedyStick = self.ysize-2
            
            if (not(self.CellSelectedx == round(self.CellSelectedxStick)) or not(self.CellSelectedy == round(self.CellSelectedyStick))):
                if (self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
                    self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.DefaultState()
                
                self.CellSelectedx = round(self.CellSelectedxStick)
                self.CellSelectedy = round(self.CellSelectedyStick)
                if (self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
                    self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.HoverState()
                    
        # Key presses for testing
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Space)):
            self.printField()
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.R)):
            self.refreshWeight()
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.T)):
            self.Space.FindObjectByName("Player").PlayerLogic.level = 59
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Home)):
            self.debugMode = not self.debugMode
            
    def refreshWeight(self):
        #Resets the end point to 0 and starting loop variables
        self.count += 1
        self.node_array[self.endx][self.endy].weight = 0
        completeRefresh = False
        
        #Loops through the entire play field
        for i in range(1, self.xsize - 1):
            for j in range(1, self.ysize - 1):
                self.count += 1
                
                #Saves each side of the current cell to variables
                down = self.node_array[i][j+1]
                up = self.node_array[i][j-1]
                right = self.node_array[i+1][j]
                left = self.node_array[i-1][j]
                current = self.node_array[i][j]
                
                #Sets the base minimum to a very large number
                minimum = 1000000000
                
                #Finds the minimum weight between all the sides
                if(down.weight >= 0):
                    minimum = min(minimum, down.weight)
                if(up.weight >= 0):
                    minimum = min(minimum, up.weight)
                if(right.weight >= 0):
                    minimum = min(minimum, right.weight)
                if(left.weight >= 0):
                    minimum = min(minimum, left.weight)
                    
                #Different weight if the cell has a tower also sets a variable to re-loop if something changed
                if(current.tower):
                    if(minimum != 1000000000 and current.weight > minimum + 1001 or current.weight == -2):
                        current.weight = minimum + 1001
                        completeRefresh = True
                elif(minimum != 1000000000 and (current.weight > minimum + 1 or current.weight == -2)):
                    current.weight = minimum + 1
                    completeRefresh = True
        
        #Calls the function again if it needs to
        if(completeRefresh):
            self.refreshWeight()
        
    #Prints the entire grid
    def printField(self):
        for i in range(self.xsize):
            for j in range(self.ysize):
                print(self.node_array[i][j].weight)
            print("------------------------")
            
    def OnButtonDown(self, gamepadEvent):
        
        
        if(gamepadEvent.Button == Zero.Buttons.RightShoulder):
            self.towerChoice += 1
            if (self.towerChoice > self.towerChoiceMax):
                self.towerChoice = 1
            if (self.towerChoice == 1):
                self.select.Transform.Translation = Vec3(self.red.Transform.Translation.x, -6, 0)
            if (self.towerChoice == 2):
                self.select.Transform.Translation = Vec3(self.green.Transform.Translation.x, -6, 0)
            if (self.towerChoice == 3):
                self.select.Transform.Translation = Vec3(self.blue.Transform.Translation.x, -6, 0)
            if (self.towerChoice == 4):
                self.select.Transform.Translation = Vec3(self.yellow.Transform.Translation.x, -6, 0)
        if(gamepadEvent.Button == Zero.Buttons.LeftShoulder):
            self.towerChoice -= 1
            if (self.towerChoice < 1):
                self.towerChoice = self.towerChoiceMax
            if (self.towerChoice == 1):
                self.select.Transform.Translation = Vec3(self.red.Transform.Translation.x, -6, 0)
            if (self.towerChoice == 2):
                self.select.Transform.Translation = Vec3(self.green.Transform.Translation.x, -6, 0)
            if (self.towerChoice == 3):
                self.select.Transform.Translation = Vec3(self.blue.Transform.Translation.x, -6, 0)
            if (self.towerChoice == 4):
                self.select.Transform.Translation = Vec3(self.yellow.Transform.Translation.x, -6, 0)
            
        
        
        if(gamepadEvent.Button == Zero.Buttons.DpadLeft and self.CellSelectedx > 1):
            if (self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
                self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.DefaultState()
            self.CellSelectedx -= 1
            self.CellSelectedxStick = self.CellSelectedx
            self.CellSelectedyStick = self.CellSelectedy
            if (self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
                self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.HoverState()
        
        if(gamepadEvent.Button == Zero.Buttons.DpadRight and self.CellSelectedx < self.xsize-2):
            if (self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
                self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.DefaultState()
            self.CellSelectedx += 1
            self.CellSelectedxStick = self.CellSelectedx
            self.CellSelectedyStick = self.CellSelectedy
            if (self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
                self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.HoverState()
        
        if(gamepadEvent.Button == Zero.Buttons.DpadUp and self.CellSelectedy > 1):
            if (self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
                self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.DefaultState()
            self.CellSelectedy -= 1
            self.CellSelectedxStick = self.CellSelectedx
            self.CellSelectedyStick = self.CellSelectedy
            if (self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
                self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.HoverState()
            
        if(gamepadEvent.Button == Zero.Buttons.DpadDown and self.CellSelectedy < self.ysize-2):
            if (self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
                self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.DefaultState()
            self.CellSelectedy += 1
            self.CellSelectedxStick = self.CellSelectedx
            self.CellSelectedyStick = self.CellSelectedy
            if (self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
                self.node_array[self.CellSelectedx][self.CellSelectedy].cellName.CellLogic.HoverState()
            
        if(gamepadEvent.Button == Zero.Buttons.A and self.node_array[self.CellSelectedx][self.CellSelectedy].cellName):
            if(self.towerChoice == 1 and self.player.money >= 5 and not self.node_array[self.CellSelectedx][self.CellSelectedy].tower):
                tower = self.Space.CreateAtPosition("RedTower",Vec3(self.CellSelectedx,-self.CellSelectedy,1))
                tower.Transform.Translation += Vec3(0,0,1)
                tower.RedTowerLogic.xpos = round(tower.Transform.Translation.x)
                tower.RedTowerLogic.ypos = -round(tower.Transform.Translation.y)
                self.player.money -= 5
            elif(self.towerChoice == 2 and self.player.money >= 25 and not self.node_array[self.CellSelectedx][self.CellSelectedy].tower):
                tower = self.Space.CreateAtPosition("GreenTower",Vec3(self.CellSelectedx,-self.CellSelectedy,1))
                tower.Transform.Translation += Vec3(0,0,1)
                tower.GreenTowerLogic.xpos = round(tower.Transform.Translation.x)
                tower.GreenTowerLogic.ypos = -round(tower.Transform.Translation.y)
                self.player.money -= 25
            elif(self.towerChoice == 3 and self.player.money >= 10 and not self.node_array[self.CellSelectedx][self.CellSelectedy].tower):
                tower = self.Space.CreateAtPosition("BlueTower",Vec3(self.CellSelectedx,-self.CellSelectedy,1))
                tower.Transform.Translation += Vec3(0,0,1)
                tower.BlueTowerLogic.xpos = round(tower.Transform.Translation.x)
                tower.BlueTowerLogic.ypos = -round(tower.Transform.Translation.y)
                self.player.money -= 10
            elif(self.towerChoice == 4 and self.player.money >= 50 and not self.node_array[self.CellSelectedx][self.CellSelectedy].tower):
                tower = self.Space.CreateAtPosition("YellowTower",Vec3(self.CellSelectedx,-self.CellSelectedy,1))
                tower.Transform.Translation += Vec3(0,0,1)
                tower.YellowTowerLogic.xpos = round(tower.Transform.Translation.x)
                tower.YellowTowerLogic.ypos = -round(tower.Transform.Translation.y)
                self.player.money -= 50
            else:
                self.Gamepad.Vibrate(.15,1,1)
    def OnButtonUp(self, gamepadEvent):
        if(gamepadEvent.Button == Zero.Buttons.LeftShoulder):
            pass

#Houses all the cell information
class Cell:
    def Initialize(self, initializer):
        self.weight = -2
        self.tower = False
        self.mob = False
        self.name = 0
        self.cellName = 0

Zero.RegisterComponent("GameLogic", GameLogic)