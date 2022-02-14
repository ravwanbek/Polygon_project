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