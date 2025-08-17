#%% Graph class

# Adjacency List
class Graph:
    """
    A graph class used to represent the city's map with train stations, locations, and roads.
    During Dijkstra, the graph will generate a multi-layered graph where there will be C layers, with
    C being the cycle time of the friend. This allows us to keep track of the state of each vertex in each layer
    and allow our Dijkstra to run on the multi-layered graph.
    Due to our constraints of 20 stations and 5 minute maximum travel time, our upper bound of C will be 100, meaning
    there can only be a maximum of 100 layers in the graph. This also means we can treat our C as a constant in our
    analysis.
    """
    def __init__(self, V):
        """
        Function Description:
          Initializes a graph object with a list of vertices and sets the cycle_time and intercepts attributes to None.
          cycle_time is the time for the friend to complete a loop/cycle, intercepts is a tuple that is later used
          to store information regarding the shortest path to intercept the friend. Locations passed in the input are
          treated as vertices in the graph while roads are treated as edges.
        
        Input:
          V: a list of integers, the vertices id (locations) in the graph
          
        Returns:
          None, initializes the graph object with the vertices
        
        * L = number of vertices/locations
        Time Complexity: O(L)
          Time complexity for the init function comes from initializing an empty array for the vertices with length L. Furthermore,
          we will loop through the list of vertices to create a vertex object for each location, which will also take O(L) time.
          this gives us O(2L) which is simplified to O(L).
        
        Aux Space Complexity: O(L)
          Aux space complexity comes from us initializing a list of vertices with length L, taking up O(L) space for auxiliary space.
        
        Total Space Complexity: O(L)
          Total space complexity comes from our aux space complexity and input space complexity, where our input space is O(L) since
          we have a list of vertices (locations) as input and our aux space is O(L) since we are initializing a list of vertices with length L.
          this gives us O(2L) which is simplified to O(L).
        """
        self.vertices = [None] * len(V)
        self.cycle_time = None
        self.intercept = None
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])
    
    def reset_vertices(self):
        """
        Function Description:
          Resets the vertices in the graph to their initial state, modified to account for multi-layered graphs.
          This function resets the discovered, visited, index, cost, time, and previous attributes of every vertex in every layer.
          The function does this by duplicating the vertices in the graph and creating a new array of vertices for each layer.
          There will be as many layers as the friend's cycle time in minutes, where each layer will hold its own collection
          of vertices. This allows us to keep track of the state of each vertex in each layer.
        
        Input:
          None
        
        Returns:
          None, reduplicates the vertices in the graph in each layer, effectively resetting all states of the vertex
        
        * C = cycle_time/number of layers, L = number of locations
        Time Complexity: O(L)
          Since we are duplicating every vertex in the graph C times, the time complexity of this function is O(C*L). This is due to the
          fact we need to iterate C times (the outer loop) to duplicate a vertex and adding them to each layer. Furthermore, since every
          vertex needs to be duplicated, then we have an inner loop that loops L times. So, the time complexity of the function is O(C*L)
          which can be simplfied to O(L) due to C being treated as a constant (upper boundary of 100).
        
        Aux Space Complexity: O(CL) = O(L)
          Since we are duplicating each vertex C times and storing it in a new array, we will have O(C * L) space complexity to reserve space
          to store the vertices in each layer. However, since C is treated as a constant, we can simplify this to O(L) space complexity.
        
        Total Space Complexity: O(L) + O(L) = O(L)
          Since we are accessing the self.vertices array which as a size of L, we are treating this as our input space complexity. When we add
          this with our space complexity of O(L), we get a total space complexity of O(L + L) which can be simplified to O(L).
        """
        layers = self.cycle_time # our number of layers is equivalent to the friend's cycle time in minutes
        self.layers = [None] * layers
        
        # duplcating vertices to each layer # O(C*L) simplified to O(L)
        for i in range(layers):
            new_layer = [None] * len(self.vertices)
            for j in range(len(self.vertices)):
                new_layer[j] = Vertex(self.vertices[j].id)
                new_layer[j].layer = i
            self.layers[i] = new_layer
            
    def dijkstra(self, source):
        """
        Function Description:
          Finds the shortest path from a source to every other node in the graph, modified to account for multi-layered graphs, meaning
          we will find the shortest path to every visitable vertex in every layer.
        
        Approach Description:
        
          * L = locations, R = roads, C = cycle_time/number of layers
              
          The Dijkstra's algorithm is modified to account for multi-layered graph, where each traversal to a new node will result in us being a different layer
          based on the time taken to reach that node. The number of layers is equal to the cycle time of the friend. Here's how Dijkstra works to solve the problem:
          1.  Resetting the vertices by recreating the layers and reduplicating our vertices to each layer, done to ensure we can track different states of each
              vertex in each layer.
          2.  Creating a min heap of size C * L to potentially store every vertice in every layer, ensures heap is only full if every location is added in the heap.
          3.  Dijkstra runs from the source location, where our Dijkstra will be able to traverse between layers based on the time taken to reach a vertex modulus
              by the friend's cycle time.
          4.  Since a vertex can have different states in different layers, this effectively allows us to revisit a location in different layers.
          5.  When a vertex is visited, Dijkstra checks if the vertex is a station, and if it is, we check if we have successfully intercepted the friend.
          6.  Our interception data is stored as a tuple in the graph as an attribute, and it will continuously be updated if we find a better path to intercept.
              The better path is defined as a path that has a lower cost, or equal cost but lower time.
        
        Input:
          source: an integer, the start/source of our Dijkstra algorithm
        
        Returns:
          None, finds the shortest path to every reachable node in the multi-layered graph
        
        * L = locations, R = roads, C = cycle_time/number of layers
        Time Complexity: O(R log L)
          Time complexity of our Dijkstra stems from several different operations, which we will break down in steps:
            1.  Resetting our vertices and creating layers, takes O(L) complexity as explained in reset_vertices()
            2.  Creating our min heap of size C * L, takes O(C * L) time complexity to create the heap.
            3.  Doing edge relaxation for every vertex we visit, where we will have O(C * R * log(C * L))) time complexity since we have to account
                for our multilayered graph and the cost of minheap operations (add, sink, rise, update)
          
          Since we know that the upper bound of C is 100, we can treat C as a constant and remove it from our analysis, this gives us a total complexity
          of O(L + L + R log L), which we will simplify to O(R log L) since R >= L.
            
        Aux Space Complexity: O(L)
          Our aux space complexity comes from the space required for the min heap, where we need to reserve space for C * L vertices, and resetting
          our vertices, which is also O(L) which is explained previously in reset_vertices(). Since C is treated as a constant, we can simplify this to O(L).
        
        Total Space Complexity: O(L + R)
          Our total space complexity accounts for the space required for the graph and Dijkstra. The graph will take O(R + L) space complexity since we 
          need to store the locations, roads, and layers, but since R >= L, we can simplify this to O(R). Taking into account the space required by the graph 
          and our aux space, we get that our total space complexity is O(L + R).
        """
        self.reset_vertices()
        
        # starting/source vertex, so cost 0, time 0, and no previous vertex
        source = self.layers[0][source]
        source.cost  = 0
        source.time = 0
        source.previous = None
        
        min_heap = MinHeap(self.cycle_time * len(self.vertices))  # initializing size to fit vertices * layers
        min_heap.add(source) # adding source vertice to heap
        source.discovered = True
        
        # Dijkstra starts running
        while len(min_heap) > 0:
            u = min_heap.get_min()
            original_vertex = self.vertices[u.id] # get the original vertex object from the graph
            # since we aren't duplicating edges nor any additional information of vertices that are stations, we use
            # the original vertex to get the edges and other information we add in preprocessing
            
            u.visited = True
            
            # checking if we intercept friend, and updating current known shortest path
            if original_vertex.is_station and u.time % self.cycle_time == original_vertex.time_from_source:
                if self.intercept: # if we have previously intercepted, check if we have a better path
                    if u.cost < self.intercept[2]:
                        self.intercept = (u.id, u.layer, u.cost, u.time)
                    elif u.cost == self.intercept[2] and u.time < self.intercept[3]:
                        self.intercept = (u.id, u.layer, u.cost, u.time)
                else: # first interception, set intercept data
                    self.intercept = (u.id, u.layer, u.cost, u.time)

            # doing edge relaxation for current vertex for all edges to its adjacent vertices
            for edge in original_vertex.edges:
                new_time = (u.time + edge.time)
                next_layer = new_time % self.cycle_time # get the layer of the adjacent vertex, based on time taken
                v = self.layers[next_layer][edge.v] # getting adjacent vertex in corresponding layer
                
                if not v.discovered:
                    v.discovered = True
                    v.cost = u.cost + edge.cost
                    v.previous = u
                    v.time = new_time
                    min_heap.add(v)
                    
                elif not v.visited: # if vertex visited, cost & time finalized, skip it
                    new_cost = u.cost + edge.cost
                    if new_cost < v.cost or new_cost <= v.cost and new_time < v.time:
                        v.previous = u
                        v.time = new_time
                        min_heap.update_node(v, new_cost) # updating vertex in heap

    def add_edges(self, edges):
        """
        Function Description:
          Adds edges to the graph by iterating through a list of edges and adding them to the vertices.
          
        Input:
          edges: a list of tuples containing edge information (start_vertex, end_vertex, cost, time)
            * in the context of the assignment this is roads
          
        Returns:
          None, adds edges to the graph
        
        * R = Number of edges/roads (based on input)
        Time Complexity: O(R)
          The time complexity in this function is O(R) since we iterate through every edge (road) given in the input
          and add each one to the corresponding vertice in the graph.
          
        Aux Space Complexity: O(R)
          The aux space complexity comes from appending each edge to the vertices edge list, which requires O(R) space
          since we need to store each edge (road) in the graph
          
        Total Space Complexity: O(2R + L) = O(R)
          Since we have a list of edges as an input and we need to store them in the graph, our input space will be O(R + L),
          with R being the input list of edges (roads) and L being the list of vertices (locations) in the graph. 
          This means our total space complexity is O(L + R + R) = O(R + L) = O(R) since R >= L.
        """
        for edge in edges:
            u = edge[0]
            v = edge[1]
            cost = edge[2]
            time = edge[3]
            current_edge = Edge(u, v, cost, time)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)

class Vertex:
    """
    The Vertex class represents a node in the graph or a location in the city. Each vertex holds information such as its id, outgoing edges, and different
    states used in Dijkstra's algorithm. The most notable attribute is the layer, which is used to keep track which layer in the multilayered graph the
    vertex is in. The cost, time, previous, index, discovered, and visited are attributes used in Dijkstra's algorithm to keep track of the state of the vertex
    which helps in finding the most optimal path to our friend.
    """
    def __init__(self, id):
        """
        Function Description:
          Initializes a vertex object with an id, empty edges list, is_station boolean check, and attributes used
          in Dijkstra such as layer, cost, previous, time, index, discovered, and visited.
          
        Input:
          id: an integer, the id of the vertex
        
        Returns:
          None, initializes the vertex object
        
        Time Complexity: O(1)
          No loops, we are simply initializing primitive values and an empty list, time complexity of O(1).
        
        Aux Space Complexity: O(1)
          Only constant space is required to store the values when initializing the vertex object, O(1) aux space complexity.
        
        Total Space Complexity: O(1)
          Our aux space complexity is O(1) and our input is a single integer, which is also O(1), this gives us a total space
          complexity of O(1).
        """
        self.id = id
        self.edges = []
        self.is_station = False
        self.layer = None
        self.cost = None
        self.previous = None
        self.time = None
        self.index = None
        self.discovered = None
        self.visited = None
    
    def add_edge(self, edge):
        """
        Function Description:
          Adds an edge to the vertex's edge list.
        
        Input:
          edge: an Edge object, the edge to add to the vertex
        
        Returns:
          None, adds edge to the vertex's edge list
        
        Time Complexity: O(1)
          While we are appending an edge to the list, we can assume that appending to a list is O(1) due to amortized complexity.
        
        Aux Space Complexity: O(1)
          Since we are only adding a single edge to the vertex's edge list, the aux space complexity is O(1) because we do not need
          to reserve any additional space.
          
        Total Space Complexity: O(R)
          Since we are accessing the list of edges in the vertex and adding an edge to it, the list of edges stored in the vertex
          acts as our input. This has an upper bound of O(R) since we can have a maximum of R edges in the graph. So, our total space
          complexity is O(R).
        """
        self.edges.append(edge) # add edge to vertex
    
    def __lt__(self, other):
        """
        Function Description:
          Compares two vertices based on their cost and time attributes, true if the first vertex has a smaller cost or equal cost
          but lower time
        
        Input:
          other: a Vertex object, the vertex to compare to
        
        Returns:
          True if the first vertex has a smaller cost or equal cost but lower time, False otherwise
        
        Time Complexity: O(1)
          We are only performing comparisons of integers, O(1) complexity for such operations.
          
        Total Space Complexity: O(1)
          Only a constant amount of space is used, O(1) space complexity.
        """
        return self.cost < other.cost or (self.cost == other.cost and self.time < other.time)

    def __gt__(self, other):
        """
        Function Description:
          Compares two vertices based on their cost and time attributes, true if the first vertex has a greater cost or equal cost
          but greater time
          
        Input:
          other: a Vertex object, the vertex to compare to
        
        Returns:
          True if the first vertex has a greater cost or equal cost but greater time, False otherwise
        
        Time Complexity: O(1)
          We are only performing comparisons of integers, O(1) complexity for such operations.
        
        Total Space Complexity: O(1)
          Only a constant amount of space is used, O(1) space complexity.
        """
        return self.cost > other.cost or (self.cost == other.cost and self.time > other.time)
    
    def __le__(self, other):
        """
        Function Description:
          Compares two vertices based on their cost and time attributes, true if the first vertex has a smaller cost or equal cost
          but lesser or equal time.
        
        Input:
          other: a Vertex object, the vertex to compare to
        
        Returns:
          True if the first vertex has a smaller cost or equal cost but lesser or equal time, False otherwise
        
        Time Complexity: O(1)
          We are only performing comparisons of integers, O(1) complexity for such operations.
        
        Total Space Complexity: O(1)
          Only a constant amount of space is used, O(1) space complexity.
        """
        return self.cost <= other.cost or (self.cost == other.cost and self.time <= other.time)
    
    def __ge__(self, other):
        """
        Function Description:
          Compares two vertices based on their cost and time attributes, true if the first vertex has a greater cost or equal cost
          but greater or equal time.
        
        Input:
          other: a Vertex object, the vertex to compare to
        
        Returns:
          True if the first vertex has a greater cost or equal cost but greater or equal time, False otherwise
        
        Time Complexity: O(1)
          We are only performing comparisons of integers, O(1) complexity for such operations.
        
        Total Space Complexity: O(1)
          Only a constant amount of space is used, O(1) space complexity.
        """
        return self.cost >= other.cost or (self.cost == other.cost and self.time >= other.time)
    
    def __eq__(self, other):
        """
        Function Description:
          Compares two vertices based on their cost and time attributes, true if both vertices have the same cost and time
        
        Input:
          other: a Vertex object, the vertex to compare to
        
        Returns:
          True if both vertices have the same cost and time, False otherwise
        
        Time Complexity: O(1)
          We are only performing comparisons of integers, O(1) complexity for such operations.
        
        Total Space Complexity: O(1)
          Only a constant amount of space is used, O(1) space complexity.
        """
        return self.cost == other.cost and self.time == other.time
        
class Edge:
    """
    The edge class represents a road between two locations (vertices) in the graph. Each edge stores the start vertex, end vertex, cost,
    and time taken to traverse the edge.
    """
    def __init__(self, u, v, cost, time):
        """
        Function Description:
          Initializes an edge object with start vertex, end vertex, cost, and time.
          
        Input:
          u: an integer, the start vertex of the edge
          v: an integer, the end vertex of the edge
          cost: an integer, the cost of the edge
          time: an integer, the time taken to traverse the edge
        
        Returns:
          None, initializes the edge object
        
        Time Complexity: O(1)
          Initializing edge object with start vertex, end vertex, cost, and time, which are all
          primitive values (integer), giving us time complexity of O(1)
        
        Total Space Complexity: O(1)
          Initializing edge object with just primitive values of integers, which only requires
          space for the integers, giving us a space complexity of O(1).
        """
        self.u = u
        self.v = v
        self.cost = cost
        self.time = time

#%% MinHeap class
class MinHeap:
    """
    A modified MinHeap implementation made to support the Dijkstra algorithm. The MinHeap is used to store the vertices in the graph
    that are discovered during Dijkstra. The base code is taken from FIT1008 MaxHeap and modified to a MinHeap and further modified
    to better fit the assignment.
    """
    def __init__(self, max_length):
        """
        Function Description:
          Initializes a MinHeap object with a maximum length given as an input and creates an
          empty array of the given max length.
        
        Input:
          max_length: an integer, the maximum length of the heap
        
        Returns:
          None, initializes the min heap object with the given max length
        
        * L = number of vertices/locations in the graph
        Time Complexity: O(CL) = O(L)
          The time complexity of this function comes from initializing an empty array of length max_length.
          For the context of this assignment, this minheap is only utilized for storing locations in the dijkstra.
          While we may potentially store C * L vertices in the heap, we can treat C as a constant since there can
          only be a maximum of 100 layers for our graph. So, we simplify the time complexity to O(L). 
        
        Total Space Complexity: O(CL) = O(L)
          Given that the input is simply an integer, our input space complexity is O(1). For our aux space complexity,
          we are creating an array of length max_length, which in the context of the assignment would be of size
          C * L. So, our aux space complexity is O(CL), which we can simplify to O(L) since C is treated as a constant.
        """
        self.array = [None] * (max_length+1)
        self.length = 0
        self.max_length = max_length
        
    def rise(self, i):
        """
        Function Description:
          Rises a specific element in the heap to its correct position in the heap, modified to include updating
          the index (position in the heap) of each vertex.
        
        Input:
          i: an integer, the index of the element to rise
        
        Returns:
          None, rises the element to its correct position in the heap
        
        * L = number of elements in the heap, worst case num of locations * layers
        Time Complexity: O(log L)
          The time complexity of this function is O(log L) since worst case we are rising the element from the bottom
          of the heap to the top of the heap. In the context of this assignment, the worst case is when every location in
          every layer is currently in the heap, giving us a complexity of O(log(C * L)) which we can simplify to O(log L)
          since C can be treated as a constant.
        
        Aux Space Complexity: O(1)
          The function doesn't use any extra space, it simply interacts with the array in the heap. So, the aux space
          complexity is O(1)
        
        Total Space Complexity: O(L)
          The total space complexity of the function is O(L) from aux + input, where the array of the heap is of size L.
          This acts as the input so we will have space complexity of O(L + 1) or O(L) when simplified.
        """
        item = self.array[i]
        
        while i > 1 and item < self.array[i // 2]:
            self.array[i] = self.array[i // 2] # move parent down
            self.array[i].index = i # change index of parent to child
            i = i // 2 # moving up the heap
            
        self.array[i] = item
        self.array[i].index = i # update pos of risen vertex
    
    def sink(self, i):
        """
        Function Description:
          Sinks a specific element to its correct position in the heap
          
        Input:
          i: an integer, the index of the element to sink
        
        Returns:
          None, sinks the element to its correct position in the heap
        
        * L = number of elements in the heap, worst case num of locations * layers
        Time Complexity: O(log L)
          The time complexity of this function is O(log L) worst case since we may potentially be sinking an element at
          the root of the heap to the bottom of the heap. If we had every location in every layer currently added in the
          heap, we would have a complexity of O(log(C * L)) which we can further simplify to O(log L).
        
        Aux Space Complexity: O(1)
          The function doesn't use any extra space and simply interacts with the array in the heap, so the aux
          space complexity is O(1)
        
        Total Space Complexity: O(L)
          The total space complexity of the function is O(L) from aux + input, since the array of the heap is of size L.
          This array actas as the input so we will have a total space complexity of O(L + 1) or O(L) when simplified.
        """
        item = self.array[i]
        
        while 2 * i <= self.length:
            min_child = self.smallest_child(i) # get index of the smaller child
            if self.array[min_child] >= item:
                break # if smallest child is equal or greater, item is at correct position
            self.array[i] = self.array[min_child]
            self.array[i].index = i # update position of the swap
            i = min_child        

        self.array[i] = item
        self.array[i].index = i # update pos of sunk vertex
    
    def update_node(self, node, new_cost) -> None:
        """
        Function Description:
          Updates the cost of a node in the heap and rises it to the correct position in the heap.
        
        Precondition:
          The node being updated in the heap must be updated with a cost that is less than or equal to the current cost.
          This is because we don't have a sink() call, only rise.
        
        Input:
          node: a Vertex object, the node to update in the heap
          new_cost: an integer, the new cost to set for the node
      
        Returns:
          None, updates the node in the heap and rises it to the correct position
        
        * L = number of elements in the heap, worst case num of locations * layers
        Time Complexity: O(log L)
          The complexity of this function primarly stems from calling rise(), which in worst case we are updating a node at the
          bottom of the heap and rising it all the way up to the root. This has a complexity of O(log L).
        
        Aux Space Complexity: O(1)
          The function doesn't use any extra space and simply interacts with the array in the heap, so the aux space complexity
          is O(1)
        
        Total Space Complexity: O(L)
          The total space complexity of the function is O(L) from aux + input, since we are interacting with the array of the heap
          to get the node we have to update and rising the node. This array acts as the input so our total space complexity
          is O(L + 1) or O(L) simplified.
        """
        # Using the index stored in our vertex, we can find the Heapnode object in our array
        self.array[node.index].cost = new_cost
        self.rise(node.index)
    
    def add(self, element) -> bool:
        """
        Function Description:
          Adds an element to the heap at the bottom of the heap and rises it to its correct position.
        
        Input:
          element: a Vertex object, the element to add to the heap
        
        Returns:
          None
        
        * L = number of elements in the heap, worst case num of locations * layers
        Time Complexity: O(log L)
          The time complexity of this function is O(log L) since we are adding an element to the bottom of the heap and rising it
          to its correct position. In the context of this assignment, the worst case is when every location in every layer is currently
          in the heap, giving us a complexity of O(log(C * L)) which we can simplify to O(log L) since C can be treated as a constant.

        Complexity:
            Best case complexity: O(1) - No rising required
            Worst case complexity: O(logn) - New largest element (rises to the root)
            n is the number of elements currently in the heap
        """
        if self.is_full():
            raise IndexError
        
        self.length += 1
        self.array[self.length] = element
        element.index = self.length # update index of vertex to the new position in the heap
        self.rise(self.length)
    
    def smallest_child(self, i):
        if 2 * i == self.length or self.array[2 * i] < self.array[2 * i + 1]:
            return 2*i
        else:
            return 2*i + 1
    
    def get_min(self) -> int:
        """
        Returns the minimum element in the heap and removes it.

        Complexity:
            O(logn) - Sink the root down to its correct position
            n is the number of elements currently in the heap
        """
        if self.length == 0:
            raise IndexError

        min_element = self.array[1]
        self.length -= 1
        
        # take last item in heap and put to root, then sink
        if self.length > 0:
            self.array[1] = self.array[self.length+1] 
            self.sink(1)
        
        return min_element
    
    def __len__(self):
        """
        Function Description:
          Returns the number of elements currently in the heap
        
        Input:
          None
        
        Returns:
          An integer, the number of elements in the heap
        
        Time Complexity: O(1)
          We are simply accessing an attribute which is an integer and returning it, requiring constant time, O(1) complexity.
        
        Total Space Complexity: O(1)
          Only a constant amount of space is required to return the length of the heap, O(1) space complexity.  
        """
        return self.length
    
    def is_full(self):
        """
        Function Description:
          Checks if the heap is full by comparing the length of the heap to the maximum length
        
        Input:
          None
        
        Returns:
          A boolean, True if the heap is full, False otherwise
        
        Time Complexity: O(1)
          We are simply accessing two attributes and doing an integer comparison, which only requires a constant time, O(1) complexity.
        
        Total Space Complexity: O(1)
          Only a constant amount of space is required to return the boolean value, O(1) space complexity.
        """
        return self.length == self.max_length

def preprocess(roads, stations, friendStart):
    """
    Function Description:
      The function preprocesses the graph and input, creating the graph and adding the edges and vertices.
      The function also calculates things that are needed for the modified Dijkstra's algorithm to work, 
      such as cycle_time and time_taken for each station node/vertex
    
    Input:
      roads: a list of tuples containing the road information (start, end, cost, time)
      stations: a list of tuples containing the station information (location, time)
      friendStart: the starting location of the friend
    
    Returns:
      my_graph, a Graph object with all the vertices and edges added, and the cycle_time attribute set.
    
    Time Complexity: O(2R + 2S + L) = O(R)
    
      * R = number of roads, S = number of stations, L = number of locations
    
      Total time complexity of O(R + S + L + R + S) from finding max_loc_id, processing cycle time, initializing vertice array, 
      adding graph edges, and adding station information.
      
      This gives us a complexity of O(2R + 2S + L), but since we know that R >= S >= L, we can simplify this to O(R) time complexity.
      
    Aux Space Complexity: O(R+L) = O(R)
    
      * R = number of roads, S = number of stations, L = number of locations
      
      In this function, extra space is required to store vertices and edges in the graph, which is O(R + L) space complexity.
      Though, we know that R >= L, so we can simplify this to O(R) space complexity.
    
    Total Space Complexity: O(R + S + R + L) = O(R)

      We can calculate total space complexity from input space complexity + aux space complexity, where our input is O(R + S) which can be
      simplified to O(R) since R >= S, and since our aux space is O(R + L), we will have O(R + R + L), which can be simplified to O(R)
    """
    # find number of locations
    max_loc_id = 0
    for i in range(len(roads)): # O(R) time comp
        if roads[i][0] > max_loc_id:
            max_loc_id = roads[i][0] 
        if roads[i][1] > max_loc_id:
            max_loc_id = roads[i][1]
    
    # processing stations
    cycle_time = 0
    friend_start_index = None
    for i in range(len(stations)): # O(S) time comp
        if stations[i][0] > max_loc_id:
            max_loc_id = stations[i][0]
        if stations[i][0] == friendStart:
            friend_start_index = i
        cycle_time += stations[i][1]
    
    # initializing the graph
    my_graph = Graph([i for i in range(max_loc_id + 1)])
    my_graph.add_edges(roads) # O(R) time comp to add everything to the graph
    
    my_graph.cycle_time = cycle_time # adding to graph as attribute for easy usage
    
    # adding information to station nodes/vertices
    time_taken = 0
    for i in range(len(stations)): # O(S) time comp
        station_index = stations[(friend_start_index + i) % len(stations)]
        my_graph.vertices[station_index[0]].time_from_source = time_taken
        # time taken equals to time it takes to reach from source, used to check if can intercept
        my_graph.vertices[station_index[0]].is_station = True
        time_taken += station_index[1]
    
    return my_graph
        
#%% run test cases
def intercept(roads, stations, start, friendStart):
    """
        Function Description: 
          The function finds the shortest path from your start location to intercept your friend. The "shortest" path is defined as the path with
          the least cost and the least time taken to intercept your friend. The function uses a modified Dijkstra's algorithm to find the shortest 
          path in a graph with layers.
        
        Approach Description: 
        
          * R = number of roads, S = number of stations, L = number of locations
          
          1. After receiving the input, we will preprocess the input to get information such as:
            1.1 The number of locations through the max location id given in roads
            1.2 Processing the time it takes for the friend to complete a cycle
            1.3 Creating a graph with the list of locations as vertices and adding each road as edges. Furthermore, saving the cycle of the friend
                as an extra attribute of the graph
            1.4 Adding extra information like time_taken to get to the station from friendStart and setting is_station to True.
          
          2. After preprocessing, we will run a modified Dijkstra algorithm which will do the following steps:
            2.1 Reset vertices and generate layers for each location, to store different states in each layer, each location (vertice) will store
                an array with a length of however many layers that is determined by the friend's cycle time.
          
          # Preprocessing phase
          This function initializes all the vertices and edges in the graph, while also preprocessing information regarding the friend's travel time.
          We know that the friend will travel in a loop from station to station, meaning we can preprocess the time taken by the friend to reach each station
          and the length of the cycle for the friend (in minutes). The length of the cycle will determine the number of layers we need to create for the graph.
          This takes a time complexity of O(R) (written in the preprocess function) and space complexity of O(R).
          
          Instead of duplicating the nodes or the entire graph, the approach provided allows a singular vertex (node) to store multiple states at a time. This is done
          by initializing array of length layers for each attribute Dijkstra may need to use. Attributes such as cost, time, previous node, discovered, and visited will be stored
          in an array of length layers. This allows us to keep track of the state of each vertex in each layer, and allows us to use Dijkstra's algorithm to find the shortest path.

          Dijkstra will only run once, starting from our starting location (start) and traverse through our graph. The main modification done is the introduction of stepping into
          different layers. Based on the elapsed time (time it takes to reach a node from the source), we can determine which node in which layer we discover and visit.
          This allows our Dijkstra to effectively visit every visitable node in every visitable layer, which finds multiple interceptions with the friend.
          
          When finished, our algorithm will return the shortest path that we intercept our friend with, 
          which includes the cost of the path, the time of the path, and the path itself!
        
        Input:
          roads: a list of tuples containing the road information (start, end, cost, time)
          stations: a list of tuples containing the station information (location, time)
          start: the starting location
          friendStart: the starting location of the friend
        
        Returns:
          A tuple containing (total_cost, total_time, [path])
    """
    my_graph = preprocess(roads, stations, friendStart) # preprocess the graph and stations
        
    my_graph.dijkstra(start) # run dijkstra from start location
    
    # backtracking
    if my_graph.intercept is not None:
        intercept_result = my_graph.intercept
        vertex_id, layer = intercept_result[0], intercept_result[1]
        curr_vertex = my_graph.layers[layer][vertex_id]
        path = []
        while curr_vertex is not None:
            path.append(curr_vertex.id)
            curr_vertex = curr_vertex.previous
        
        path.reverse()
        
        return (intercept_result[2], intercept_result[3], path)
    else:
        return None

if __name__ == "__main__":
    roads = [(3, 1, 50, 4), (3, 4, 40, 2), (4, 1, 9, 2), (4, 5, 2, 2), (5, 6, 5, 2), (5, 1, 2, 4), (6, 1, 20, 2), (2, 3, 10, 2)]
    stations = [(1, 2), (2, 2)]
    friendStart = 1
    start = 3
    
    print(intercept(roads, stations, start, friendStart))
    
    friendStart = 1
    start = 5
    
    print(intercept(roads, stations, start, friendStart))
# %%
