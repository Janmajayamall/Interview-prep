class Destination():
    
    def __init__(self):
        self.destinations = []
    
    def add(self, val, flag):
        self.destinations.append(val)
        if flag:
            self.destinations.sort()

    
    def pop(self):
        if len(self.destinations)==0:
            return None
        else:
            temp = self.destinations[0]
            self.destinations=self.destinations[1:]
            return temp
        
    def size(self):
        return len(self.destinations)

class Solution:
                
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        def dfs (current, airports, final_list):
    
            while current in airports.keys() and airports[current].size()>0:
                temp = airports[current].pop() 
                dfs(temp, airports, final_list)
            
            final_list.append(current)
        
        
        airports={}

        for i in range(len(tickets)):
            
            if tickets[i][0] not in airports.keys():
                temp_node = Destination()
                temp_node.add(tickets[i][1], True)
                airports[tickets[i][0]]=temp_node
            
            else:
                airports[tickets[i][0]].add(tickets[i][1], True)

        initial_air = 'JFK'
        final_list = []
        dfs('JFK', airports, final_list)
        
                
        return final_list[::-1]
                
                
                
        