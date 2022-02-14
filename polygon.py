import math
class Polygon:
    """ 
    A class to represent a polygon.
    Polygon is a finite set of vertices in the plane.
    The vertices are stored in a list, each element of the list is a pair of coordinates (x, y).
    attributes:
        vertices: a list of vertices
    methods:
        area: calculate the area of the polygon
        distance: calculate the distance between two points
        sides: get all sides of the polygon
        angles: get all angles of the polygon        
        perimeter: calculate the perimeter of the polygon
        is_valid: validate the polygon
        centroid: calculate the centroid of the polygon
    """
    # Constructor with vertices
    def __init__(self, vertices: list):
        """
        Constructor with vertices.
        vertices: a list of vertices each element of the list is a pair of coordinates (x, y)
        """
        self.vertices = vertices

    #Define the method to validate the polygon
    def is_valid(self) -> bool:
        """
        Validate the polygon.
        Returns:
            True if the polygon is valid
            False if the polygon is invalid
        """
        pass
    
    # Calculate the area of the polygon
    def area(self) -> float:
        """
        Calculate the area of the polygon.
        """
        pass
    # Distance between two points
    def distance(self, p1: tuple, p2: tuple) -> float:
        """
        Calculate the distance between two points.
        Args:
            p1: a pair of coordinates (x, y)
            p2: a pair of coordinates (x, y)
        Returns:
            the distance between p1 and p2
        """
        # d = √[(x2 − x1)**2 + (y2 − y1)**2]
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt( pow(x2 − x1, 2) + pow(y2 − y1, 2))
        

    #Define the method to get all sides of the length of the polygon
    def sides(self) -> list:
        """
        Get all sides of the polygon.
        Returns:
            a list of all sides of the polygon
        """
        pass
     
     # Define the method to calculate the perimeter of the polygon
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the polygon.
        Returns:
            the perimeter of the polygon
        """
        
        pass

    #Define the method to calculate the angle between two sides
    def angles(self) -> list:
        """
        Calculate the angles of the polygon.
        Returns:
            a list of all angles of the polygon
        """
        pass
        
    #Define the method to calculate the centroid of the polygon
    def centroid(self) -> tuple:
        """
        Calculate the centroid of the polygon.
        Returns:
            a pair of coordinates (x, y)
        """
        pass

