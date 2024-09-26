# Tuple Examples

# RGB
def get_nice_purple():
    color = (255, 128, 33)
    return color


purple = get_nice_purple()
print(purple)

r, g, b = get_nice_purple()
print(r)
print(g)
print(b)

# Coordinates


def get_character_coords():
    return (3, 9)


position = get_character_coords()
print(position)

x, y = get_character_coords()
print(x)
print(y)

# tuples can be dict keys !
world = {(3, 9): "Jason"}

print(world[get_character_coords()])
