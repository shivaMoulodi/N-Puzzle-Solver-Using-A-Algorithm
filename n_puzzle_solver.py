class Node:
    def __init__(self,data,gn,fn):
        self.data = data
        self.gn = gn
        self.fn = fn
        
    def generate_child(self):
        """ Generate child nodes by moving the blank space in four directions {up,down,left,right} """
        x,y = self.find(self.data,'_')
        move_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in move_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.gn+1,0)
                children.append(child_node)
        return children
        
    def find(self,puz,x):
        """ find the position of the blank space """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j
                
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space and value out of limits return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
    
    def copy(self,root):
        """ create a similar matrix for move"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
           
class Puzzle:
    def __init__(self,size):
        self.n = size
        self.open = []
        self.closed = []
        
    def get_input(self):
        """ Accepts the puzzle from the user """
        input_state = []
        for i in range(0,self.n):
            temp = input().split(" ")
            input_state.append(temp)
        return input_state
        
    def f(self,current_state,goal_state):
        """ f(x) = h(x) + g(x) """
        x = self.h(current_state.data,goal_state) + current_state.gn
        return x
    
    def h(self,current_state,goal_state):
        """ Calculates the different between the current_state and goal_state """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if current_state[i][j] != goal_state[i][j] and current_state[i][j] != '_':
                    temp += 1
        return temp
             
    def process(self):
        """ Accept Current and Goal Puzzle state"""
        print("Please enter current state: ")
        current_state = self.get_input()
        print("\n Please enter goal state: ")
        goal_state = self.get_input()
         
        """ Extend current_state node """
        current_state = Node(current_state, 0, 0)
        current_state.fn = self.f(current_state,goal_state)
        """ Put the current_state node in the open list"""
        self.open.append(current_state)
        
        while True:
            print("\n")
            current = self.open[0]
            for i in current.data:
                for j in i:
                    print(j,end=" ")
                print("")
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.h(current.data,goal_state) == 0):
                break
            for i in current.generate_child():
                i.fn = self.f(i,goal_state)
                self.open.append(i)
            self.closed.append(current)
            del self.open[0]

            """ sort the open list based on f """
            self.open.sort(key = lambda x:x.fn,reverse=False)
            
main = Puzzle(3)
main.process()
