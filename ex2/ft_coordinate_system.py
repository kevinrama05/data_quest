from sys import argv

def valid_coordinates(coordinates: str) -> tuple[int, int, int] | bool:
    if coordinates[0] == "(" and coordinate[-1] == ")":
        coordinates = coordinates[1:]
        coordinates = coordinates[:-1]
    try:
        x, y, z = coordinates.split(",")
    except ValueError:
        return False
    try:
        x = int(x)
        y = int(y)
        z = int(z)
    except ValueError:
        return False
    c = (x, y, z)
    return c

if __name__ == "__main__":
    location = (5, 8, 10)
    checkpoint = (0, 0, 0)
    print("=== Game Coordinate System ===\n")
    print(f"Position created: {location}")
    print(f"Distance between {checkpoint} and {location}: {((location[0] + checkpoint[0])**2 + (location[1] + checkpoint[1])**2 + (location[2] + checkpoint[2])**2)**0.5:.2f}\n")
    coordinates = input("Parsing coordinatea: ")
    if valid_coordinates(coordinates) == False:
        print(
    f"""Error parsing coordinates: invalid literal for int() with base 10: '{coordinates}'
Error details - Type: ValueError, Args: ("invalid literal for int() with base 10: ’{coordinates}’",)
    """)
    else:
        location = valid_coordinates(coordinates)
        print(f"Position created: {location}")
        print(f"Distance between {checkpoint} and {location}: {((location[0] + checkpoint[0])**2 + (location[1] + checkpoint[1])**2 + (location[2] + checkpoint[2])**2)**0.5:.2f}\n")
 
    print("Unpacking demonstration: ")
    print(f"Player at x={location[0]}, y={location[1]}, z={location[2]}")
    print(f"Coordinates: X={location[0]}, Y={location[1]}, Z={location[2]}")
