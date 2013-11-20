import Zero
import Events
import Property
import VectorMath

Vec4 = VectorMath.Vec4
Vec3 = VectorMath.Vec3

class CellLogic:
    InputType = Property.Bool(True)
    GamepadIndex = Property.Int(default = 0)
    def Initialize(self, initializer):
        self.Selected = False
        self.nameSet = 0
        self.currentx = round(self.Owner.Transform.Translation.x)
        self.currenty = round(-1*(self.Owner.Transform.Translation.y))
        self.GameLogic = self.Space.FindObjectByName("GameLogic") 
        self.Gamepad = Zero.Gamepads.GetGamePad(self.GamepadIndex)
        #Set up the mouse event functions
        if(self.InputType == True):
            Zero.Connect(self.Owner, Events.MouseEnter, self.OnMouseEnter)
            Zero.Connect(self.Owner, Events.MouseExit, self.OnMouseExit)
            Zero.Connect(self.Owner, Events.MouseDown, self.OnMouseDown)
            Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        elif(self.InputType == False and self.Gamepad):
            Zero.Connect(self.Gamepad, Events.ButtonDown, self.OnButtonDown)
            Zero.Connect(self.Gamepad, Events.ButtonUp, self.OnButtonUp)
            
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
        #Initializes the cell color highlights
        self.DefaultColor = Vec4(1,1,1,1)
        self.HoverColor = Vec4(1,1,1,.25)
        self.DownColor = Vec4(.5,.5,.5,.5)
        self.towerChoice = 1
        self.towerChoiceMax = 4
        
        #Initializes the hud and other level settings
        self.hudspace = Zero.Game.FindSpaceByName("HUDLevel")
        self.select = self.hudspace.FindObjectByName("Selector")
        level = self.Space.FindObjectByName("Player")
        self.player = level.PlayerLogic
        self.towerstats = self.Space.FindObjectByName("TowerStats").TowerStats
        
        #Creates variables for the various hud objects
        
        self.red = self.hudspace.FindObjectByName("RedTower")
        self.blue = self.hudspace.FindObjectByName("BlueTower")
        self.green = self.hudspace.FindObjectByName("GreenTower")
        self.yellow = self.hudspace.FindObjectByName("YellowTower")
        
        self.hoverZ = self.Owner.Transform.Translation.z
        
        self.sprite = self.Owner.Sprite.SpriteSource
        self.debugMode = self.GameLogic.GameLogic.debugMode
        self.DefaultState()
        
    
    def OnLogicUpdate(self, UpdateEvent):
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.Home)):
            self.debugMode = self.GameLogic.GameLogic.debugMode
        if(self.debugMode and self.Owner.Sprite.SpriteSource == self.sprite):
            self.Owner.Sprite.SpriteSource = "Square"
            self.Owner.SpriteText.Visible = True
        elif(not(self.debugMode) and not(self.Owner.Sprite.SpriteSource == self.sprite)):
            self.Owner.Sprite.SpriteSource = self.sprite
            self.Owner.SpriteText.Visible = False
        if (self.nameSet == 0):
            self.nameSet = 1
            self.GameLogic.GameLogic.node_array[self.currentx][self.currenty].cellName = self.Owner
        
        
        self.Owner.SpriteText.Text = str(self.GameLogic.GameLogic.node_array[round(self.Owner.Transform.Translation.x)][-round(self.Owner.Transform.Translation.y)].weight)
        
        #Changes the tower being placed based on input
        if (self.InputType):
            if(Zero.Keyboard.KeyIsPressed(Zero.Keys.One)):
                self.towerChoice = 1
                self.select.Transform.Translation = Vec3(-4, -9.035, 3)
            elif(Zero.Keyboard.KeyIsPressed(Zero.Keys.Three)):
                self.towerChoice = 2
                self.select.Transform.Translation = Vec3(0, -9.035, 3)
            elif(Zero.Keyboard.KeyIsPressed(Zero.Keys.Two)):
                self.towerChoice = 3
                self.select.Transform.Translation = Vec3(-2, -9.035, 3)
            elif(Zero.Keyboard.KeyIsPressed(Zero.Keys.Four)):
                self.towerChoice = 4
                self.select.Transform.Translation = Vec3(2, -9.035, 3)
                
            elif(Zero.Keyboard.KeyIsPressed(Zero.Keys.Five)):
                self.towerChoice = 5
                self.select.Transform.Translation = Vec3(3.942, -9.035, 3)
                    
    def OnButtonDown(self, gamepadEvent):
        pass
    def OnButtonUp(self, gamepadEvent):
        pass
            
    def DefaultState(self):
        self.Owner.Sprite.Color = self.DefaultColor
        self.Owner.Transform.Translation = VectorMath.Vec3(self.Owner.Transform.Translation.x,self.Owner.Transform.Translation.y,self.hoverZ)
        
    def HoverState(self):
        self.Owner.Sprite.Color = self.HoverColor
        self.Owner.Transform.Translation = VectorMath.Vec3(self.Owner.Transform.Translation.x,self.Owner.Transform.Translation.y,self.hoverZ+5)
        
    def DownState(self):
        self.Owner.Sprite.Color = self.DownColor
        
    def OnMouseEnter(self, MouseEvent):
        self.HoverState()
        
    def OnMouseExit(self, MouseEvent):
        self.DefaultState()
        
    def OnMouseDown(self, MouseEvent):
        self.DownState()
        
    def OnMouseUp(self, MouseEvent):
        self.HoverState()
        self.Owner.Transform.Translation = VectorMath.Vec3(self.Owner.Transform.Translation.x,self.Owner.Transform.Translation.y,self.hoverZ)
        #Places a tower at the cell location if it is valid
        self.cellProp = self.GameLogic.GameLogic.node_array[round(self.Owner.Transform.Translation.x)][-round(self.Owner.Transform.Translation.y)]
        
        if (self.towerChoice == 1 and self.player.money >= self.towerstats.cost1[self.towerstats.towerlevel[0]] and not self.cellProp.tower):
            tower = self.Space.CreateAtPosition("RedTower",self.Owner.Transform.Translation)
            tower.Transform.Translation += Vec3(0,0,1)
            tower.TowerLogic.cost = self.towerstats.cost1[self.towerstats.towerlevel[0]]
            #tower.Sprite.Color = self.towerstats.color1[self.towerstats.towerlevel[0]]
            tower.Sprite.SpriteSource = self.towerstats.sprite1[self.towerstats.towerlevel[0]]
            tower.RedTowerLogic.cost = self.towerstats.cost1[self.towerstats.towerlevel[0]]
            tower.RedTowerLogic.xpos = round(tower.Transform.Translation.x)
            tower.RedTowerLogic.ypos = -round(tower.Transform.Translation.y)
            tower.RedTowerLogic.level = self.towerstats.towerlevel[0]
            self.player.numRed[self.towerstats.towerlevel[0]] += 1
            self.player.money -= self.towerstats.cost1[self.towerstats.towerlevel[0]]
            
        elif (self.towerChoice == 2 and self.player.money >= self.towerstats.cost2[self.towerstats.towerlevel[1]] and not self.cellProp.tower):
            tower = self.Space.CreateAtPosition("BlueTower",self.Owner.Transform.Translation)
            tower.Transform.Translation += Vec3(0,0,1)
            tower.TowerLogic.cost = self.towerstats.cost2[self.towerstats.towerlevel[1]]
            tower.Sprite.Color = self.towerstats.color3[self.towerstats.towerlevel[1]]
            tower.BlueTowerLogic.cost = self.towerstats.cost2[self.towerstats.towerlevel[1]]
            tower.BlueTowerLogic.xpos = round(tower.Transform.Translation.x)
            tower.BlueTowerLogic.ypos = -round(tower.Transform.Translation.y)
            tower.BlueTowerLogic.level = self.towerstats.towerlevel[1]
            self.player.numBlue[self.towerstats.towerlevel[1]] += 1
            self.player.money -= self.towerstats.cost2[self.towerstats.towerlevel[1]]
            
        elif (self.towerChoice == 3 and self.player.money >= self.towerstats.cost3[self.towerstats.towerlevel[2]] and not self.cellProp.tower):
            tower = self.Space.CreateAtPosition("GreenTower",self.Owner.Transform.Translation)
            tower.Transform.Translation += Vec3(0,0,1)
            tower.TowerLogic.cost = self.towerstats.cost3[self.towerstats.towerlevel[2]]
            tower.Sprite.Color = self.towerstats.color2[self.towerstats.towerlevel[2]]
            tower.GreenTowerLogic.cost = self.towerstats.cost3[self.towerstats.towerlevel[2]]
            tower.GreenTowerLogic.xpos = round(tower.Transform.Translation.x)
            tower.GreenTowerLogic.ypos = -round(tower.Transform.Translation.y)
            tower.GreenTowerLogic.level = self.towerstats.towerlevel[2]
            self.player.numGreen[self.towerstats.towerlevel[2]] += 1
            self.player.money -= self.towerstats.cost3[self.towerstats.towerlevel[2]]
            
        elif (self.towerChoice == 4 and self.player.money >= self.towerstats.cost4[self.towerstats.towerlevel[3]] and not self.cellProp.tower):
            tower = self.Space.CreateAtPosition("YellowTower",self.Owner.Transform.Translation)
            tower.Transform.Translation += Vec3(0,0,1)
            tower.TowerLogic.cost = self.towerstats.cost4[self.towerstats.towerlevel[3]]
            tower.Sprite.Color = self.towerstats.color4[self.towerstats.towerlevel[3]]
            tower.YellowTowerLogic.cost = self.towerstats.cost4[self.towerstats.towerlevel[3]]
            tower.YellowTowerLogic.xpos = round(tower.Transform.Translation.x)
            tower.YellowTowerLogic.ypos = -round(tower.Transform.Translation.y)
            tower.YellowTowerLogic.level = self.towerstats.towerlevel[3]
            self.player.numYellow[self.towerstats.towerlevel[3]] += 1
            self.player.money -= self.towerstats.cost4[self.towerstats.towerlevel[3]]
            
        # TOWER REMOVE
        # Finds the tower at the selected location and removes it for half cash back guaranteed
        elif (self.towerChoice == 5 and self.cellProp.tower):
            removexpos = round(self.Owner.Transform.Translation.x)
            removeypos = -round(self.Owner.Transform.Translation.y)
            # Get the list of all obj in the space
            allObjects = self.Space.AllObjects()
            for cog in allObjects:
                if (cog.Sprite):
                    # Nasty hack to retrieve the selected turret
                    cogx = round(cog.Transform.Translation.x)
                    cogy = -round(cog.Transform.Translation.y)
                    cogz = round(cog.Transform.Translation.z)
                    if (cogx == removexpos and cogy == removeypos and cogz == 1):
                        # Get the tower type and give the appropriate money
                        self.player.money += round(cog.TowerLogic.cost / 2)
                        if(cog.Name == "RedTower"):
                            self.player.numRed[cog.RedTowerLogic.level] -= 1
                        if(cog.Name == "GreenTower"):
                            self.player.numGreen[cog.GreenTowerLogic.level] -= 1
                        if(cog.Name == "BlueTower"):
                            self.player.numBlue[cog.BlueTowerLogic.level] -= 1
                        if(cog.Name == "YellowTower"):
                            self.player.numYellow[cog.YellowTowerLogic.level] -= 1
                        cog.Destroy()
                        
                        #Reset node to blank
                        GameLogic = self.Space.FindObjectByName("GameLogic")
                        GameLogic.GameLogic.node_array[removexpos][removeypos].tower = False
                        GameLogic.GameLogic.node_array[removexpos][removeypos].name = 0
                        
                        #Resets the grid weights
                        for i in range(1, GameLogic.GameLogic.xsize - 1):
                            for j in range(1, GameLogic.GameLogic.ysize - 1):
                                GameLogic.GameLogic.node_array[i][j].weight = -2
                                    
                        #Refreshes the grid weights
                        GameLogic.GameLogic.count = 0
                        GameLogic.GameLogic.node_array[GameLogic.GameLogic.endx][GameLogic.GameLogic.endy].weight = 0
                        GameLogic.GameLogic.refreshWeight()
        self.Owner.Transform.Translation = VectorMath.Vec3(self.Owner.Transform.Translation.x,self.Owner.Transform.Translation.y,self.hoverZ+5)
        
        
        
        
        
Zero.RegisterComponent("CellLogic", CellLogic)