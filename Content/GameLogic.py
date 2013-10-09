import Zero
import Events
import Property
import VectorMath

'''

sweg

 0+ Empty spaces
 -1 Wall
 -2 Unnassigned

'''

class GameLogic:
    def Initialize(self, initializer):
        #Snatches the size and end from the MapCreate script
        self.xsize = self.Space.FindObjectByName("LevelSettings").MapCreate.xsize
        self.ysize = self.Space.FindObjectByName("LevelSettings").MapCreate.ysize
        
        self.endx = self.Space.FindObjectByName("LevelSettings").MapCreate.endx
        self.endy = self.Space.FindObjectByName("LevelSettings").MapCreate.endy
        
        self.node_array = [[[0]*self.ysize for i in range(self.ysize)][0]*self.xsize for i in range(self.xsize)]
        self.count = 0
        for i in range(self.xsize):
            for j in range(self.ysize):
                if(i == 0 or i == self.xsize-1 or j == 0 or j == self.ysize-1):
                    self.node_array[i][j] = Cell()
                    self.node_array[i][j].Initialize(1)
                    self.node_array[i][j].weight = -1
                    
                else:
                    self.node_array[i][j] = Cell()
                    self.node_array[i][j].tower = False
                    self.node_array[i][j].check_down = False
                    self.node_array[i][j].check_up = False
                    self.node_array[i][j].check_left = False
                    self.node_array[i][j].check_right = False
                    self.node_array[i][j].weight = -2
                    self.node_array[i][j].name = 0
                
        self.node_array[self.endx][self.endy].weight = 0
        
        self.refreshWeight()
            
        
    def refreshWeight(self):
        self.count += 1
        self.node_array[self.endx][self.endy].weight = 0
        completeRefresh = False
        
        for i in range(1, self.xsize - 1):
            for j in range(1, self.ysize - 1):
                self.count += 1
                
                down = self.node_array[i][j+1]
                up = self.node_array[i][j-1]
                right = self.node_array[i+1][j]
                left = self.node_array[i-1][j]
                
                current = self.node_array[i][j]
                minimum = 1000000000
                
                if(down.weight >= 0):
                    minimum = min(minimum, down.weight)
                if(up.weight >= 0):
                    minimum = min(minimum, up.weight)
                if(right.weight >= 0):
                    minimum = min(minimum, right.weight)
                if(left.weight >= 0):
                    minimum = min(minimum, left.weight)
                    
                
                if(current.tower):
                    if(minimum != 1000000000 and current.weight > minimum + 1001 or current.weight == -2):
                        current.weight = minimum + 1001
                        completeRefresh = True
                elif(minimum != 1000000000 and (current.weight > minimum + 1 or current.weight == -2)):
                    current.weight = minimum + 1
                    completeRefresh = True
                        
        if(completeRefresh):
            self.refreshWeight()
        
    def printField(self):
        for i in range(self.xsize):
            for j in range(self.ysize):
                print(self.node_array[i][j].weight)
            print("------------------------")
            

class Cell:
    def Initialize(self, initializer):
        self.weight = -2
        self.wall = False
        self.tower = False
        self.mob = False
        self.name = 0
        self.check_down = False
        self.check_up = False
        self.check_left = False
        self.check_right = False

Zero.RegisterComponent("GameLogic", GameLogic)