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
        
        #Sets up the array for cell
        self.node_array = [[[0]*self.ysize for i in range(self.ysize)][0]*self.xsize for i in range(self.xsize)]
        self.count = 0
        #Initializes the play field
        for i in range(self.xsize):
            for j in range(self.ysize):
                #Sets up the play field for the walls
                if(i == 0 or i == self.xsize-1 or j == 0 or j == self.ysize-1):
                    self.node_array[i][j] = Cell()
                    self.node_array[i][j].Initialize(1)
                    self.node_array[i][j].weight = -1
                    
                #Sets up the cell play field
                else:
                    self.node_array[i][j] = Cell()
                    self.node_array[i][j].Initialize(1)
                
        #Sets the end point weight to 0
        self.node_array[self.endx][self.endy].weight = 0
        
        #Refreshes all the weight
        self.refreshWeight()
            
        
    def refreshWeight(self):
        #Resets the end point to 0 and starting loop variables
        self.count += 1
        self.node_array[self.endx][self.endy].weight = 0
        completeRefresh = False
        
        #Loops through the entire play field
        for i in range(1, self.xsize - 1):
            for j in range(1, self.ysize - 1):
                self.count += 1
                
                #Saves each side of the current cell to variables
                down = self.node_array[i][j+1]
                up = self.node_array[i][j-1]
                right = self.node_array[i+1][j]
                left = self.node_array[i-1][j]
                current = self.node_array[i][j]
                
                #Sets the base minimum to a very large number
                minimum = 1000000000
                
                #Finds the minimum weight between all the sides
                if(down.weight >= 0):
                    minimum = min(minimum, down.weight)
                if(up.weight >= 0):
                    minimum = min(minimum, up.weight)
                if(right.weight >= 0):
                    minimum = min(minimum, right.weight)
                if(left.weight >= 0):
                    minimum = min(minimum, left.weight)
                    
                #Different weight if the cell has a tower also sets a variable to re-loop if something changed
                if(current.tower):
                    if(minimum != 1000000000 and current.weight > minimum + 1001 or current.weight == -2):
                        current.weight = minimum + 1001
                        completeRefresh = True
                elif(minimum != 1000000000 and (current.weight > minimum + 1 or current.weight == -2)):
                    current.weight = minimum + 1
                    completeRefresh = True
        
        #Calls the function again if it needs to
        if(completeRefresh):
            self.refreshWeight()
        
    #Prints the entire grid
    def printField(self):
        for i in range(self.xsize):
            for j in range(self.ysize):
                print(self.node_array[i][j].weight)
            print("------------------------")
            

#Houses all the cell information
class Cell:
    def Initialize(self, initializer):
        self.weight = -2
        self.tower = False
        self.mob = False
        self.name = 0

Zero.RegisterComponent("GameLogic", GameLogic)