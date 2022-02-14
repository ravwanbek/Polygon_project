# Introduction to Polygon
Polygon are two-dimensional geometric objects composed of points and straight lines connecting those points.

Sample of Polygon:

![polygon](https://cdn-skill.splashmath.com/panel-uploads/GlossaryTerm/277097a6a870457e90553ed24cf46042/1548051233_Two-dimensional-2-D-shapes-circle-triangle-square-polygons.png
)

## Type of Polygon:
1. Triangle
2. Rectangle
3. Square
4. Pentagon

## Notation of triangle

![triangle](https://i.stack.imgur.com/1GkR3.png
)

## Properties of Polygons

1. Coords of vertices

![vertices](images/vertices.png
)

![coords](images/coords.png
)

2. Perimeter
3. Area
4. Centroid
5. Angle of each vertex

## Usage example:

```python

triangle = Polygon([(4.00,5.00), (1.50,2.00), (7.00,2.00)])
print(f'Area of the triangle: {triangle.area():.2f}')
# Output: Area of the triangle: 8.25
print(f'Perimeter of the triangle: {triangle.perimeter():.2f}')
# Output: Perimeter of the triangle: 13.65

print(f'Sides of the triangle: {triangle.sides()}')
print(f'Angles of the triangle: {triangle.angles()}')
```