import Zero
import Events
import Property
import VectorMath

class TowerLogic:
    def Initialize(self, initializer):
        self.currentx = round(self.Owner.Transform.Translation.x)
        self.currenty = round(-1*(self.Owner.Transform.Translation.y))
        
        GameLogic =self.Space.FindObjectByName("GameLogic")
        GameLogic.GameLogic.node_array[self.currentx][self.currenty].weight += 1000
        GameLogic.GameLogic.node_array[self.currentx][self.currenty].tower = True
        GameLogic.GameLogic.node_array[self.currentx][self.currenty].name = self.Owner
        #print(str(self.currentx) + " : " + str(self.currenty))
        for i in range(1, GameLogic.GameLogic.xsize-1):
            for j in range(1, GameLogic.GameLogic.ysize-1):
                GameLogic.GameLogic.node_array[i][j].weight = -2
                    
        #GameLogic.GameLogic.printField()
        #print("Tower Add")
        GameLogic.GameLogic.count = 0
        GameLogic.GameLogic.node_array[GameLogic.GameLogic.endx][GameLogic.GameLogic.endy].weight = 0
        #GameLogic.GameLogic.refreshWeight(GameLogic.GameLogic.endx, GameLogic.GameLogic.endy)
        GameLogic.GameLogic.refreshWeight()
        
        #GameLogic.GameLogic.printField()
        
        

Zero.RegisterComponent("TowerLogic", TowerLogic)