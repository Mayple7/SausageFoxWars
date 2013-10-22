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
        self.map = 0
        self.zoomMin = 7
        self.zoomMax = 20
        self.MaxScrollX = 0
        self.MinScrollX = 0
        self.MaxScrollY = 0
        self.MinScrollY = 0
        self.MaxScrollSet = 0
        
    def OnLogicUpdate(self, UpdateEvent):
        self.map = self.Space.FindObjectByName("MapCreate")
        self.DeltaTime = UpdateEvent.Dt
        movement = VectorMath.Vec3(0,0,0)
        if(self.map):
            
            if (self.MaxScrollSet == 0):
                self.MaxScrollX = self.map.MapCreate.xsize
                self.MaxScrollY = self.map.MapCreate.ysize
                self.MaxScrollSet = 1
            
            if(Zero.Keyboard.KeyIsDown(Zero.Keys.D) and self.Owner.Transform.Translation.x < self.MaxScrollX):
                movement += VectorMath.Vec3(1,0,0)
            if(Zero.Keyboard.KeyIsDown(Zero.Keys.A) and self.Owner.Transform.Translation.x > self.MinScrollX):
                movement += VectorMath.Vec3(-1,0,0)
            if(Zero.Keyboard.KeyIsDown(Zero.Keys.W) and self.Owner.Transform.Translation.y < self.MinScrollY):
                movement += VectorMath.Vec3(0,1,0)
            if(Zero.Keyboard.KeyIsDown(Zero.Keys.S) and self.Owner.Transform.Translation.y > -self.MaxScrollY):
                movement += VectorMath.Vec3(0,-1,0)
            
            
            if (self.mousePos.x > self.Owner.Transform.Translation.x + ((self.Owner.Camera.Size/2)+.35*self.Owner.Camera.Size)):
                if (self.Owner.Transform.Translation.x < self.MaxScrollX):
                    movement += VectorMath.Vec3(self.Owner.Camera.Size/10,0,0)
            if (self.mousePos.x < self.Owner.Transform.Translation.x - ((self.Owner.Camera.Size/2)+.35*self.Owner.Camera.Size)):
                if (self.Owner.Transform.Translation.x > self.MinScrollX):
                    movement += VectorMath.Vec3(-self.Owner.Camera.Size/10,0,0)
                
            if (self.mousePos.y > self.Owner.Transform.Translation.y + ((self.Owner.Camera.Size/2)-.05*self.Owner.Camera.Size)):
                if (self.Owner.Transform.Translation.y < self.MinScrollY):
                    movement += VectorMath.Vec3(0,self.Owner.Camera.Size/10,0)
            if (self.mousePos.y < self.Owner.Transform.Translation.y - ((self.Owner.Camera.Size/2)-.05*self.Owner.Camera.Size)):
                if (self.Owner.Transform.Translation.y > -self.MaxScrollY):
                    movement += VectorMath.Vec3(0,-self.Owner.Camera.Size/10,0)
        self.Owner.Transform.Translation += movement * UpdateEvent.Dt * 5
    
    def OnMouseUpdate(self, ViewportMouseEvent):
        self.mousePos = ViewportMouseEvent.ToWorldZPlane(0.0)
        if(self.map):
            if ((self.Owner.Camera.Size > self.zoomMin and ViewportMouseEvent.Scroll.y == 1) or (self.Owner.Camera.Size < self.zoomMax and ViewportMouseEvent.Scroll.y == -1)):
                self.Owner.Camera.Size -= ViewportMouseEvent.Scroll.y
            
        
    def OnMouseMove(self, ViewportMouseEvent):
        self.mousePos = ViewportMouseEvent.ToWorldZPlane(0.0)
        if(self.map):
            if ((self.Owner.Camera.Size > self.zoomMin and ViewportMouseEvent.Scroll.y == 1) or (self.Owner.Camera.Size < self.zoomMax and ViewportMouseEvent.Scroll.y == -1)):
                self.Owner.Camera.Size -= ViewportMouseEvent.Scroll.y
        
Zero.RegisterComponent("CameraLogic", CameraLogic)