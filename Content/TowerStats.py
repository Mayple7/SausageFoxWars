import Zero
import Events
import Property
import VectorMath
import Color

class TowerStats:
    def Initialize(self, initializer):
        self.race = 1
        self.towerlevel = [[0] * 4 for i in range(4)]
        
        self.cost1 = [[1] * 4 for i in range(4)]
        self.cost2 = [[1] * 4 for i in range(4)]
        self.cost3 = [[1] * 4 for i in range(4)]
        self.cost4 = [[1] * 4 for i in range(4)]
        
        self.damage1 = [[1] * 4 for i in range(4)]
        self.damage2 = [[1] * 4 for i in range(4)]
        self.damage3 = [[1] * 4 for i in range(4)]
        self.damage4 = [[1] * 4 for i in range(4)]
        
        self.cooldown1 = [[1] * 4 for i in range(4)]
        self.cooldown2 = [[1] * 4 for i in range(4)]
        self.cooldown3 = [[1] * 4 for i in range(4)]
        self.cooldown4 = [[1] * 4 for i in range(4)]
        
        self.color1 = [[1] * 4 for i in range(4)]
        self.color2 = [[1] * 4 for i in range(4)]
        self.color3 = [[1] * 4 for i in range(4)]
        self.color4 = [[1] * 4 for i in range(4)]
        
        self.range1 = 3
        self.range2 = 3
        self.range3 = 2
        self.range4 = 8
        
        self.bullet1 = 0
        self.bullet2 = 1
        self.bullet3 = 3
        self.bullet4 = 0
        
        self.upgradecost1 = [[0] * 3 for i in range(3)]
        self.upgradecost2 = [[0] * 3 for i in range(3)]
        self.upgradecost3 = [[0] * 3 for i in range(3)]
        self.upgradecost4 = [[0] * 3 for i in range(3)]
        
        
        
    def setRace1(self):
        self.race = 1
        
        #Initialize the tower levels to 0
        for i in range(4):
            self.towerlevel[i] = 0
        
        #Race 1 Tower 1 Scaling
        self.cost1[0] = 10
        self.cost1[1] = 20
        self.cost1[2] = 30
        self.cost1[3] = 40
        
        self.damage1[0] = 0
        self.damage1[1] = 20
        self.damage1[2] = 40
        self.damage1[3] = 100
        
        self.cooldown1[0] = 1.5
        self.cooldown1[1] = 1.25
        self.cooldown1[2] = 1
        self.cooldown1[3] = 0.75
        
        self.color1[0] = Color.Red
        self.color1[1] = Color.MistyRose
        self.color1[2] = Color.DarkSalmon
        self.color1[3] = Color.IndianRed
        
        self.upgradecost1[0] = 100
        self.upgradecost1[1] = 300
        self.upgradecost1[2] = 500
        
        #Race 1 Tower 2 Scaling
        self.cost2[0] = 10
        self.cost2[1] = 10
        self.cost2[2] = 10
        self.cost2[3] = 10
        
        self.damage2[0] = 0
        self.damage2[1] = 20
        self.damage2[2] = 40
        self.damage2[3] = 100
        
        self.cooldown2[0] = 1.5
        self.cooldown2[1] = 1.25
        self.cooldown2[2] = 1
        self.cooldown2[3] = 0.75
        
        self.color2[0] = Color.Green
        self.color2[1] = Color.DarkOliveGreen
        self.color2[2] = Color.SpringGreen
        self.color2[3] = Color.ForestGreen
        
        self.upgradecost2[0] = 100
        self.upgradecost2[1] = 300
        self.upgradecost2[2] = 500
        
        #Race 1 Tower 3 Scaling
        self.cost3[0] = 10
        self.cost3[1] = 10
        self.cost3[2] = 10
        self.cost3[3] = 10
        
        self.damage3[0] = 0
        self.damage3[1] = 20
        self.damage3[2] = 40
        self.damage3[3] = 100
        
        self.cooldown3[0] = 1.5
        self.cooldown3[1] = 1.25
        self.cooldown3[2] = 1
        self.cooldown3[3] = 0.75
        
        self.color3[0] = Color.Blue
        self.color3[1] = Color.DeepSkyBlue
        self.color3[2] = Color.RoyalBlue
        self.color3[3] = Color.MidnightBlue
        
        self.upgradecost3[0] = 100
        self.upgradecost3[1] = 300
        self.upgradecost3[2] = 500
        
        #Race 1 Tower 4 Scaling
        self.cost4[0] = 10
        self.cost4[1] = 10
        self.cost4[2] = 10
        self.cost4[3] = 10
        
        self.damage4[0] = 0
        self.damage4[1] = 20
        self.damage4[2] = 40
        self.damage4[3] = 100
        
        self.cooldown4[0] = 1.5
        self.cooldown4[1] = 1.25
        self.cooldown4[2] = 1
        self.cooldown4[3] = 0.75
        
        self.color4[0] = Color.Yellow
        self.color4[1] = Color.Goldenrod
        self.color4[2] = Color.Orange
        self.color4[3] = Color.Gold
        
        self.upgradecost4[0] = 100
        self.upgradecost4[1] = 300
        self.upgradecost4[2] = 500
        
        #Race 1 level 1 tower range
        self.range1 = 5
        self.range2 = 4
        self.range3 = 3
        self.range4 = 8
        
        #Race 1 bullet types
        self.bullet1 = 0
        self.bullet2 = 1
        self.bullet3 = 3
        self.bullet4 = 0
        
        self.Space.CreateAtPosition("Upgrade1", VectorMath.Vec3(9.5, -10.5, 0))
        self.Space.CreateAtPosition("Upgrade2", VectorMath.Vec3(13.5, -10.5, 0))
        self.Space.CreateAtPosition("Upgrade3", VectorMath.Vec3(17.5, -10.5, 0))
        self.Space.CreateAtPosition("Upgrade4", VectorMath.Vec3(21.5, -10.5, 0))
        
    def setRace2(self):
        self.race = 2
        
        #Initialize the tower levels to 0
        for i in range(4):
            self.towerlevel[i] = 0
        
        #Race 2 Tower 1 Scaling
        self.cost1[0] = 10
        self.cost1[1] = 10
        self.cost1[2] = 10
        self.cost1[3] = 10
        
        self.damage1[0] = 0
        self.damage1[1] = 20
        self.damage1[2] = 40
        self.damage1[3] = 100
        
        self.cooldown1[0] = 1.5
        self.cooldown1[1] = 1.25
        self.cooldown1[2] = 1
        self.cooldown1[3] = 0.75
        
        #Race 2 Tower 2 Scaling
        self.cost2[0] = 10
        self.cost2[1] = 10
        self.cost2[2] = 10
        self.cost2[3] = 10
        
        self.damage2[0] = 0
        self.damage2[1] = 20
        self.damage2[2] = 40
        self.damage2[3] = 100
        
        self.cooldown2[0] = 1.5
        self.cooldown2[1] = 1.25
        self.cooldown2[2] = 1
        self.cooldown2[3] = 0.75
        
        #Race 2 Tower 3 Scaling
        self.cost3[0] = 10
        self.cost3[1] = 10
        self.cost3[2] = 10
        self.cost3[3] = 10
        
        self.damage3[0] = 0
        self.damage3[1] = 20
        self.damage3[2] = 40
        self.damage3[3] = 100
        
        self.cooldown3[0] = 1.5
        self.cooldown3[1] = 1.25
        self.cooldown3[2] = 1
        self.cooldown3[3] = 0.75
        
        #Race 2 Tower 4 Scaling
        self.cost4[0] = 10
        self.cost4[1] = 10
        self.cost4[2] = 10
        self.cost4[3] = 10
        
        self.damage4[0] = 0
        self.damage4[1] = 20
        self.damage4[2] = 40
        self.damage4[3] = 100
        
        self.cooldown4[0] = 1.5
        self.cooldown4[1] = 1.25
        self.cooldown4[2] = 1
        self.cooldown4[3] = 0.75
        
        #Race 2 level 1 tower range
        self.range1 = 5
        self.range2 = 4
        self.range3 = 3
        self.range4 = 8
        
        #Race 2 bullet types
        self.bullet1 = 0
        self.bullet2 = 1
        self.bullet3 = 3
        self.bullet4 = 0
        
        self.Space.CreateAtPosition("Upgrade1", VectorMath.Vec3(9.5, -10.5, 0))
        self.Space.CreateAtPosition("Upgrade2", VectorMath.Vec3(13.5, -10.5, 0))
        self.Space.CreateAtPosition("Upgrade3", VectorMath.Vec3(17.5, -10.5, 0))
        self.Space.CreateAtPosition("Upgrade4", VectorMath.Vec3(21.5, -10.5, 0))
        
    def setRace3(self):
        self.race = 3
        
        #Initialize the tower levels to 0
        for i in range(4):
            self.towerlevel[i] = 0
            
        #Race 3 Tower 1 Scaling
        self.cost1[0] = 10
        self.cost1[1] = 10
        self.cost1[2] = 10
        self.cost1[3] = 10
        
        self.damage1[0] = 0
        self.damage1[1] = 20
        self.damage1[2] = 40
        self.damage1[3] = 100
        
        self.cooldown1[0] = 1.5
        self.cooldown1[1] = 1.25
        self.cooldown1[2] = 1
        self.cooldown1[3] = 0.75
        
        #Race 3 Tower 2 Scaling
        self.cost2[0] = 10
        self.cost2[1] = 10
        self.cost2[2] = 10
        self.cost2[3] = 10
        
        self.damage2[0] = 0
        self.damage2[1] = 20
        self.damage2[2] = 40
        self.damage2[3] = 100
        
        self.cooldown2[0] = 1.5
        self.cooldown2[1] = 1.25
        self.cooldown2[2] = 1
        self.cooldown2[3] = 0.75
        
        #Race 3 Tower 3 Scaling
        self.cost3[0] = 10
        self.cost3[1] = 10
        self.cost3[2] = 10
        self.cost3[3] = 10
        
        self.damage3[0] = 0
        self.damage3[1] = 20
        self.damage3[2] = 40
        self.damage3[3] = 100
        
        self.cooldown3[0] = 1.5
        self.cooldown3[1] = 1.25
        self.cooldown3[2] = 1
        self.cooldown3[3] = 0.75
        
        #Race 3 Tower 4 Scaling
        self.cost4[0] = 10
        self.cost4[1] = 10
        self.cost4[2] = 10
        self.cost4[3] = 10
        
        self.damage4[0] = 0
        self.damage4[1] = 20
        self.damage4[2] = 40
        self.damage4[3] = 100
        
        self.cooldown4[0] = 1.5
        self.cooldown4[1] = 1.25
        self.cooldown4[2] = 1
        self.cooldown4[3] = 0.75
        
        #Race 3 level 1 tower range
        self.range1 = 5
        self.range2 = 4
        self.range3 = 3
        self.range4 = 8
        
        #Race 3 bullet types
        self.bullet1 = 0
        self.bullet2 = 1
        self.bullet3 = 3
        self.bullet4 = 0
        
        self.Space.CreateAtPosition("Upgrade1", VectorMath.Vec3(9.5, -10.5, 0))
        self.Space.CreateAtPosition("Upgrade2", VectorMath.Vec3(13.5, -10.5, 0))
        self.Space.CreateAtPosition("Upgrade3", VectorMath.Vec3(17.5, -10.5, 0))
        self.Space.CreateAtPosition("Upgrade4", VectorMath.Vec3(21.5, -10.5, 0))
        

Zero.RegisterComponent("TowerStats", TowerStats)