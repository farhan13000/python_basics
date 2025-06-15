def area(h, b) -> float:
    """
    Calculate the area of a triangle given its height and base.

    Parameters:
    h (float): The height of the triangle.
    b (float): The base of the triangle.

    Returns:
    float: The area of the triangle.
    """
    print("__name__ is: ", __name__)
    return 0.5 * h * b

if __name__ == "__main__":
    # Example usage
    height = 5.0
    base = 10.0
    print("I am in main.")
    print(f"The area of the triangle with height {height} and base {base} is: {area(height, base)}")