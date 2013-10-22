import Zero
import Events
import Property
import VectorMath
import random
import math

class WallLogic:
    def Initialize(self, initializer):
        self.Owner.Transform.Rotation = VectorMath.Quat(0,0,math.radians(random.randint(0,3) * 90))
        pass

Zero.RegisterComponent("WallLogic", WallLogic)