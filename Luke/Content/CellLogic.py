import Zero
import Events
import Property
import VectorMath

Vec4 = VectorMath.Vec4
Vec3 = VectorMath.Vec3

class CellLogic:
    def Initialize(self, initializer):
        Zero.Connect(self.Owner, Events.MouseEnter, self.OnMouseEnter)
        Zero.Connect(self.Owner, Events.MouseExit, self.OnMouseExit)
        Zero.Connect(self.Owner, Events.MouseDown, self.OnMouseDown)
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        
        self.DefaultColor = Vec4(1,1,1,1)
        self.HoverColor = Vec4(.75,.75,.75,.75)
        self.DownColor = Vec4(.5,.5,.5,.5)
        self.towerChoice = 1
        
        self.hudspace = Zero.Game.FindSpaceByName("HUDLevel")
        self.select = self.hudspace.FindObjectByName("Selector")
        level = self.Space.FindObjectByName("LevelSettings")
        self.player = level.PlayerLogic
        
        self.DefaultState()
        
        self.GameLogic = self.Space.FindObjectByName("GameLogic")
        
        self.red = self.hudspace.FindObjectByName("RedTower")
        self.blue = self.hudspace.FindObjectByName("BlueTower")
        self.green = self.hudspace.FindObjectByName("GreenTower")
        self.yellow = self.hudspace.FindObjectByName("YellowTower")
    
    def OnLogicUpdate(self, UpdateEvent):
        
        #self.Owner.SpriteText.Text = str(self.GameLogic.GameLogic.node_array[round(self.Owner.Transform.Translation.x)][-round(self.Owner.Transform.Translation.y)].weight)
        
        if(Zero.Keyboard.KeyIsPressed(Zero.Keys.One)):
            self.towerChoice = 1
            self.select.Transform.Translation = Vec3(self.red.Transform.Translation.x, -9, 0)
        elif(Zero.Keyboard.KeyIsPressed(Zero.Keys.Two)):
            self.towerChoice = 2
            self.select.Transform.Translation = Vec3(self.blue.Transform.Translation.x, -9, 0)
        elif(Zero.Keyboard.KeyIsPressed(Zero.Keys.Three)):
            self.towerChoice = 3
            self.select.Transform.Translation = Vec3(self.green.Transform.Translation.x, -9, 0)
        elif(Zero.Keyboard.KeyIsPressed(Zero.Keys.Four)):
            self.towerChoice = 4
            self.select.Transform.Translation = Vec3(self.yellow.Transform.Translation.x, -9, 0)
            
    def DefaultState(self):
        self.Owner.Sprite.Color = self.DefaultColor
        
    def HoverState(self):
        self.Owner.Sprite.Color = self.HoverColor
        
    def DownState(self):
        self.Owner.Sprite.Color = self.DownColor
        
    def OnMouseEnter(self, MouseEvent):
        self.HoverState()
        
    def OnMouseExit(self, MouseEvent):
        self.DefaultState()
        
    def OnMouseDown(self, MouseEvent):
        self.DownState()
        
    def OnMouseUp(self, MouseEvent):
        self.cellProp = self.GameLogic.GameLogic.node_array[round(self.Owner.Transform.Translation.x)][-round(self.Owner.Transform.Translation.y)]
        
        self.HoverState()
        if(self.towerChoice == 1 and self.player.money >= 5 and not self.cellProp.tower):
            tower = self.Space.CreateAtPosition("RedTower",self.Owner.Transform.Translation)
            tower.Transform.Translation += Vec3(0,0,1)
            tower.RedTowerLogic.xpos = round(tower.Transform.Translation.x)
            tower.RedTowerLogic.ypos = -round(tower.Transform.Translation.y)
            self.player.money -= 5
        elif(self.towerChoice == 2 and self.player.money >= 10 and not self.cellProp.tower):
            tower = self.Space.CreateAtPosition("BlueTower",self.Owner.Transform.Translation)
            tower.Transform.Translation += Vec3(0,0,1)
            tower.BlueTowerLogic.xpos = round(tower.Transform.Translation.x)
            tower.BlueTowerLogic.ypos = -round(tower.Transform.Translation.y)
            self.player.money -= 10
        elif(self.towerChoice == 3 and self.player.money >= 25 and not self.cellProp.tower):
            tower = self.Space.CreateAtPosition("GreenTower",self.Owner.Transform.Translation)
            tower.Transform.Translation += Vec3(0,0,1)
            tower.GreenTowerLogic.xpos = round(tower.Transform.Translation.x)
            tower.GreenTowerLogic.ypos = -round(tower.Transform.Translation.y)
            self.player.money -= 25
        elif(self.towerChoice == 4 and self.player.money >= 50 and not self.cellProp.tower):
            tower = self.Space.CreateAtPosition("YellowTower",self.Owner.Transform.Translation)
            tower.Transform.Translation += Vec3(0,0,1)
            tower.YellowTowerLogic.xpos = round(tower.Transform.Translation.x)
            tower.YellowTowerLogic.ypos = -round(tower.Transform.Translation.y)
            self.player.money -= 50
        
Zero.RegisterComponent("CellLogic", CellLogic)