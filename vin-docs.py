class Edge():
  """
  Class represents an edge in a graph which will connect 2 nodes together. It will store the connected node along
  with the weight of the edge.
  """
  def __init__(self, connected_node, time):
    """
    Function description:
      Initialises an Edge object with the connected node and the weight of the edge. Since all we do in init is assigning
      variables to the object, the time complexity is O(1) no matter what the input is.
    
    Input:
      connected_node: a Node object representing the node that this edge is connected to
      time: the weight of the edge, which in the context of CityMap is the amount of time it takes to travel from
            one location to another.

    Returns:
      None, but initialises an Edge object with the given connected node and weight.

    Time complexity: O(1)
      All we are doing is assigning values to the instance variables, which is an O(1) operation.

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).
    """
  

class Node():
  """
  This class represents a node in a graph, but in the context of the CityMap, it represents a location in the city. This
  class will hold information about the location, the time it takes to get to the location, the index of the location in
  the heap for dijkstra's, the other nodes connected to this node/location along with the time needed to get to those nodes,
  a visited and discovered flag used for dijkstra's, a uid for the node which indicates whether it is part of the graph
  thats carrying or not carrying a friend, a visitable flag to indicate if the node is visitable by a friend via train
  within 2 stops, a train rank to indicate how many stops away the friend is, a friend to indicate which friend
  is at the location, a previous node to indicate the previous node in the shortest path, and a pickup location to indicate
  where the friend is picked up in that shortest path.
  """
  def __init__(self, location, time, index, uid):
    """
    Function description:
      Initialises a Node object which represents a location in the city using the given location, time, index, and uid.
      It also initialises a default value for the other instance variables.
    
    Input:
      location: the location of the node in the city
      time: the time it takes to get to the location
      index: the index of the location in the heap for dijkstra's
      uid: the unique identifier for the node, indicating whether the node is in the graph for carrying a friend or not
           carrying a friend

    Returns:
      None, but initialises a Node object which contains information about the location in the city.

    Time complexity: O(1)
      All we are doing in the function is assigning values to the instance variables, which is an O(1) operation.

    Aux space complexity: O(1)
      Although there are a lot of instance variables, the ones initialised are currently constant and thus Only a constant amount of additional
      space is used, so the auxiliary space complexity is O(1).
    """

  def update_to_visitable(self, rank, friend):
    """
    Function description:
      Updates the node to be visitable by a friend within 2 train stops.
    
    Input:
      rank: the rank of the train stop, indicating how many stops away the friend is
      friend: the name of the friend that is at the location

    Returns:
      None, but updates the node to be visitable by a friend within 2 train stops.

    Time complexity: O(1)
      All we are doing is assigning values to the instance variables, which is an O(1) operation.

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).
    """

  def update_better_path(self, other):
    """
    Function description:
      Updates the node when a better path is found, be it the time it takes or the train rank.
    
    Input:
      other: the other node from which the better path results from

    Returns:
      None, but updates the node with the better path.

    Time complexity: O(1)
      All we are doing is assigning values to the instance variables, which is an O(1) operation.

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).
    """
    self.train_rank = other.train_rank
    self.pickup_location = other.pickup_location

  def __eq__(self, other):
    """
    Function description:
      Checks if the current node's time, train rank, and uid are equal to the other node's time, train rank, and uid.
    
    Input:
      other: the other node to compare with

    Returns:
      True if the time, train rank, and uid of the current node are equal to the other node, False otherwise.

    Time complexity: O(1)
      The only operations we're doing are comparisons between integers, which is O(1).

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).
    """
    return (self.time, self.train_rank, self.uid) == (other.time, other.train_rank, other.uid)
  
  def __ne__(self, other):
    """
    Function description:
      Checks if the current node's time, train rank, and uid are not equal to the other node's time, train rank, and uid.
    
    Input:
      other: the other node to compare with

    Returns:
      True if the time, train rank, and uid of the current node are not equal to the other node, False otherwise.

    Time complexity: O(1)
      We are calling __eq__() and negating the result, both of which are O(1)

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).
    """
    return not self.__eq__(other)
  
  def __lt__(self, other):
    """
    Function description:
      Compares the current node's time, train rank, and uid to the other node's time, train rank, and uid to check if
      the current node is less than the other node with respect to those aspects.
    
    Input:
      other: the other node to compare with

    Returns:
      True if the time, train rank, and uid of the current node are less than the other node, False otherwise.

    Time complexity: O(1)
      The only operations we're doing are comparisons between integers, which is O(1).

    Aux space complexity:
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).
    """
    return (self.time, self.train_rank, self.uid) < (other.time, other.train_rank, other.uid)
  
  def __le__(self, other):
    """
    Function description:
      Compares the current node's time, train rank, and uid to the other node's time, train rank, and uid to check if
      the current node is less than or equal to the other node with respect to those aspects.
    
    Input:
      other: the other node to compare with

    Returns:
      True if the time, train rank, and uid of the current node are less than or equal to the other node, False otherwise.

    Time complexity: O(1)
      We are calling __lt__() and __eq__(), both of which are O(1)

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).
    """
    return self.__lt__(other) or self.__eq__(other)
  
  def __gt__(self, other):
    """
    Function description:
      Compares the current node's time, train rank, and uid to the other node's time, train rank, and uid to check if
      the current node is greater than the other node with respect to those aspects.
    
    Input:
      other: the other node to compare with

    Returns:
      True if the time, train rank, and uid of the current node are greater than the other node, False otherwise.

    Time complexity: O(1)
      We are calling __lt__() and negating the result, both of which are O(1)

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).
    """
    return not self.__le__(other)
  
  def __ge__(self, other):
    """
    Function description:
      Compares the current node's time, train rank, and uid to the other node's time, train rank, and uid to check if
      the current node is greater than or equal to the other node with respect to those aspects.
    
    Input:
      other: the other node to compare with

    Returns:
      True if the time, train rank, and uid of the current node are greater than or equal to the other node, False
      otherwise.

    Time complexity: O(1)
      We are calling __gt__() and __eq__(), both of which are O(1)

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).
    """
    return not self.__lt__(other)
  
class CityMap():
  """
  This class represents a graph of a city, where the nodes represent locations in the city and the edges represent the
  connections between the locations. This class will be used to find the shortest path from one location to another, while
  also picking up a friend in a certain location given a specific condition, which is that the friend can only go travel
  through 2 train stops.
  """
  def __init__(self, roads, tracks, friends): 
    """
    * R = number of roads
    * L = number of locations
    * F = number of friends
    * T = number of tracks

    Function description:
      Initialises a CityMap object with the given roads, tracks, and friends. This function will connect the locations
      with each other via roads, and also find out which locations are visitable by our friends within 2 train stops.

    Approach description:

      * R = number of roads, L = number of locations, F = number of friends, T = number of tracks.

      - Connecting the locations:
        To connect each location to another via road, we must first create the location nodes. Due to needing to be able
        to index each location, we must use an array which means we would need to first find out the length of the array,
        or how many locations we will have.

        To do this, we have to first get the number of locations we will have. Since the locations will be numbered from
        0 to (L-1), and each location will be connected to a road, there will be at least 1 road that is connected to the
        (L-1)-th location. We can simply iterate through all the roads in O(R) time to get this number (L-1). Once we
        find this (L-1)-th location, we can simply add 1 to that number to get the number of total locations.

        Now that we have the number of locations, we can initialize 2 arrays of length L in O(2L) time to store our nodes.
        The reason we need 2 is because I am implementing the multi-layered graph approach where we will have 1 graph
        where we aren't carrying our friends, and another graph where we are carrying our friends. After creating the
        arrays, we can create the nodes and their connections/edges by simply iterating through the roads in another
        O(R) time.

        Total time so far: O(2R + 2L)

      - Searching for which nodes are visitable by our friends within 2 train stops
        We first must mark which nodes are visitable by our friends, and to do this we can simply loop through our friends
        array in O(F) time and mark whichever nodes/locations our friends are at, giving them a train distance/train rank
        of 0. After that, we can loop through our tracks in O(T) time to see if any of our locations/nodes are travelable
        from any of the nodes that have been previously been marked. If so, that means this node is also visitable by our
        friend since we have only gone through 1 train stop. We do this again, but only searching for nodes that are
        travelable from the nodes we marked in the previous loop. Since we do this twice, and we are looping through the
        tracks in O(T) time, that means it takes O(2T) time to mark all the travelable/visitable nodes.

        If any of the nodes we find are visitable by a friend within 2 train stops, we will connect the 2 graphs, graph
        carrying a friend and graph not carrying a friend, by adding an edge between 2 of the same locations but in
        different graphs with a weight of 0, essentially adding a "teleport" between the 2 graphs. This way, whenever
        we pick up a friend at a certain node, we can instantly go to the graph for carrying a friend.

        This is all done in O(F + 2T) time, making our total time complexity O(2R + 2L + F + 2T). 
    
    Input:
      roads: a list of tuples representing the roads in the city.
             Each tuple contains 3 elements: (start, end, time), with the start being the start location, the end being
             the end location, and the time being the time it takes to travel from the start location to the end location.
      tracks: a list of tuples representing the train tracks in the city.
              Each tuple contains 3 elements: (start, end, time), with the start being the start location, the end being
              the end location, and the time being the time it takes to travel from the start location to the end location.
      friends: a list of tuples representing the friends in the city.
               Each tuple contains 2 elements: the name of the friend and the location of the friend.

    Returns:
      None, but initialises a CityMap object with the given roads, tracks, and friends.

    Time complexity: O(2R + 2L + F + 2T) = O(5R + 2T) = O(R + T)
      In the worst case, we have that R = (L-1), meaning O(R) = O(L). Additionally, we will also have that F = L in the
      worst case, and since L = R as stated previously, O(F) = O(R). Adding up all our complexities, we have that
      O(2R + 2L + F + 2T) = O(2R + 2R + R + 2T) = O(5R + 2T) = O(R + T)


    Aux space complexity: O(2L + 2R) = O(4R) = O(R)
      Since we are storing our nodes in 2 arrays of length L, that means we must use at most O(2L) space to store these.
      Not only that, but we are also storing the edges/connections/roads associated with these locations, meaning in
      total, we will be storing R roads, but since we have 2 graphs, it will add up to O(2R). Similarly to time
      complexity, our worst case for aux space complexity when R = (L-1), meaning O(R) = O(L). With these being the case,
      O(2L + 2R) = O(2R + 2R) = O(4R) = O(R)

    Total space complexity: O(R + T + F + L)
      Since our input involves roads, tracks, and friends, while our aux space involves locations, removing the constants
      we have our total space complexity to be O(R + T + F + L).
    """

  def plan(self, start = 0, destination = 0):
    """
    * R = number of roads
    * L = number of locations

    Function description:
      Finds the shortest distance from the starting location to the destination location while also picking up a single
      friend and ensuring that the friend only travels the least required train stops for that distance.

    Approach description:

      * R = number of roads, L = number of locations

      We can simply use dijkstra's algorithm to find the shortest path from our source to destination in O(E log V) time,
      with our E being our roads which we have 2R of in total due to having 2 graphs, and our V being our number of locations,
      which we have 2L of since we have 2 graphs. The dijkstra has also been modified in such a way that it will not only
      prioritise the shortest distance but also the least amount of train stops (Further explained in the dijkstra function).
      This gives us a running complexity of O(2R log 2L)

      After completing dijkstra, we now have the shortest distance to our destination and also the ability to backtrack
      to our source node, giving us the shortest path albeit in reverse order. Aside from that, we must also make sure
      we do not include one of the "teleport" node in our path since we will have 2 of them due to having to travel from
      one of the "teleport" nodes to another. We can do this simply by looping through our path and checking for whether
      or not we have any side-by-side duplicates, since if we "teleport", they will be one after another in our path.
      This loop will be at worst O(2R) time in the case where we have to go through every road in both graphs. After
      that, we must also reset the nodes for the next time we want to call plan() again, and to reset the nodes we must
      iterate over every node which will be an additional O(2L).
      Our running complexity is now O(2R) + O(2R log 2L) + O(2L) = O( 2R + (2R log 2L) + 2L ). And since in the worst
      case O(R) = O(L) , we have a total complexity of O( 4R + (2R log 2L) ).   
    Input:
      start: the starting location
      destination: the destination location

    Returns:
      A tuple containing (time, [shortest path], name of friend, friend's pickup location)

    Time complexity: O ( 2R+(2R log 2L) ) = O(2R log 2L) = O(R log L)
      We get this complexity by adding up the time it takes to do dijkstra's and the post-processing to get the path of
      the shortest path.

    Aux space complexity: O(2L + 2L) = O(4R) = O(R)
      For dijkstra, we need to create a heap with a size of 2L to store our 2L number of locations, and in the worst case,
      our shortest path will contain all 2L nodes, meaning we must use an additional 2L memory to store all these nodes.
      This brings our total to O(2L + 2L) = O(4L), but remember that in the worst case, O(L) = O(R), so we have
      O(4L) = O(4R) = O(R).

    Total space complexity: O(R + L)
      Adding up the space complexities from dijkstra() and reset_nodes(), we get that our total space complexity
      including our input space is O(4R) + O(2L), giving us O(R + L) in total 
    """
  
  def get_location_count(self):
    """
    * R = number of roads

    Function description:
      Gets the number of total locations by looking at the max from all roads.
    
    Input:
      None

    Returns:
      None, but modifies the value of self.location_count to be the number of locations

    Time complexity: O(R)
      Since we have a for loop that loops through self.roads, this would happen in O(R) time.

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).

    Total space complexity: O(R)
      Since we are using our roads as our input, we must add that to our aux space to get the total space
    """

  def create_connections_between_locations(self, u, v, time):
    """
    * R = number of roads

    Function description:
      Adds the connections/edges/roads between two nodes, along with the time it takes to travel.
    
    Input:
      u: the first location/node
      v: the second location/node
      time: the time it takes to travel between the two nodes.

    Returns:
      None, but adds an edge/connection in the nodes' connections list.

    Time complexity: O(1)
      All we are doing is appending an Edge object to a list, which is all done in O(1) time

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).

    Total space complexity: O(R)
      Since our nodes can store at max R connections, we must add that to our auxiliary space
    """

  def create_locations(self):
    """
    * R = number of roads
    * L = number of locations

    Function description:
      Creates the nodes for all of the locations in the city, and adds connections between them based on the roads.
    
    Input:
      None

    Returns:
      None, but creates 2 arrays for the graphs' nodes and adds the connections between those nodes

    Time complexity: O(2R + 2L) = O(2R + 2R) = O(4R) = O(R)
      To get the number of locations, we must loop through all the roads in O(R) time, and then we must also initialise
      the 2 arrays of length L, giving us another O(2L), and then we also loop through the roads one last time to create
      the connections between all the nodes/locations, which is another O(R).
      In total, we have O(2L + 2R), but in the worst case, R = (L-1) which means O(R) = O(L), so
      O(2L + 2R) = O(2R + 2R) = O(4R) = O(R)

    Aux space complexity: O(2L) = O(2R) = O(R)
      We must store our 2L nodes in arrays, making us need another 2L space in memory. In the worst case, as mentioned
      before, O(L) = O(R), so O(2L) = O(2R) = O(R)

    Total space complexity: O(R + L) = O(R)
      Since our input involves our roads, we must add R to our aux space to get total space.
    """

  def get_visitable_locations(self):
    """
    * R = number of roads
    * L = number of locations
    * T = number of tracks
    * F = number of friends

    Function description:
      Finds out which nodes are visitable by friends within 2 train stops and marks them and updates their properties.
    
    Input:
      None

    Returns:
      None, but updates the properties of the nodes visitable by friends

    Time complexity: O(F + 2T) = O(L + 2T) = O(R + 2T) = O(R + T)
      We loop through our friends to see where our friends are at, which takes O(F) time. Then, we loop through our
      tracks twice, giving us another O(2T) complexity. Adding it up, we get O(F + 2T). In the worst case, every
      location has a friend, meaning F = L. And remember that the worst case is when R = L, so we have that F = L = R,
      so O(F + 2T) translates to O(R + 2T) = O(R + T)

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).

    Total space complexity: O(F + T + L) = O(L + T) = O(R + T)
      Since our inputs involve our friends and tracks, we have to add those to our total space complexity. In the worst
      case, every location has a friend, so F = L, and worst case R = L, so we have O(F + T) = O(L + T) = O(R + T)
    """

  def reset_nodes(self):
    """
    * R = number of roads
    * L = number of locations

    Function description:
      Resets the status for all the nodes once we have called plan()
    
    Input:
      None

    Returns:
      None, but resets the nodes to their default state before calling dijkstra()

    Time complexity: O(2L) = O(2R) = O(R)
      We iterate through all our locations, which is O(2L). And worst case, O(R) = O(L), so we have O(2L) = O(2R)

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).

    Total space complexity: O(L * R)
      Since we have to go through all 2L locations, and each location at worst has 2R roads, we need a total of
      2L * 2R space, and removing the constants we get L * R
    """

  def reset_node_stats(self, node):
    """
    * R = number of roads

    Function description:
      Resets a particular node's properties/statistics to its state before we ran dijkstra
    
    Input:
      node: the node whose properties we want to reset

    Returns:
      None, but this function resets the properties of a node

    Time complexity: O(1)
      All we are doing are assignment and if operations, which are all done in O(1) time.

    Aux space complexity: O(1)
      Only a constant amount of additional space is used, so the auxiliary space complexity is O(1).

    Total space complexity: Aux + input = O(R)
      Since our input is a node, and a node at the worst case contains R roads, we add that to our space complexity.
    """
      
  def dijkstra(self, source: int):
    """
    * R = number of roads
    * L = number of locations

    Function description:
      Finds the shortest path from a specific source to every other node in the graph.

    Approach description:
      We ues a min heap to keep track of which node currently has the shortest distance/time. Once we get the node with
      the shortest time/distance, we check all of the node's connections to see if the connected node has been discovered,
      if it hasn't, then we can add it to the heap with the new time since if the node hasn't been discovered, it will
      have a time of float('inf').

      If our current node's time, added with the time it takes to travel from the current node to the connected node,
      is less than that of the connected node's time, we will update the time. There are also a few things to update:
      the previous node, the train rank, and the pickup location. If the added time is less than the connected node's
      time, we must also consider a few things.

      If the node has been discovered, we can simply update the time, previous, pickup location, and train rank since we
      know that it indeed has a lower time to get there. But, if the node hasn't been discovered, it will always have a
      higher time compared to the time of the current node + the time it takes to get to that node since it will have a
      time of float('inf'). That means we should check if the train rank of the connected_node is higher than the one of
      the current node, and if it is only then we will update the train rank and pickup location.

      Besides that, we will also check for whether the new time it takes to get to the connected node is the same as
      the time currently stored in the connected node. If it is, then we will update the train rank and pickup location
      only if the train rank of the new path is lesser than the connected node's train rank.
    
    Input:
      source: the source location where we will start our dijkstra algorithm

    Returns:
      None, but updates the time of all the nodes to be the shortest time it takes to go from the source to the node

    Time complexity: O(2L + (2R log 2L)) = O(R log L)
      To initialize the heap, we require O(2L) time. To go through all of the connections in the nodes, we also require
      a complexity of O(2R) since there are 2 graphs, but every time we go through the connections, we might also update
      the node in the heap, causing it to rise() and/or sink(), which means in the worst case we will have to do
      O(2R * sink() or rise()) operations, which ends up being O(2R * (log 2L)).

    Aux space complexity: O(2L) = O(2R) = O(R)
      We have to create a min heap which will store all our nodes, and since we have 2L nodes, we will require O(2L)
      space to store them. Since in the worst case R = L, we have that O(2L) = O(2R)

    Total space complexity: Aux space + input space = O(R + L)
      Since our input for dijkstra will be all of our nodes, we must add L to the total space used in our algorithm.
      Removing all the constants, we end up with O(R + L)
    """


