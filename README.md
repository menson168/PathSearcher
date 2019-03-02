# PathSearcher
## A collection of path searching algorithm in Python3

- This repository is intended to explore path searching algorithm for robotics application (specifically for mobile robots).
- Currently included algorithm:
    - Breadth First Search
      - A simple path searcher that will return a viable path but may not be the shortest path.
    - Dijkstra Algorithm
      - A path searching algorithm that determines a path based on the cost to reach the goal. The Dijkstra Algorithm included in this repository is a slightly modified version. Please see [this](https://www.aaai.org/ocs/index.php/SOCS/SOCS11/paper/viewFile/4017/4357) paper for more detail. 
    - A* Algorithm
      - A variant of Dijkstra. The difference between Dijkstra and A* is that A* utilizes heuristic to determine the cost. A better way to describe A* is that it is the combination of Dijkstra (Using Graph Cost) and Greedy Best First Search (Using Heuristic). 
      - *Heuristic -> This is a "cheat" value that can help the path searcher to determine the "true" cost of the path. Most cases of heuristic is simply the cartesian distance in between nodes.

## Reference
The internet has a great collection of resources on all kinds of knowledge, including search algos. Here is a list of sources that I have referenced to for composing this repo:  
- [https://www.redblobgames.com/pathfinding/a-star/introduction.html](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
- [https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)

## Maintainer
Menson Li  
[menson168@gmail.com](menson168@gmail.com)  
LinkedIn: [Menson's LinkedIn Profile](https://www.linkedin.com/in/mensonli/)