from .elements import *


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    air = create_air()
    return f"Invisibility potion brewed with {air} and {create_water()}"


def wisdom_potion() -> str:
    f = create_fire()
    w = create_water()
    e = create_earth()
    a = create_air()
    return f"Wisdom potion brewed with all elements: {w}, {e}, {f} amd {a}"
