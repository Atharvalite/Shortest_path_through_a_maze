
class Graph:
    def __init__(self,start,end,obstacles) :
        self.xi=start[0]
        self.yi=start[1]
        self.xz=end[0]
        self.yz=end[1]
        self.obstacles=obstacles 
        self.moves=[(1,0),(0,1),(0,-1),(-1,0)]
        self.visited=[]
        self.paths=[]

    def Heuristic(self,x1,y1):
        return abs(self.yz-y1)+abs(self.xz-x1)
    
    def Possible_Move(self,x,y,cost):
        f_val=6000
        flag=False
        for i in self.moves:
            dx=i[0]
            dy=i[1]
            if ((x+dx,y+dy) not in self.obstacles and 
            (x+dx,y+dy) not in self.visited and
            x+dx>=0 and x+dx<=100 and y+dx>=0 and y+dx<=100):
                flag=True
                f= self.Heuristic(x+dx,y+dy)+cost+1
                if f<f_val:
                    f_val=f
                    delx=dx
                    dely=dy 

        if (flag):
            return (x+delx,y+dely,cost+1)
        return None 

    
    def Path_update(self,x,y,xold,yold):
        l=[]
        for i in self.paths:
            if i[0]==(xold,yold):
                l=list(i[1])
                l.append((x,y))
                self.paths.append(((x,y),l))
                return 

    def F_val(self,val):
        x,y,cost=val
        return cost + self.Heuristic(x,y)


    def Search(self):
        x=self.xi
        y=self.yi 
        cost=0
        open_list=[]
        count=0

        open_list.append((x,y,cost))
        self.visited.append((x,y))
        path=((x,y),((x,y)))
        self.paths.append(path)

        while(x!=self.xz or y!=self.yz):
            open_list.sort( key=self.F_val, reverse=True)
            x,y,cost=open_list[count]
            
            xold,yold=x,y 

            if (self.Possible_Move(x,y,cost)!=None):

                x,y,cost=self.Possible_Move(x,y,cost)
                open_list.append((x,y,cost))
                self.visited.append((x,y))
                
                self.Path_update(x,y,xold,yold)
                count+=1
            
            else:

                count-=1
                open_list.pop()

            
            if not open_list:
                return None
        
        return self.paths[-1][1]

            
