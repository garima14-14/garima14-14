import math


def calculate_circle_area(radious):
    area = math.pi * radious**2
    return area
# Example usage with a radious of 6 units
radious = 6
circle_area = calculate_circle_area(radious)
print(f"The area of the circle with radious {radious} is {circle_area}")
