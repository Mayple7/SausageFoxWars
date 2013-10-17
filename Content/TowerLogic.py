import Zero
import Events
import Property
import VectorMath

class TowerLogic:
    def Initialize(self, initializer):
        #Sets the tower's location
        self.currentx = round(self.Owner.Transform.Translation.x)
        self.currenty = round(-1*(self.Owner.Transform.Translation.y))
        
        self.cost = 0
        
        #Sets the cell to have a tower and name
        GameLogic =self.Space.FindObjectByName("GameLogic")
        GameLogic.GameLogic.node_array[self.currentx][self.currenty].tower = True
        GameLogic.GameLogic.node_array[self.currentx][self.currenty].name = self.Owner
        
        #Resets the grid weights
        for i in range(1, GameLogic.GameLogic.xsize-1):
            for j in range(1, GameLogic.GameLogic.ysize-1):
                GameLogic.GameLogic.node_array[i][j].weight = -2
                    
        #Refreshes the grid weights
        GameLogic.GameLogic.count = 0
        GameLogic.GameLogic.node_array[GameLogic.GameLogic.endx][GameLogic.GameLogic.endy].weight = 0
        GameLogic.GameLogic.refreshWeight()
        
Zero.RegisterComponent("TowerLogic", TowerLogic)