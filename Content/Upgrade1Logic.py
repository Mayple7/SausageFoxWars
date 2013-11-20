import Zero
import Events
import Property
import VectorMath

Vec4 = VectorMath.Vec4
Vec3 = VectorMath.Vec3

class Upgrade1Logic:
    def Initialize(self, initializer):
        cameraCog = self.Space.FindObjectByName("Camera")
        Zero.Connect(cameraCog.Camera.Viewport, Events.MouseMove, self.OnMouseMove)
        Zero.Connect(self.Owner, Events.MouseEnter, self.OnMouseEnter)
        Zero.Connect(self.Owner, Events.MouseExit, self.OnMouseExit)
        Zero.Connect(self.Owner, Events.MouseDown, self.OnMouseDown)
        Zero.Connect(self.Owner, Events.MouseUp, self.OnMouseUp)
        self.LevelSpace = 0
        
        self.DefaultColor = Vec4(1,0,0,1)
        self.HoverColor = Vec4(1,0,0,.25)
        self.DownColor = Vec4(.5,0,0,.5)
        
        self.DefaultState()
        
    def OnMouseMove(self, ViewportMouseEvent):
        self.mousePosition = ViewportMouseEvent.ToWorldZPlane(0.0)
        
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
        self.towerstats = self.LevelSpace.FindObjectByName("TowerStats").TowerStats
        self.player = self.LevelSpace.FindObjectByName("Player").PlayerLogic
        if(self.towerstats.towerlevel[0] < 3 and self.player.money >= self.towerstats.upgradecost1[self.towerstats.towerlevel[0]]):
            self.player.money -= self.towerstats.upgradecost1[self.towerstats.towerlevel[0]]
            self.towerstats.towerlevel[0] += 1
            if(self.towerstats.towerlevel[0] == 3):
                self.Owner.Destroy()
            else:
                self.Owner.SpriteText.Text = str(self.towerstats.upgradecost1[self.towerstats.towerlevel[0]]) + "g"

        self.HoverState()
        
Zero.RegisterComponent("Upgrade1Logic", Upgrade1Logic)