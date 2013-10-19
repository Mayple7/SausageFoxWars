import Zero
import Events
import Property
import VectorMath

class CameraLogic:
    def Initialize(self, initializer):
        cameraCog = self.Space.FindObjectByName("Camera")
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        Zero.Connect(cameraCog, Events.MouseUpdate, self.OnMouseUpdate)
        Zero.Connect(cameraCog, Events.MouseMove, self.OnMouseMove)
        self.mousePos = VectorMath.Vec3(0,0,0)
        
        self.zoomMin = 7
        self.zoomMax = 20
        
    def OnLogicUpdate(self, UpdateEvent):
        self.DeltaTime = UpdateEvent.Dt
        movement = VectorMath.Vec3(0,0,0)
        
        if(Zero.Keyboard.KeyIsDown(Zero.Keys.D)):
            movement += VectorMath.Vec3(1,0,0)
        if(Zero.Keyboard.KeyIsDown(Zero.Keys.A)):
            movement += VectorMath.Vec3(-1,0,0)
        if(Zero.Keyboard.KeyIsDown(Zero.Keys.W)):
            movement += VectorMath.Vec3(0,1,0)
        if(Zero.Keyboard.KeyIsDown(Zero.Keys.S)):
            movement += VectorMath.Vec3(0,-1,0)
            
            
        if (self.mousePos.x > self.Owner.Transform.Translation.x + ((self.Owner.Camera.Size/2)+.35*self.Owner.Camera.Size)):
            movement += VectorMath.Vec3(self.Owner.Camera.Size/10,0,0)
        if (self.mousePos.x < self.Owner.Transform.Translation.x - ((self.Owner.Camera.Size/2)+.35*self.Owner.Camera.Size)):
            movement += VectorMath.Vec3(-self.Owner.Camera.Size/10,0,0)
            
        if (self.mousePos.y > self.Owner.Transform.Translation.y + ((self.Owner.Camera.Size/2)-.05*self.Owner.Camera.Size)):
            movement += VectorMath.Vec3(0,self.Owner.Camera.Size/10,0)
        if (self.mousePos.y < self.Owner.Transform.Translation.y - ((self.Owner.Camera.Size/2)-.05*self.Owner.Camera.Size)):
            movement += VectorMath.Vec3(0,-self.Owner.Camera.Size/10,0)
        
        self.Owner.Transform.Translation += movement * UpdateEvent.Dt * 5
    
    def OnMouseUpdate(self, ViewportMouseEvent):
        self.mousePos = ViewportMouseEvent.ToWorldZPlane(0.0)
        if ((self.Owner.Camera.Size > self.zoomMin and ViewportMouseEvent.Scroll.y == 1) or (self.Owner.Camera.Size < self.zoomMax and ViewportMouseEvent.Scroll.y == -1)):
            self.Owner.Camera.Size -= ViewportMouseEvent.Scroll.y
            
        
    def OnMouseMove(self, ViewportMouseEvent):
        self.mousePos = ViewportMouseEvent.ToWorldZPlane(0.0)
        if ((self.Owner.Camera.Size > self.zoomMin and ViewportMouseEvent.Scroll.y == 1) or (self.Owner.Camera.Size < self.zoomMax and ViewportMouseEvent.Scroll.y == -1)):
            self.Owner.Camera.Size -= ViewportMouseEvent.Scroll.y
        
Zero.RegisterComponent("CameraLogic", CameraLogic)