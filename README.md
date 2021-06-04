# Search Algorithms in AI

This repo is about demonstration of various search techniques used in artificial intelligence

---

## Introduction

### Local Search Techniques

These techniques are used when the state space is very large (close to infinity) and it is not affordable to keep a track all the explored and unexplored nodes

1. Simple Hill Climbing

   -  This algorithm requires to maintain only the current state rather than all the explored states.
   -  It greedily accepts the move which leads to the solution rather than checking all the moves possible from that state, hence it may fall into the traps of local maximum, plateaus and ridges.
   -  It is not optimal.
   -  It is complete as it surely stops when there is no other state better than the current state.
   -  Eg. N Queens problem
   -  More information can be found [here](https://en.wikipedia.org/wiki/Hill_climbing)

2. Steepest Ascent Hill Climbing

   -  This algorithm requires to maintain only the current state rather than all the explored states.
   -  It accepts the move which leads to the best possible state from the current state by applying all the moves and selecting the best of output, but it too suffers from local maximum, plateaus and ridges.
   -  It is not optimal.
   -  It is complete as it surely ends when there is no other state better than the current state.
   -  Eg. Gradient descent
   -  More information can be found [here](https://en.wikipedia.org/wiki/Hill_climbing)

3. Simulated Annealing

   -  This algorithm is similar to Simple Hill Climbing, however it may select a move which is not better than the current state depending on a certain probability. This probability keeps on decreasing with every iteration. Hence if the algorithm gets stuck at the local maximum, plateaus or ridges it has a high probability of getting out of that state in the beginning phase of the algorithm. If it happens that the algorithm continues on for many iterations the probability of selecting sub optimal moves decreases to value close to zero, hence for later phase this algorithm is same as Simple Hill Climbing.
   -  It is complete.
   -  It is not optimal.
   -  It requires very less state information (only one state)
   -  Eg. Used in searches where path is not required and the state space is not uniform (i.e. it has many local maximas, ridges and plateaus)
   -  More information can be found [here](https://en.wikipedia.org/wiki/Simulated_annealing)


### Informed Search Techniques

The informed search algorithms are provided with additional information other than the problem space information which helps to find the solution more efficiently. On contrary, The uninformed search algorithms are only provided with the information in the problem statement, and no other information and hence termed as *blind search*.

1. A-star algorithm

   -  It is complete in finite spaces.
   -  It is optimal.
   -  Explores the node which has the minimum sum of distance covered yet and estimated distance to destination, i.e minimum estimated distance from source to destination. Hence it does not explore nodes which are have larger estimated distances from source to destination via a path from that node.
   -  Frontier used is priority queue which has more implementation complexity.
   -  Requires large memory which is proportional to the number of currently expanded nodes (for storing frontier and explored set).
   -  eg. Robot Pathing
   -  More information can be found [here](https://en.wikipedia.org/wiki/A*_search_algorithm)

---

## Usage

Each program can be run by entering the command :

> python3 <program_name>