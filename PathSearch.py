#!/usr/bin/env python3

# PathSearch.py
# The main python file for this repo. Documents all the search algorithms and helper function.

# Import the library module
import PathSearchLib as pslib


# Path Parser
def getPathFromVisitHistory(visited_nodes, start_node, goal_node):
    # Parse the path from visit history in the reverse direction (From goal)
    ## Init the current parsing node variable with the goal
    current_parsing_node = goal_node
    ## Declare an empty path list
    path = []
    ## Recursively parse (back track) the visit history until the start point is reached  
    while current_parsing_node != start_node:
        path.append(current_parsing_node)
        current_parsing_node = visited_nodes[current_parsing_node]
    ## Add the start node back into the path because that's skipped in the loop
    path.append(start_node)
    ## Reverse the path because we back tracked the history to create the path
    path.reverse()

    return path

# Breadth First Search
def breadthFirstSearch(graph, start_node, goal_node):
    # Declare the "frontier" list 
    unvisited_nodes = pslib.Queue()
    # Initialize the frontier list with the start node
    unvisited_nodes.put(start_node)
    # Declare the visit history list
    visit_history = {}
    # Initialize the visit history list 
    visit_history[start_node] = None
    
    # Recursively look for the goal and traverse through the graph
    ## While the unvisited node list is NOT empty
    while not unvisited_nodes.empty():
        # Get the first unvisited node from the list
        current_node = unvisited_nodes.get()
        #print("Currently visiting node: " + str(current_node))

        if(goal_node == current_node):
            # Break the recurring search loop if the goal has been found
            break

        for next in graph.getNeighbors(current_node):
            if next not in visit_history:
                unvisited_nodes.put(next)
                visit_history[next] = current_node
    
    path = getPathFromVisitHistory(visit_history, start_node, goal_node)

    ### RETURN THE PATH
    return path

# Dijkstra Search 
def dijkstra_search(weighted_graph, start_node, goal_node):
    # Declare and Initialize the unvisited node list
    ## Please note that the cost is equivalent to the priority of the P_queue (min heap, so smallest cost (priority) is serviced first)
    unvisited_nodes = pslib.PriorityQueue()
    # Init the first node with start node and set the cost to 0
    unvisited_nodes.put(start_node, 0)
    # Declare visited node list
    visited_node_list = {}
    # Declare list to record cost
    cost_of_visit = {}
    # Init the visited node list with start
    visited_node_list[start_node] = None
    # Init the cost of visit to the first node as 0
    cost_of_visit[start_node] = 0

    # Recursively look for a path
    while not unvisited_nodes.empty():
        # Store the current node
        current_visiting_node = unvisited_nodes.get()

        # Check if the current visiting node is already the goal
        if current_visiting_node == goal_node:
            break
        # If goal not reached, look for the neighbors of the current node and branch out on the shortest path tree set (visited_node)
        for next in weighted_graph.getConnection(current_visiting_node):
            updated_cost = cost_of_visit[current_visiting_node] + next[1]
            if next[0] not in cost_of_visit or updated_cost < cost_of_visit[next[0]]:
                cost_of_visit[next[0]] = updated_cost
                unvisited_nodes.put(next[0], updated_cost) 
                visited_node_list[next[0]] = current_visiting_node

    path = getPathFromVisitHistory(visited_node_list, start_node, goal_node)

    return path

######### Main Function #########
def main():
    ## Example for a simple BFS
    example_graph = pslib.SimpleGraph()
    example_graph.edges = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['A'],
        'D': ['E', 'A'],
        'E': ['B']
    }    
    bfs_path = breadthFirstSearch(example_graph, 'B', 'E')
    print("BFS Path is: " + str(bfs_path))
    
    ## Example for a Dijkstra
    dijkstra_ex_graph = pslib.WeightedGraph()
    dijkstra_ex_graph.NodeList = {
        'A': [('B', 3)],
        'B': [('A',4), ('C',2), ('D',9), ('E',7)],
        'C': [('A',5)],
        'D': [('E',8), ('A',1)],
        'E': [('B',4), ('D', 1)]
    }
    dijkstra_path = dijkstra_search(dijkstra_ex_graph, 'A', 'D')
    print("Dijkstra Shortest Path is: " + str(dijkstra_path))
    return

if __name__== "__main__":
    main()