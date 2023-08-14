import sys
#DEFINING THE GLOBAL VARIABLES
total_cost=0 #the final output of the Uniform_astar gets returned at the total cost
pop_count = 0 # returns the count of the nodes popped 
visited_cities = [] #list that contains cities that has been visited 
fringe=[] 
track_node=[]
track_pathcost=[]
totalcost=0 #total cost is the cost that is passed inside the node 
type=""
generated_count=0
heu_input=[] #stores the heuristic files inputs 
input=[[]] #stores the input1 files inputs 

#READING INPUT FILE AND STORING IT AS A LIST
def read(inp):
    global input
    file_open = open(inp,"r")
    if file_open == None:
        print("Cannot open the file")
    else: 
         input= [i.split() for i in file_open]
          #INCLUDE THIS IF FILE HAS END OF INPUT 
        # input.pop(-1)
        # input.pop(-2)
        # input.pop(-3)
        
#IF HEURISTIC FILE IS PROVIDED, THIS FUNCTION WILL BE USED  
def hue_read(hue):
    global heu_input
    file_open = open(hue,"r")
    if file_open == None:
        print("Cannot open the file")
    else:
        heu_input= [i.split() for i in file_open]
        # heu_input.pop(-1)
        # heu_input.pop(-2)
        # heu_input.pop(-3)

#FUNCTION NAMED Uniform_astar to perform ucs or astar respectively 
def Uniform_astar(start_city,goal_city):

    global fringe,generated_count,visited_cities
    sNode = node(start_city,None,0,0)
    fringe.append(sNode)
    generated_count = generated_count+1
    while(len(fringe)>0 and fringe[0].name != goal_city):
        visited_cities.append(fringe[0].name)
        expand()
        if(type=="heu"):
            addHeuristic()        
        # print(visited_cities)
        #for x in fringe:
        #     print(x.name,x.totalcost)
        # print(pop_count,len(visited_cities),generated_count)

    if(type=="heu" and len(fringe)>0):
        return fringe[0].htotalcost
    elif(len(fringe)>0):
        return fringe[0].totalcost
    else:
        return None
               
def addHeuristic():
    global fringe,heu_input
    for x in fringe:
        for y in heu_input:
            if y[0] == x.name:
                x.cost += int(y[1])
                #print(x.cost)
    return fringe                                        
#FUNCTION WRITTEN TO EXPAND THE NODES    
def expand():
    flag=0
    global fringe,generated_count,visited_cities,pop_count
    tempNode = fringe[0]
    del fringe[0]
    pop_count= pop_count+1
    for x in input:
            if((x[0] == tempNode.name)):
                newNode = node(x[1],tempNode,int(x[2]),int(x[2])+tempNode.cost,int(x[2]),int(x[2])+tempNode.cost)
                fringe.append(newNode)
                generated_count = generated_count+1
                fringe=sorted(fringe,key=lambda node:node.totalcost)
               
            elif((x[1] == tempNode.name) ):
                  
                  newNode = node(x[0],tempNode,int(x[2]),int(x[2])+tempNode.cost,int(x[2]),int(x[2])+tempNode.cost)
                  fringe.append(newNode)
                  generated_count = generated_count+1
                  fringe=sorted(fringe,key=lambda node:node.totalcost)
            #if((x[0] == tempNode.name) and (x[1] in visited_cities) or ((x[1] == tempNode.name) and (x[0] in visited_cities))):
                #pop_count=pop_count+1
                
    while True:
        if(flag == 1):
            break
        if(len(fringe)>0 and fringe[0].name in visited_cities):
            del fringe[0]
            pop_count= pop_count+1
        else:
            flag = 1
            




class node:
    def __init__(self, name,parent,cost,totalcost,hcost=0,htotalcost=0):
        self.name= name
        self.parent=parent
        self.cost=cost
        self.totalcost=totalcost
        self.hcost=hcost
        self.htotalcost=htotalcost

#DEFINING A FUNCTION NAMED NODE TO BACKTRACK THE PATH FROM GOAL TO INPUT 
def route(node):
    global track_node,track_pathcost,totalcost
    while node:
        track_node.append(node.name)
        if(type=="heu"):
            track_pathcost.append(node.htotalcost)
        else:
            track_pathcost.append(node.totalcost)
        node = node.parent
    track_node.reverse()
    track_pathcost.reverse()



def main():
    global input,type,heu_input,total_cost
    leng = len(sys.argv)
    if leng == 4:    
           inp = sys.argv[1]
           start_city = sys.argv[2]
           goal_city = sys.argv[3]
           read(inp)
           total_cost = Uniform_astar(start_city,goal_city)
    if leng==5:
           inp = sys.argv[1]
           start_city = sys.argv[2]
           goal_city = sys.argv[3]
           inp4 = sys.argv[4]
           hue_read(inp4)
           read(inp)
           type = "heu"           
           total_cost = Uniform_astar(start_city,goal_city)
    

    if(total_cost == None):
        print("No possible route")
    else:
        print("Nodes popped", pop_count)
        print("nodes expanded:", len(visited_cities))
        print("nodes generated:", generated_count)
        goal=fringe[0]
        route(goal)
        if(type=="heu"):
            print("Distance:", round(float(total_cost),1),"Km")
        else:
            print("Distance :", round(float(total_cost),1),"Km")
        path_len=len(track_node)
        print("Route: ")
        for i in range(0,path_len-1):
            print(track_node[i],"to",track_node[i+1]," ",(round(float(track_pathcost[i+1]),1))-(round(float(track_pathcost[i]),1)),"Km")

       
    
if __name__ == '__main__':
    main()