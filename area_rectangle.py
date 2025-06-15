def area(h, b) -> float:
    """
    Calculate the area of a rectangle given its height and base.

    Parameters:
    h (float): The height of the rectangle.
    b (float): The base of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    print("__name__ is: ", __name__)
    return h * b

if __name__ == "__main__": # Entry point for the script
    # Example usage
    height = 5.0
    base = 10.0
    print("I am in main.")
    print(f"The area of the rectangle with height {height} and base {base} is: {area(height, base)}")