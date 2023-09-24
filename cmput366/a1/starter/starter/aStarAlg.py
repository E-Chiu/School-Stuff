from search.algorithms import State
from search.map import Map
import heapq

def aStar(si: State, sg: State, T: Map):
    cost = 0
    expansions = 0
    # openList is a heap
    openList = []
    # closedList is a dict
    closedList = {}

    # add initial node
    si.set_cost = 0;
    heapq.heappush(openList, si)

    closedList[si.state_hash()] = si.get_cost()
    
    while len(openList) > 0:
        currNode = heapq.heappop(openList)
        if currNode == sg:
            return currNode.get_cost(), expansions
        # get the next set of children
        for childNode in T.successors(currNode):
            expansions += 1

            # calculate the f value
            delX = abs(childNode.get_x() - sg.get_x())
            delY = abs(childNode.get_y() - sg.get_y())
            fVal = 1.5 * min(delX, delY) + abs(delX - delY)

            if childNode.state_hash() not in closedList:
                # add the node to closed and open lists
                childNode.set_cost(fVal)
                heapq.heappush(openList, childNode)
                closedList[childNode.state_hash()] = childNode.get_cost()
            if childNode.state_hash() in closedList and fVal < closedList[currNode.state_hash()]:
                # add new node to heap since it is cheaper it will show first
                childNode.set_cost(fVal)
                heapq.heappush(openList, childNode)
                closedList[childNode.state_hash()] = childNode.get_cost()
        # re-heapify list to maintain structure
        heapq.heapify(openList)
    # if loop ends and goal was not found then there was no solution to be found
    return -1, expansions