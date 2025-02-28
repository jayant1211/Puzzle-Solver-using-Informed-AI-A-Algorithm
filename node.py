import copy
class Node:
    def __init__(self, data, level, fval):
        """
        Initialize a node in the search tree.
        
        Args:
            data: The puzzle state represented as a 2D list
            level: The depth level of the node in the search tree
            fval: The f-value (heuristic value) of the node
        """
        self.data = data
        self.level = level
        self.fval = fval
        self.direction = ''
    
    def movement(self, x1, y1, x2, y2):
        """
        Define movement direction when the blank space moves from (x1, y1) to (x2, y2).
        
        In the puzzle representation:
        - 'up' means the blank moves up (a tile moves down into the blank)
        - 'down' means the blank moves down (a tile moves up into the blank)
        - 'left' means the blank moves left (a tile moves right into the blank)
        - 'right' means the blank moves right (a tile moves left into the blank)
        
        Coordinates are in (row, column) format:
        (0,0) (0,1) (0,2)
        (1,0) (1,1) (1,2)
        (2,0) (2,1) (2,2)
        """
        # Moving vertically (same column)
        if x1 == x2:
            if y1 > y2:  # Blank moves up
                self.direction = 'left'
            else:  # Blank moves down
                self.direction = 'right'
        # Moving horizontally (same row)
        elif y1 == y2:
            if x1 > x2:  # Blank moves left
                self.direction = 'up'
            else:  # Blank moves right
                self.direction = 'down'
        
        return self.direction

    def generate_child(self):
        """
        Generate child nodes by moving the blank space in four directions.
        
        Returns:
            List of valid child nodes
        """
        x, y = self.find(self.data, '_')
        
        # Possible moves: up, down, left, right
        val_list = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        children = []
        
        for i in val_list:
            child = self.slide(self.data, x, y, i[0], i[1])
            child_direction = self.movement(x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level+1, 0)
                child_node.direction = child_direction
                children.append(child_node)
                
        return children
        
    def slide(self, puz, x1, y1, x2, y2):
        """
        Move the blank space in the given direction.
        
        Args:
            puz: Current puzzle state
            x1, y1: Current position of blank space
            x2, y2: Target position for blank space
            
        Returns:
            New puzzle state if move is valid, None otherwise
        """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
            
    
    def copy(self, root):
        """Create a deep copy of the given matrix"""
        return copy.deepcopy(root)  
            
    def find(self, puz, x):
        """
        Find the position of a specific value in the puzzle.
        
        Args:
            puz: The puzzle state
            x: The value to find (usually '_' for blank space)
            
        Returns:
            Tuple of (row, column) coordinates
        """
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j
