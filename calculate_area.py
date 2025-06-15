import area_rectangle as area_rectangle
import area_triangle as area_triangle

def calculate_area_rectangle(height, base) -> float:
    """
    Calculate the area of a rectangle given its height and base.

    Parameters:
    height (float): The height of the rectangle.
    base (float): The base of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return area_rectangle.area(height, base)

def calculate_area_triangle(height, base) -> float:
    """
    Calculate the area of a triangle given its height and base.

    Parameters:
    height (float): The height of the triangle.
    base (float): The base of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return area_triangle.area(height, base)


area_rectangle: float = calculate_area_rectangle(5.0, 10.0)
area_triangle: float = calculate_area_triangle(5.0, 10.0)


print("I am in calculate_area.py.")
print(f"Area: {area_rectangle}")