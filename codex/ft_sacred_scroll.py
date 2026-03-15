import alchemy

if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    functions = [
        alchemy.elements.create_fire(),
        alchemy.elements.create_water(),
        alchemy.elements.create_earth(),
        alchemy.elements.create_air()
    ]
    print(f"alchemy.elements.create_fire(): {functions[0]}")
    print(f"alchemy.elements.create_water(): {functions[1]}")
    print(f"alvhemy.elements.create_earth(): {functions[2]}")
    print(f"alchemy.elements.create_air(): {functions[3]}")

    print()
    print("Testimg package-level access(controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    try:
        x = alchemy.create_earth()
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        x = alchemy.create_air()
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")
    print()
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
