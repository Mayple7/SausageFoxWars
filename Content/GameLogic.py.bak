import Zero
import Events
import Property
import VectorMath

class GameLogic:
    def Initialize(self, initializer):
        self.xsize = 30
        self.ysize = 10
        self.node_array = [[[0]*self.ysize for i in range(self.ysize)][0]*self.xsize for i in range(self.xsize)]
        self.endx = 2
        self.endy = 3
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
        
        self.refreshWeight(self.endx, self.endy)
            
        
    def refreshWeight(self, i, j):
        down = self.node_array[i][j+1]
        up = self.node_array[i][j-1]
        right = self.node_array[i+1][j]
        left = self.node_array[i-1][j]
        current = self.node_array[i][j]
        
        current.check_down = False
        current.check_up = False
        current.check_right = False
        current.check_left = False
        
        if(down.weight == -1):
            pass
        elif(down.tower):
            if(down.weight > current.weight+1001 or down.weight == -2):
                down.weight = current.weight+1001
                current.check_down = True
                #self.refreshWeight(i, j+1)
        elif(down.weight == -2):
            down.weight = current.weight+1
            current.check_down = True
            #self.refreshWeight(i, j+1)
        elif(down.weight > current.weight+1):
            down.weight = current.weight+1
            current.check_down = True
            #self.refreshWeight(i, j+1)
        
        if(left.weight == -1):
            pass
        elif(left.tower):
            if(left.weight > current.weight+1001 or left.weight == -2):
                left.weight = current.weight+1001
                current.check_left = True
                #self.refreshWeight(i-1, j)
        elif(left.weight == -2):
            left.weight = current.weight+1
            current.check_left = True
            #self.refreshWeight(i-1, j)
        elif(left.weight > current.weight+1):
            left.weight = current.weight+1
            current.check_left = True
            #self.refreshWeight(i-1, j)
            
        if(up.weight == -1):
            pass
        elif(up.tower):
            if(up.weight > current.weight+1001 or up.weight == -2):
                up.weight = current.weight+1001
                current.check_up = True
                #self.refreshWeight(i, j-1)
        elif(up.weight == -2):
            up.weight = current.weight+1
            current.check_up = True
            #self.refreshWeight(i, j-1)
        elif(up.weight > current.weight+1):
            up.weight = current.weight+1
            current.check_up = True
            #self.refreshWeight(i, j-1)
            
        if(right.weight == -1):
            pass
        elif(right.tower):
            if(right.weight > current.weight+1001 or right.weight == -2):
                right.weight = current.weight+1001
                current.check_right = True
                #self.refreshWeight(i+1, j)
        elif(right.weight == -2):
            right.weight = current.weight+1
            current.check_right = True
            #self.refreshWeight(i+1, j)
        elif(right.weight > current.weight+1):
            right.weight = current.weight+1
            current.check_right = True
            #self.refreshWeight(i+1, j)
        
        #print(str(i) + " : " + str(j))
        #print(str(check_down) + str(check_left) + str(check_up) + str(check_right))
        
        
        if(current.check_right):
            self.refreshWeight(i+1, j)
        if(current.check_left):
            self.refreshWeight(i-1, j)
        if(current.check_up):
            self.refreshWeight(i, j-1)
        if(current.check_down):
            self.refreshWeight(i, j+1)
        
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